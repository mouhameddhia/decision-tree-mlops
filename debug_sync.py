# debug_sync.py
import time
import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DebugHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print(f"🔍 Event type: {event.event_type}")
        print(f"🔍 Path: {event.src_path}")
        print(f"🔍 Is directory: {event.is_directory}")
        print("---")
    
    def on_modified(self, event):
        if not event.is_directory:
            print(f"🔄 MODIFIED: {os.path.basename(event.src_path)}")
            self.sync_to_github()
    
    def on_created(self, event):
        if not event.is_directory:
            print(f"🆕 CREATED: {os.path.basename(event.src_path)}")
            self.sync_to_github()
    
    def sync_to_github(self):
        try:
            print("🚀 Attempting to push to GitHub...")
            
            # Check git status first
            result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
            if result.stdout.strip():
                print(f"📝 Changes detected: {result.stdout}")
                subprocess.run(['git', 'add', '.'], check=True)
                subprocess.run(['git', 'commit', '-m', f'Auto-sync: {time.strftime("%Y-%m-%d %H:%M:%S")}'], check=True)
                subprocess.run(['git', 'push'], check=True)
                print("✅ Successfully pushed to GitHub!")
            else:
                print("ℹ️ No changes to commit")
                
        except Exception as e:
            print(f"❌ Error: {e}")

def start_debug():
    print("🐛 Starting DEBUG mode...")
    event_handler = DebugHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Debug stopped")
    observer.join()

if __name__ == "__main__":
    start_debug()

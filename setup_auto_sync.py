# setup_auto_sync.py
import subprocess
import os

def setup_auto_sync():
    print("⚙️ Setting up automatic GitHub sync...")
    
    # Install watchdog
    try:
        subprocess.run(['pip', 'install', 'watchdog'], check=True)
        print("✅ Watchdog installed")
    except:
        print("❌ Could not install watchdog - try: pip install watchdog")
        return
    
    print("✅ Auto-sync setup complete!")
    print("\n📋 NEXT STEP: Run -> python auto_sync.py")
    print("Then make changes to your files and watch them auto-push to GitHub!")

if __name__ == "__main__":
    setup_auto_sync()
# webhook_listener.py
import os
import hmac
import hashlib
import threading
import subprocess
import sys
from flask import Flask, request, jsonify

app = Flask(__name__)

# Optional: set GITHUB_WEBHOOK_SECRET in env to enable HMAC verification
GITHUB_SECRET = os.environ.get("GITHUB_WEBHOOK_SECRET")  # e.g. 'mysupersecret'


def verify_signature(payload, signature_header):
    """Verify GitHub webhook HMAC signature."""
    if not GITHUB_SECRET:
        return (
            True  # no secret configured -> skip verification (not recommended for prod)
        )
    if not signature_header:
        return False

    sha_name, signature = signature_header.split("=")
    if sha_name != "sha256":
        return False

    mac = hmac.new(GITHUB_SECRET.encode(), msg=payload, digestmod=hashlib.sha256)
    expected = mac.hexdigest()
    return hmac.compare_digest(expected, signature)


def run_pipeline():
    """Run the ML pipeline in a subprocess."""
    try:
        print("🚀 Starting pipeline subprocess...")
        # Use the current python interpreter (from activated venv) to run main.py
        subprocess.run([sys.executable, "main.py", "--all"], check=True)
        print("✅ Pipeline finished successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Pipeline failed: {e}")


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok"}), 200


@app.route("/webhook", methods=["POST"])
def webhook():
    """Handle GitHub webhook events."""
    event = request.headers.get("X-GitHub-Event", "")
    signature = request.headers.get("X-Hub-Signature-256", "")
    payload = request.get_data()

    # Verify HMAC signature (if secret provided)
    if not verify_signature(payload, signature):
        print("⚠️ Signature verification failed.")
        return jsonify({"message": "invalid signature"}), 401

    if event != "push":
        print(f"ℹ️ Ignored event: {event}")
        return jsonify({"message": "event ignored"}), 200

    print("🔔 Push event received — launching pipeline in background thread.")
    thread = threading.Thread(target=run_pipeline, daemon=True)
    thread.start()

    return jsonify({"message": "pipeline started"}), 200


if __name__ == "__main__":
    # Bind to 127.0.0.1 so local servers/ngrok can reach the server
    app.run(host="127.0.0.1", port=5000)

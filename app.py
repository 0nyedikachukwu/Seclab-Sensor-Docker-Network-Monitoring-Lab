from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

SUSPICIOUS_PATHS = ["/admin", "/.env", "/wp-login.php", "/login", "/config", "/.git"]

@app.before_request
def log_all_requests():
    ua = request.headers.get("User-Agent", "unknown")
    entry = f"{datetime.utcnow().isoformat()} - {request.method} {request.path} from {request.remote_addr} - UA: {ua}\n"
    print(entry, end="")

    if request.path in SUSPICIOUS_PATHS:
        print(f" ⚠️  SUSPICIOUS PATH HIT: {request.path} from {request.remote_addr}\n")

@app.route("/")
def index():
    entry = f"{datetime.utcnow().isoformat()} - visitor hit homepage from {request.remote_addr}\n"
    print(entry, end="")
    return "504 Gateway Timeout: The server did not respond in time. Please try again.\n", 504

@app.route("/log")
def log_entry():
    entry = f"{datetime.utcnow().isoformat()} - LOGIN ATTEMPT recorded from {request.remote_addr}\n"
    print(entry, end="")
    return "Error: Incorrect username or password. Please try again.\n", 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

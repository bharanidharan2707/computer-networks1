
from flask import Flask, render_template
import socket
import subprocess

app = Flask(__name__)

@app.route("/")
def home():

    # Get local IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    # Check internet connection
    try:
        result = subprocess.run(
            ["ping", "-n", "1", "1.1.1.1"],
            capture_output=True,
            text=True,
            timeout=3
        )

        if result.returncode == 0:
            status = "Connected"
        else:
            status = "Disconnected"

    except Exception:
        status = "Disconnected"

    return render_template(
        "index.html",
        ip=ip_address,
        status=status
    )

if __name__ == "__main__":
    app.run(debug=True)

import os
import psutil
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({
        "status": "up",
        "ip": os.getenv("HOST_IP", "127.0.0.1"),
        "cpu_usage": f"{psutil.cpu_percent()}%",
        "memory": f"{psutil.virtual_memory().percent}%"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

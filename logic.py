from flask import Flask, jsonify, render_template
import socket
import time

app = Flask(__name__)

def measure_ping(host='1.1.1.1', port=80):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        
        start_time = time.time()
        s.connect((host, port))
        end_time = time.time()
        
        s.close()
        
        latency = (end_time - start_time) * 1000
        return round(latency, 2)
    except Exception as e:
        return None
    finally:
        s.close()

@app.route('/')
def index():
    return render_template('index.html')

# API-эндпоинт для пинга
@app.route('/api/ping', methods=['GET'])
def api_ping():
    ping = measure_ping()
    return jsonify({'ping': ping})

if __name__ == '__main__':
    app.run(debug=True)


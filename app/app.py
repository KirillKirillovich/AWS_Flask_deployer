from flask import Flask, send_from_directory, abort, jsonify, Response
import os
import logging

app = Flask(__name__)

log_file_path = './logs/app.log'
start_page = './files'

if not os.path.exists('./logs'):
    os.makedirs('./logs')

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


@app.route('/')
def return_content():
    app.logger.info("Request received at /")
    file_path = os.path.join('./files', 'index.html')

    if os.path.exists(file_path):
        app.logger.info("Serving index.html")
        return send_from_directory('./files', 'index.html')
    else:
        app.logger.error("index.html not found")
        abort(404, description="File not found")


@app.route('/logs')
def logs():
    if os.path.exists(log_file_path):
        app.logger.info("Serving logs")
        with open(log_file_path, 'r') as log_file:
            log_content = log_file.read()
        return Response(log_content, mimetype='text/plain')
    else:
        app.logger.error("Log file not found")
        abort(404, description="Log file not found")


@app.route('/status')
def status():
    app.logger.info("Request received at /status")
    status = {
        "status": "healthy",
        "app": "Flask App",
        "version": "1.0.0"
    }
    return jsonify(status), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

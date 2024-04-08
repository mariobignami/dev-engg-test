from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Flask App! Use /files to list files and /hello for a greeting."


@app.route('/files', methods=['GET'])
def list_files():
    # List all files in the root directory
    files = []
    for entry in os.scandir('/'):
        if entry.is_file():
            files.append({"name": entry.name, "size": entry.stat().st_size})

    # Prepare the response object
    response = {
        "fileCount": len(files),
        "files": files
    }

    return jsonify(response)


@app.route('/hello', methods=['GET'])
def hello():
    # Fetch the MY_NAME environment variable, default to 'Damian' if not set
    name = os.getenv('MY_NAME', 'Damian')
    return f"Hello this is {name}"


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0')

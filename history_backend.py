from flask import Flask, request, jsonify
import os

app = Flask(__name__)

HISTORY_DIR = 'history'
os.makedirs(HISTORY_DIR, exist_ok=True)

@app.route('/history/<history_type>', methods=['GET'])
def get_history(history_type):
    history_file = os.path.join(HISTORY_DIR, f"{history_type}.txt")
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history = f.read()
        return history
    else:
        return 'No history found for this type', 404

@app.route('/history/<history_type>', methods=['DELETE'])
def delete_history(history_type):
    history_file = os.path.join(HISTORY_DIR, f"{history_type}.txt")
    if os.path.exists(history_file):
        os.remove(history_file)
        return 'History deleted successfully'
    else:
        return 'No history found for this type', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10004, debug=False)
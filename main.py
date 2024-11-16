from flask import Flask, request, jsonify, send_from_directory
import os
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

# Unrestricted Resource Consumption
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    # Hier könnte eine enorme Datei ohne Größenlimit hochgeladen werden
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    return jsonify({"message": "File uploaded successfully"}), 200

# Server Side Request Forgery (SSRF)
# Unsafe Consumption of APIs
@app.route('/file', methods=['GET'])
def get_file():
    file_path = request.args.get('path')
    folder_path, filename = os.path.split(file_path)

    if file_path:
        if os.path.exists(file_path):
            # Der Benutzer könnte auf beliebige Dateien zugreifen, wenn keine Validierung stattfindet.
            return send_from_directory(folder_path, filename)
        else:
            return jsonify({"status": "error", "message": "File not found."}), 404
    else:
        return jsonify({"status": "error", "message": "No URL provided."})

# Security Misconfiguration
@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        def get_user_from_database(user_id):
            # Simulated "database" of users
            users = [
                {"id": 1, "username": "alice", "email": "alice@example.com"},
                {"id": 2, "username": "bob", "email": "bob@example.com"},
                {"id": 3, "username": "carol", "email": "carol@example.com"}
            ]
            
            for user in users:
                if user["id"] == int(user_id): 
                    return user
            
            return None

        print("user_id", user_id)
        user = get_user_from_database(user_id)
        print("user", user)
        
        if user is None:
            return jsonify({
                "error": "Not Found",
                "message": "User with provided ID not found. Possible reasons: Invalid ID, the user was deleted, or the user was never registered." # Zu viele Informationen
            }), 404
        
        return jsonify({
            "user_id": user_id,
            "email": user["username"],
        })
    
    # Überflüssige Fehlerdetails und keine Authentifizierung
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500  

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
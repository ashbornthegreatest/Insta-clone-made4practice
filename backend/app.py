from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)

users = {
    "arsh@example.com": "1234"
}

active_tokens = {}

@app.route('/login', methods=['POST'])
def login():
    data = request.json

    # 🔥 LOG EVERYTHING RECEIVED
    print("\n===== NEW LOGIN ATTEMPT =====")
    print("Raw data:", data)

    email = data.get("email")
    password = data.get("password")

    print("Email entered:", email)
    print("Password entered:", password)

    # login logic
    if email in users and users[email] == password:
        token = str(uuid.uuid4())
        active_tokens[token] = email

        print("STATUS: LOGIN SUCCESS ✅")
        print("Generated token:", token)

        return jsonify({
            "success": True,
            "redirect": f"http://localhost:3000/dashboard.html?token={token}"
        })

    else:
        print("STATUS: LOGIN FAILED ❌")
        return jsonify({
            "success": False,
            "redirect": "http://localhost:3000/failed.html"
        })


@app.route('/verify', methods=['GET'])
def verify():
    token = request.args.get("token")

    print("\n===== TOKEN CHECK =====")
    print("Token received:", token)

    if token in active_tokens:
        print("Token valid for:", active_tokens[token])
        return jsonify({"valid": True, "email": active_tokens[token]})
    else:
        print("INVALID TOKEN ❌")
        return jsonify({"valid": False})


if __name__ == "__main__":
    print("🔥 Backend running...")
    app.run(debug=True)
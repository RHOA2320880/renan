from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    login = request.args.get("login")
    senha = request.args.get("senha")
    
    if not login or not senha:
        return jsonify({"erro": "Login e senha são obrigatórios"}), 400
    
    return jsonify({"login": login, "senha": senha})

if __name__ == '__main__':
    app.run(host= '127.0.0.1', port=5000)
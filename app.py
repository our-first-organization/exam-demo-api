from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/is_prime/<int:x>', methods=['GET'])
def is_prime(x):
    if x <= 2:
        return 'false'
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return 'false'
    return 'true'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8081)

# @app.route('/getcode', methods=['GET'])
# def get_code():
#     return "0000"

# @app.route('/plus/<int:a>/<int:b>', methods=['GET'])
# def plus(a, b):
#     return str(a + b), 200

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8081)

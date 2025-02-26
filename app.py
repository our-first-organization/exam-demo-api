from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/cir_sur/<x>', methods=['GET'])
def cir_sur(x:str):
    r = float(x)
    if r <= 0 :
        return "0.00"
    ans = 4*(3.14)*(r*r)
    return str(round(ans,2))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)

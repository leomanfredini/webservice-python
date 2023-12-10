from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Olá, mundo!"


@app.route('/cep/<cep>', methods=['GET'])
def getCep(cep):
    url = "https://viacep.com.br/ws/"+ cep +"/json/";
    response = requests.get(url)
    return response.text

@app.route('/soma', methods=['POST'])
def soma():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    resultado = num1 + num2
    return str(resultado)

if __name__ == '__main__':
    app.run()

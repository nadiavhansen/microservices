from flask import Flask, request
from DataBase.pedidos import Pedidos
import json
import requests

app = Flask(__name__)


@app.route("/listar_pedidos/", methods=["GET"])
def listar_pedidos():
    info = Pedidos().listar_pedidos()
    json = info.to_json(orient="records")

    return json


@app.route("/listar_pedidos_por_usuario/<int:Id_usuario>", methods=["GET"])
def listar_pedidos_por_usuario(Id_usuario):
    info = Pedidos().listar_pedidos_por_usuario(Id_usuario)
    json = info.to_json(orient="records")

    return json


@app.route("/exibir_pedido/<int:id>", methods=["GET"])
def exibir_pedido(id):
    info = Pedidos().exibir_pedido(id)
    json = info.to_json(orient="records")

    return json


@app.route("/criar_pedido/", methods=["POST"])
def criar_pedido():
    dict_values = request.get_json()

    url = f"http://localhost:5001/verificar_existencia_usuario/{dict_values['Id_usuario']}"
    response = requests.get(url)
    print(response.status_code, response.status_code == 400)
    if response.status_code == 400:
        return "Usuário não existe!"
    if dict_values['Quantidade'] <= 0:
        return "Você deve selecionar pelo menos um item!"

    try:
        return Pedidos().criar_pedido(dict_values)

    except Exception as error:
        return str(error.args)


@app.route("/alterar_pedido/<int:id>", methods=["PUT"])
def alterar_pedido(id):
    dict_values = request.get_json()

    if dict_values['Quantidade'] <= 0:
        return "Você deve selecionar pelo menos um item!"

    try:
        return Pedidos().alterar_pedido(dict_values, id)

    except Exception as error:
        return str(error.args)


@app.route("/excluir_pedido/<int:id>", methods=["DELETE"])
def excluir_pedido(id):
    try:
        return Pedidos().excluir_pedido(id)

    except Exception as error:
        return str(error.args)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

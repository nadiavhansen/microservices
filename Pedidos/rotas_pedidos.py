from flask import Flask, request
from Pedidos.DataBase.pedidos import Pedidos
import json

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
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    try:
        Pedidos().criar_pedido(dict_values)
        return "Pedido realizado com sucesso!", 200

    except Exception as error:
        return str(error.args)


@app.route("/alterar_pedido/<int:id>", methods=["PUT"])
def alterar_pedido(id):
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    try:
        Pedidos().alterar_pedido(dict_values, id)
        return "Pedido alterado com sucesso!", 200

    except Exception as error:
        return str(error.args)

if __name__ == "__main__":
    app.run(debug=True)
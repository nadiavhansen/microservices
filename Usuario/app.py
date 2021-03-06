from flask import Flask, request
from DataBase.usuarios import Usuario
import json

app = Flask(__name__)


@app.route("/listar_usuarios/", methods=["GET"])
def listar_usuarios():
    info = Usuario().listar_usuarios()
    json = info.to_json(orient="records")

    return json


@app.route("/exibir_usuario/<Cpf>", methods=["GET"])
def exibir_usuario(Cpf):
    info = Usuario().exibir_usuario(Cpf)
    json = info.to_json(orient="records")

    return json


@app.route("/cadastrar_usuario/", methods=["POST"])
def cadastrar_usuario():
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)
    usuario = Usuario()

    try:
        return usuario.cadastrar_usuario(dict_values)

    except Exception as error:
        return str(error.args)


@app.route("/alterar_cadastro/<Cpf>", methods=["PUT"])
def alterar_cadastro(Cpf):
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    try:
        return Usuario().alterar_usuario(dict_values, Cpf)

    except Exception as error:
        return str(error.args)


@app.route("/deletar_cadastro/<Cpf>", methods=["DELETE"])
def excluir_cadastro(Cpf):
    try:
        return Usuario().excluir_usuario(Cpf)

    except Exception as error:
        return str(error.args)


@app.route("/verificar_existencia_usuario/<int:id>", methods=["GET"])
def verificar_existencia_usuario(id):
    response = Usuario().usuario_existe(id)
    return response[0], response[1]


if __name__ == "__main__":
    app.run(debug=True, port=5001)

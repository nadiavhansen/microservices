from flask import Flask, request
from Usuario.DataBase.usuarios import Usuario
import json

app = Flask(__name__)


@app.route("/listar_usuarios/", methods=["GET"])
def listar_usuarios():
    info = Usuario().listar_usuarios()
    json = info.to_json(orient="records")

    return json


@app.route("/exibir_usuario/<Cpf>", methods=["GET"])
def exibir_usuario(Cpf):
    info = Usuario().exbir_usuario(Cpf)
    json = info.to_json(orient="records")

    return json


@app.route("/cadastrar_usuario/", methods=["POST"])
def cadastrar_usuario():
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    try:
        Usuario().cadastrar_usuario(dict_values)
        return "Usuario cadastrado com sucesso!", 200

    except Exception as error:
        return str(error.args)


@app.route("/alterar_cadastro/<Cpf>", methods=["PUT"])
def alterar_cadastro(Cpf):
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    try:
        Usuario().alterar_usuario(dict_values, Cpf)
        return "Usuario alterado com sucesso!", 200

    except Exception as error:
        return str(error.args)

@app.route("/deletar_cadastro/<Cpf>", methods=["DELETE"])
def excluir_cadastro(Cpf):
    try:
        Usuario().excluir_usuario(Cpf)
        return "Cadastro deletado com sucesso!", 200

    except Exception as error:
        return str(error.args)


if __name__ == "__main__":
    app.run(debug=True)
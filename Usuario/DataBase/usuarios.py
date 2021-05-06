from .db import Mysql
import pandas as pd
from datetime import datetime
from .validacoes import Validacoes


def converter_lista_para_sql_string(data: list) -> str:
    converted_to_sql_data = [f"'{value}'"
                             if isinstance(value, str) and value.upper() != "DEFAULT" and value.upper() != "NULL"
                             else str(value)
                             for value in data]
    string_values = ",".join(converted_to_sql_data)
    return string_values


class Usuario:

    def __init__(self):
        self.db = Mysql()

    def listar_usuarios(self):
        sql = "SELECT * FROM usuarios"
        self.db.cursor.execute(sql)
        colunas = [i[0] for i in self.db.cursor.description]
        data_frame = pd.DataFrame(self.db.cursor.fetchall(), columns=colunas)
        print(data_frame)

        return data_frame

    def exbir_usuario(self, id_usuario):
        sql = f"SELECT * FROM usuarios WHERE id = {id_usuario}"
        self.db.cursor.execute(sql)
        colunas = [i[0] for i in self.db.cursor.description]
        data_frame = pd.DataFrame(self.db.cursor.fetchall(), columns=colunas)


        return data_frame

    def cadastrar_usuario(self, dict_values):
        horario_cadastro = datetime.now()
        list_values = list(dict_values.values())
        sql_values = converter_lista_para_sql_string(list_values)
        sql = f"""INSERT INTO usuarios VALUES (DEFAULT, {sql_values}, '{horario_cadastro}', NULL)"""
        validacoes = Validacoes()
        if not validacoes.validar_cpf(list_values[1]):
            return "CPF inválido!", 400
        if validacoes.validar_cpf_ja_cadastrado(list_values[1]):
            return "CPF já cadastrado!", 400
        if validacoes.validar_email_ja_cadastrado(list_values[2]):
            return "Email já cadastrado!", 400
        else:
            self.db.cursor.execute(sql)
            return "Usuário cadastrado com sucesso!", 200

    def alterar_usuario(self, dict_values, cpf):
        horario_alteracao = datetime.now()
        list_keys, list_values = list(dict_values.keys()), list(dict_values.values())
        sql = f"""UPDATE usuarios SET {list_keys[0]} = '{list_values[0]}',
                                   Cpf = '{cpf}', 
                                   {list_keys[1]} = '{list_values[1]}', 
                                   {list_keys[2]} = '{list_values[2]}', 
                                   Alterado = '{horario_alteracao}' WHERE Cpf = {cpf}"""
        validacoes = Validacoes()
        if validacoes.validar_email_ja_cadastrado(list_values[1]):
            return "Email já cadastrado!", 400
        else:
            self.db.cursor.execute(sql)
            return "Usuário alterado com sucesso", 200

    def excluir_usuario(self, cpf):
        sql = f"""DELETE FROM usuarios WHERE Cpf = {cpf}"""
        self.db.cursor.execute(sql)

    def usuario_existe(self, id_usuario):
        df = self.exbir_usuario(id_usuario)
        if df.empty:
            return "Não existe", 400
        return "Existe", 200

    # import base64
    #
    # def codificar_dado(dado):
    #     ascii_dado = dado.encode('ascii')
    #     dado_codificado_ascii = base64.b64encode(ascii_dado)
    #     dado_codificado = dado_codificado_ascii.decode('ascii')
    #
    #     return dado_codificado
    #
    # def decodificar_dado(dado):
    #     dado_codificado_ascii = dado.encode('ascii')
    #     dado_decodificado_ascii = base64.b64decode(dado_codificado_ascii)
    #     dado_decodificado = dado_decodificado_ascii.decode('ascii')
    #
    #     return dado_decodificado

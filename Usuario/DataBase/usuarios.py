from .db import Mysql
import pandas as pd
from datetime import datetime


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
        # print(sql)
        self.db.cursor.execute(sql)

    def alterar_usuario(self, dict_values, cpf):
        horario_alteracao = datetime.now()
        list_keys, list_values = list(dict_values.keys()), list(dict_values.values())
        sql = f"""UPDATE usuarios SET {list_keys[0]} = '{list_values[0]}',
                                   {list_keys[1]} = '{list_values[1]}', 
                                   {list_keys[2]} = '{list_values[2]}', 
                                   {list_keys[3]} = '{list_values[3]}', 
                                   Alterado = '{horario_alteracao}' WHERE Cpf = {cpf}"""
        self.db.cursor.execute(sql)

    def excluir_usuario(self, cpf):
        sql = f"""DELETE FROM usuarios WHERE Cpf = {cpf}"""
        self.db.cursor.execute(sql)

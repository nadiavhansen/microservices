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


class Pedidos:

    def __init__(self):
        self.db = Mysql()

    def listar_pedidos(self):
        sql = "SELECT * FROM pedidos"
        self.db.cursor.execute(sql)
        colunas = [i[0] for i in self.db.cursor.description]
        data_frame = pd.DataFrame(self.db.cursor.fetchall(), columns=colunas)

        return data_frame

    def listar_pedidos_por_usuario(self, id_usuario):
        sql = f"""SELECT * FROM pedidos WHERE Id_usuario = {id_usuario}"""
        self.db.cursor.execute(sql)
        colunas = [i[0] for i in self.db.cursor.description]
        data_frame = pd.DataFrame(self.db.cursor.fetchall(), columns=colunas)

        return data_frame

    def exibir_pedido(self, id_pedido):
        sql = f"""SELECT * FROM pedidos WHERE id = {id_pedido}"""
        self.db.cursor.execute(sql)
        colunas = [i[0] for i in self.db.cursor.description]
        data_frame = pd.DataFrame(self.db.cursor.fetchall(), columns=colunas)

        return data_frame

    def criar_pedido(self, dict_values):
        horario_criar_pedido = datetime.now()
        lista_values = list(dict_values.values())
        sql_values = converter_lista_para_sql_string(lista_values)
        valor_total = int(lista_values[2]) * float(lista_values[3])
        sql = f"""INSERT INTO pedidos VALUES (DEFAULT, {sql_values}, {valor_total}, '{horario_criar_pedido}', NULL)"""
        self.db.cursor.execute(sql)
        return "Pedido realizado com sucesso!", 200

    def alterar_pedido(self, dict_values, id):
        horario_alterar_pedido = datetime.now()
        lista_values, lista_keys = list(dict_values.values()), list(dict_values.keys())
        valor_total = int(lista_values[2]) * float(lista_values[3])
        sql = f"""UPDATE pedidos SET {lista_keys[1]} = '{lista_values[1]}',
                                     {lista_keys[2]} = '{lista_values[2]}', 
                                     {lista_keys[3]} = '{lista_values[3]}', 
                                     Preço_total = {valor_total}, 
                                     Alterado = '{horario_alterar_pedido}' WHERE id = {id}"""
        self.db.cursor.execute(sql)
        return "Pedido alterado com sucesso!", 200

    def excluir_pedido(self, id_pedido):
        sql = f"""DELETE FROM pedidos WHERE Id = {id_pedido}"""
        self.db.cursor.execute(sql)
        return "Pedido excluido com sucesso!", 200

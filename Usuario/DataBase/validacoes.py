from .db import Mysql

class Validacoes:

    def validar_cpf(self, cpf):
        if len(cpf) == 11:
            return True
        else:
            return False

    def validar_cpf_ja_cadastrado(self, cpf):
        db = Mysql()
        sql = f"SELECT Cpf from usuarios where Cpf = '{cpf}'"
        db.cursor.execute(sql)
        if db.cursor.fetchone():
            return True
        else:
            return False

    def validar_email_ja_cadastrado(self, email):
        db = Mysql()
        sql = f"SELECT Email from usuarios where Email = '{email}'"
        db.cursor.execute(sql)
        if db.cursor.fetchone():
            return True
        else:
            return False


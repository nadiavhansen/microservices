from .db import Mysql

class Validacoes:

    def validar_cpf(self, cpf):
        if len(cpf) == 11:
            return True
        else:
            return False

    def validar_cpf_ja_cadastrado(self, cpf):
        db = Mysql()
        resposta = list(db.cursor.find({"Cpf": cpf}))
        if resposta == []:
            return True
        else:
            return False

    def validar_email_ja_cadastrado(self, email):
        db = Mysql()
        resposta = list(db.cursor.find({"Email": email}))
        if resposta == []:
            return True
        else:
            return False




        # response = list(db.alunos_matricula.find({"Matricula": matricula}))
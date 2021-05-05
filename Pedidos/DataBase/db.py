import MySQLdb

class Mysql:

    def __init__(self):
        self.conn = MySQLdb.connect(host="localhost", user="root", port=3306, db="cadastro_usuarios")
        self.conn.autocommit(True)
        self.cursor = self.conn.cursor()

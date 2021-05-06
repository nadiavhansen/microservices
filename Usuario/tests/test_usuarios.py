from unittest import TestCase, mock
from Usuario.DataBase.usuarios import Usuario, converter_lista_para_sql_string


class TestUsuario(TestCase):

    def test_converter_lista_para_sql_string_works(self):
        lista = ["default", 0, 0.5, "Gustavo", "2021-05-02"]
        resultado = converter_lista_para_sql_string(lista)
        self.assertEqual(resultado, "default,0,0.5,'Gustavo','2021-05-02'")

    @mock.patch("Usuario.DataBase.usuarios.pd")
    @mock.patch("Usuario.DataBase.usuarios.Mysql")
    def test_listar_usuarios_works(self, mock_sql, mock_pd):
        mock_sql().cursor.execute.return_value = None
        mock_sql().cursor.fetchone.return_value = ""
        mock_pd.DataFrame.return_value = ""

        self.assertEqual(Usuario().listar_usuarios(), "")

    @mock.patch("Usuario.DataBase.usuarios.pd")
    @mock.patch("Usuario.DataBase.usuarios.Mysql")
    def test_exbir_usuario_works(self, mock_sql, mock_pd):
        mock_sql().cursor.execute.return_values = None
        mock_sql().cursor.fetchone.return_value = ""
        mock_pd.DataFrame.return_value = ""

        self.assertEqual(Usuario().exbir_usuario(""), "")

    @mock.patch("Usuario.DataBase.usuarios.Validacoes")
    @mock.patch("Usuario.DataBase.usuarios.Mysql")
    @mock.patch("Usuario.DataBase.usuarios.converter_lista_para_sql_string")
    @mock.patch("Usuario.DataBase.usuarios.datetime")
    def test_cadastrar_usuario_works(self, mock_datetime, mock_converter_lista_para_str, mock_sql, mock_validacoes):
        user = Usuario()

        mock_datetime.now().return_value = ""
        mock_converter_lista_para_str.return_value = ""

        mock_validacoes().validar_cpf.return_value = False
        lista = dict(nome="", iad="")
        self.assertEqual(user.cadastrar_usuario(lista), ('CPF inválido!', 400))
        mock_validacoes().validar_cpf.return_value = True

        mock_validacoes().validar_cpf_ja_cadastrado.return_value = True
        lista = dict(nome="", iad="")
        self.assertEqual(user.cadastrar_usuario(lista), ('CPF já cadastrado!', 400))
        mock_validacoes().validar_cpf_ja_cadastrado.return_value = False

        mock_validacoes().validar_email_ja_cadastrado.return_value = True
        lista = dict(nome="", iad="", cpf="")
        self.assertEqual(user.cadastrar_usuario(lista), ('Email já cadastrado!', 400))
        mock_validacoes().validar_email_ja_cadastrado.return_value = False




    def test_alterar_usuario_works(self):
        pass

    def test_excluir_usuario_works(self):
        pass

    def test_usuario_existe_works(self):
        pass
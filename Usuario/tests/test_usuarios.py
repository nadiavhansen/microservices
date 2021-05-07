from unittest import TestCase, mock
from Usuario.DataBase.usuarios import Usuario, converter_lista_para_sql_string
import pandas as pd


class TestUsuario(TestCase):

    def test_converter_lista_para_sql_string_works(self):
        lista = ["default", 0, 0.5, "Gustavo", "2021-05-02"]
        resultado = converter_lista_para_sql_string(lista)
        self.assertEqual(resultado, "default,0,0.5,'Gustavo','2021-05-02'")

    @mock.patch("Usuario.DataBase.usuarios.pd")
    @mock.patch("Usuario.DataBase.usuarios.Mysql")
    def test_listar_usuarios_works(self, mock_sql, mock_pd):
        mock_sql().cursor.execute.return_value = None
        mock_sql().cursor.fetchall.return_value = ""
        mock_pd.DataFrame.return_value = ""

        self.assertEqual(Usuario().listar_usuarios(), "")

        mock_sql().cursor.execute.assert_called_once()
        mock_sql().cursor.fetchall.assert_called_once()
        mock_pd.DataFrame.assert_called_once()

    @mock.patch("Usuario.DataBase.usuarios.pd")
    @mock.patch("Usuario.DataBase.usuarios.Mysql")
    def test_exbir_usuario_works(self, mock_sql, mock_pd):
        mock_sql().cursor.execute.return_values = None
        mock_sql().cursor.fetchall.return_value = ""
        mock_pd.DataFrame.return_value = ""

        self.assertEqual(Usuario().exibir_usuario(""), "")

        mock_sql().cursor.execute.assert_called_once()
        mock_sql().cursor.fetchall.assert_called_once()
        mock_pd.DataFrame.assert_called_once()

    @mock.patch("Usuario.DataBase.usuarios.Validacoes")
    @mock.patch("Usuario.DataBase.usuarios.Mysql")
    @mock.patch("Usuario.DataBase.usuarios.converter_lista_para_sql_string")
    @mock.patch("Usuario.DataBase.usuarios.datetime")
    def test_cadastrar_usuario_works(self, mock_datetime, mock_converter_lista_para_str, mock_sql, mock_validacoes):
        user = Usuario()

        mock_datetime.now.return_value = ""
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

        mock_sql().cursor.execute.return_value = ""
        lista = dict(index1="", index2="", index3="")
        self.assertEqual(user.cadastrar_usuario(lista), ("Usuário cadastrado com sucesso!", 200))

        mock_datetime.now.assert_called()
        mock_converter_lista_para_str.assert_called()
        mock_sql().cursor.execute.assert_called_once()
        mock_validacoes().validar_cpf.assert_called()
        mock_validacoes().validar_cpf_ja_cadastrado.assert_called()
        mock_validacoes().validar_email_ja_cadastrado.assert_called()

    @mock.patch("Usuario.DataBase.usuarios.Mysql")
    @mock.patch("Usuario.DataBase.usuarios.Validacoes")
    @mock.patch("Usuario.DataBase.usuarios.datetime")
    def test_alterar_usuario_works(self, mock_datetime, mock_validacoes, mock_sql):
        user = Usuario()
        mock_datetime.now.return_value = ""

        mock_validacoes().validar_email_ja_cadastrado.return_value = True
        lista = dict(index1="", index2="", index3="")
        self.assertEqual(user.alterar_usuario(lista, ""), ("Email já cadastrado!", 400))
        mock_validacoes().validar_email_ja_cadastrado.return_value = False

        mock_sql().cursor.execute.return_value = ""
        lista = dict(index1="", index2="", index3="")
        self.assertEqual(user.alterar_usuario(lista, ""), ("Usuário alterado com sucesso", 200))

        mock_datetime.now.assert_called()
        mock_sql().cursor.execute.assert_called_once()
        mock_validacoes().validar_email_ja_cadastrado.assert_called()

    @mock.patch("Usuario.DataBase.usuarios.Mysql")
    def test_excluir_usuario_works(self, mock_sql):
        mock_sql().cursor.execute.return_value = ""
        self.assertEqual(Usuario().excluir_usuario(""), ("Cadastro deletado com sucesso!", 200))

        mock_sql().cursor.execute.assert_called_once()

    @mock.patch("Usuario.DataBase.usuarios.Usuario.exibir_usuario")
    def test_usuario_existe_works(self, mock_exibir_usuario):
        user = Usuario()
        mock_exibir_usuario.side_effect = [pd.DataFrame([]), pd.DataFrame([""])]
        self.assertEqual(user.usuario_existe(""), ("Não existe", 400))
        self.assertEqual(user.usuario_existe(""), ("Existe", 200))

        mock_exibir_usuario.assert_called()

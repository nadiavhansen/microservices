from unittest import TestCase, mock
from Usuario.DataBase.validacoes import Validacoes

class TestValidacoes(TestCase):

    def test_validar_cpf_works(self):
        self.assertTrue(Validacoes().validar_cpf("10010010011"))
        self.assertFalse(Validacoes().validar_cpf("100100100"))

    @mock.patch("Usuario.DataBase.validacoes.Mysql")
    def test_validar_cpf_ja_cadastrado_works(self, mock_sql):
        mock_sql().cursor.execute.return_value = None
        mock_sql().cursor.fetchone.side_effect = [True, False]

        self.assertTrue(Validacoes().validar_cpf_ja_cadastrado(""))
        self.assertFalse(Validacoes().validar_cpf_ja_cadastrado(""))

    @mock.patch("Usuario.DataBase.validacoes.Mysql")
    def test_validar_email_ja_cadastrado_works(self, mock_sql):
        mock_sql().cursor.execute.return_value = None
        mock_sql().cursor.fetchone.side_effect = [True, False]

        self.assertTrue(Validacoes().validar_email_ja_cadastrado(""))
        self.assertFalse(Validacoes().validar_email_ja_cadastrado(""))


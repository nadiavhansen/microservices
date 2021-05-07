from unittest import TestCase, mock
from Pedidos.DataBase.pedidos import Pedidos, converter_lista_para_sql_string


class TestPedidos(TestCase):

    def test_converter_lista_para_sql_string_works(self):
        lista = ["index1", "index2", 3]
        resultado = converter_lista_para_sql_string(lista)
        self.assertEqual(converter_lista_para_sql_string(lista), resultado)

    @mock.patch("Pedidos.DataBase.pedidos.pd")
    @mock.patch("Pedidos.DataBase.pedidos.Mysql")
    def test_listar_pedidos_works(self, mock_sql, mock_pd):
        mock_sql().cursor.execute.return_value = None
        mock_sql().cursor.fetchall.return_value = ""
        mock_pd.DataFrame.return_value = ""

        self.assertEqual(Pedidos().listar_pedidos(), "")

        mock_sql().cursor.execute.assert_called_once()
        mock_sql().cursor.fetchall.assert_called_once()
        mock_pd.DataFrame.assert_called_once()

    @mock.patch("Pedidos.DataBase.pedidos.pd")
    @mock.patch("Pedidos.DataBase.pedidos.Mysql")
    def test_listar_pedidos_por_usuario_works(self, mock_sql, mock_pd):
        mock_sql().cursor.execute.return_value = None
        mock_sql().cursor.fetchall.return_value = ""
        mock_pd.DataFrame.return_value = ""

        self.assertEqual(Pedidos().listar_pedidos_por_usuario(""), "")

        mock_sql().cursor.execute.assert_called_once()
        mock_sql().cursor.fetchall.assert_called_once()
        mock_pd.DataFrame.assert_called_once()

    @mock.patch("Pedidos.DataBase.pedidos.pd")
    @mock.patch("Pedidos.DataBase.pedidos.Mysql")
    def test_exibir_pedido_works(self, mock_sql, mock_pd):
        mock_sql().cursor.execute.return_value = None
        mock_sql().cursor.fetchall.return_value = ""
        mock_pd.DataFrame.return_value = ""

        self.assertEqual(Pedidos().exibir_pedido(""), "")

        mock_sql().cursor.execute.assert_called_once()
        mock_sql().cursor.fetchall.assert_called_once()
        mock_pd.DataFrame.assert_called_once()

    @mock.patch("Pedidos.DataBase.pedidos.Mysql")
    @mock.patch("Pedidos.DataBase.pedidos.converter_lista_para_sql_string")
    @mock.patch("Pedidos.DataBase.pedidos.datetime")
    def test_criar_pedido_works(self, mock_datetime, mock_converter, mock_sql):
        mock_datetime.now.return_value = ""
        mock_converter.return_value = ""
        mock_sql.cursor.execute.return_value = ""
        lista = dict(index0="0", index1="0", index2="0", index3="0")
        self.assertEqual(Pedidos().criar_pedido(lista), ("Pedido realizado com sucesso!", 200))

        mock_sql().cursor.execute.assert_called_once()
        mock_datetime.now.assert_called_once()
        mock_converter.assert_called_once()

    @mock.patch("Pedidos.DataBase.pedidos.Mysql")
    @mock.patch("Pedidos.DataBase.pedidos.datetime")
    def test_alterar_pedido_works(self, mock_datetime, mock_sql):
        mock_datetime.now.return_value = ""
        mock_sql().cursor.execute.return_value = ""
        lista = dict(index0="0", index1="0", index2="0", index3="0")
        self.assertEqual(Pedidos().alterar_pedido(lista, ""), ("Pedido alterado com sucesso!", 200))

        mock_sql().cursor.execute.assert_called_once()
        mock_datetime.now.assert_called_once()

    @mock.patch("Pedidos.DataBase.pedidos.Mysql")
    def test_excluir_pedido_works(self, mock_sql):
        mock_sql().cursor.execute.return_value = ""
        self.assertEqual(Pedidos().excluir_pedido(""), ("Pedido excluido com sucesso!", 200))

        mock_sql().cursor.execute.assert_called_once()

import unittest

class TestServidorChat(unittest.TestCase):

    def test_crea_socket(self):
        pass

    def test_conecta(self):
        servidor = ServidorChat()
        servidor.crea_socket()
        cliente = ClienteChat()
        cliente.crea_socket()
        servidor.conecta()
        cliente.conecta()
        self.assertEquals(servidor.recibe(),cliente.recibe())

    def test_recibe(self):
        pass

    def test_enviar(self):
        pass

    def test_desconecta(self):
        pass

    def test_envia(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCliente)
    unittest.TextTestRunner(verbosity=2).run(suite)

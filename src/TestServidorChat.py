import unittest

class TestServidorChat(unittest.TestCase):
    def test_envia(self):
        servidor = ServidorChat()
        servidor.crea_socket()
        cliente = ClienteChat()
        cliente.crea_socket()
        servidor.conecta()
        cliente.conecta()
        self.assertEquals(servidor.recibe(),cliente.recibe())

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCliente)
    unittest.TextTestRunner(verbosity=2).run(suite)

from comandos import Submarino
import unittest


class Test_Submarino(unittest.TestCase):

    def testCoordenada(self):
        sub = Submarino()
        self.assertEqual("2 3 -2 SUL", sub.coordenada("RMMLMMMDDLL"))    #passo os comandos como parametro e ele me retorna a coordenada.

        sub = Submarino()
        self.assertEqual("-1 2 0 NORTE", sub.coordenada("LMRDDMMUU"))    #exemplo de execução do próprio problema #precisa instanciar a classe p/ zerar a posição inicial do submarino

    def testPosInicial(self):
        sub = Submarino()
        self.assertEqual("0 0 0 NORTE", sub.coordenada())      #posição inicial dada pelo problema


    def testPosicionamento(self):  #referente a bussula
        sub = Submarino()
        self.assertEqual(0, sub.apontando_para)
        self.assertEqual(3, sub.left)
        self.assertEqual(0, sub.right)
        self.assertEqual(1, sub.right)
        self.assertEqual(2, sub.right)

    def testProfundidade(self): #cima e baixo
        sub = Submarino()
        self.assertEqual(0, sub.z)
        self.assertEqual(0, sub.up())
        self.assertEqual(-1, sub.down())
        self.assertEqual(-2, sub.down())
        self.assertEqual(-3, sub.down())
        self.assertEqual(-2, sub.up())

    def testMovimentarApontandoParaONorte(self):
        sub = Submarino()
        sub.apontando_para = 0

        sub.movimentar()
        self.assertEqual(0, sub.x)
        self.assertEqual(1, sub.y)

        sub.movimentar()
        self.assertEqual(0, sub.x)
        self.assertEqual(2, sub.y)

        sub.movimentar()
        self.assertEqual(0, sub.x)
        self.assertEqual(3, sub.y)


    def testMovimentarApontandoParaOSul(self):
        sub = Submarino()
        sub.apontando_para = 2

        sub.movimentar()
        self.assertEqual(0, sub.x)
        self.assertEqual(-1, sub.y)

        sub.movimentar()
        self.assertEqual(0, sub.x)
        self.assertEqual(-2, sub.y)

        sub.movimentar()
        self.assertEqual(0, sub.x)
        self.assertEqual(-3, sub.y)


    def testMovimantarApontandoParaOOeste(self):
        sub = Submarino()
        sub.apontando_para = 3

        sub.movimentar()
        self.assertEqual(-1, sub.x)
        self.assertEqual(0, sub.y)

        sub.movimentar()
        self.assertEqual(-2, sub.x)
        self.assertEqual(0, sub.y)
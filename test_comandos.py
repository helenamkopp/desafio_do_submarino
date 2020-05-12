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

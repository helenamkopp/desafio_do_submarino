from comandos import Submarino
import unittest


class Test_Submarino(unittest.TestCase):

    def testCoordenada(self):
        sub = Submarino()
        self.assertEqual("2 3 -2 SUL", sub.coordenada("RMMLMMMDDLL"))    #passo os comandos como parametro e ele me retorna a coordenada.

        #sub = Submarino()
        #self.assertEqual("-1 2 0 NORTE", sub.coordenada("LMRDDMMUU"))    #exemplo de execução do próprio problema #precisa instanciar a classe p/ zerar a posição inicial do submarino

    #def testPosInicial(self):
        #sub = Submarino()
        #self.assertEqual("0 0 0 NORTE", sub.coordenada())      #posição inicial dada pelo problema

    #       NORTE
    #         0
    #
    # OESTE           LESTE
    #   3               1
    #
    #         SUL
    #          2
    # O teste abaixo fala que, quando esta no apontando p/ esta no norte = 0
    # Quando vira uma vez p esquerda, aponta para o 3 = oeste..
    # Assim por diante.


    def testPosicionamento(self):
        sub = Submarino()
        self.assertEqual(0, sub.apontando_para)
        self.assertEqual(3, sub.left)
        self.assertEqual(0, sub.right)
        self.assertEqual(1, sub.right)
        self.assertEqual(2, sub.right)

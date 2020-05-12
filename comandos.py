#Projeto principal
class Submarino(object):

    def __init__(self):
    #0 norte, 1 leste, 2 sul, 3 oeste
        self.apontando_para = 0
        self.z = 0
        self.x = 0
        self.y = 0

    def coordenada(self, comando=""):
        for c in comando:
            if c == "R":
                self.right()
            elif c == "L":
                self.left()
            elif c == "U":
                self.up()
            elif c == "D":
                self.down()
            elif c == "M":
                self.movimentar()

        direcao = ["NORTE", "LESTE", "SUL", "OESTE"][self.apontando_para]
        return  "%s %s %s %s" % (self.x, self.y, self.z, direcao)

    def movimentar(self):
        if self.apontando_para == 0: #norte
            self.y += 1
        if self.apontando_para == 2: #sul
            self.y -= 1
        if self.apontando_para == 1: #leste
            self.x += 1
        if self.apontando_para == 3: #oeste
            self.x -= 1

        return True

    def right(self):
        self.apontando_para = 0 if self.apontando_para == 3 else self.apontando_para + 1
        return self.apontando_para

    def left(self):
        self.apontando_para = 3 if self.apontando_para == 0 else self.apontando_para - 1
        return self.apontando_para

    def down(self):
        self.z = self.z -1
        return self.z

    def up(self):
        self.z = 0 if self.z == 0 else self.z + 1
        return self.z



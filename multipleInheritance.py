class Mario():
    def move(self):
        print("I am moving")

class Shroom():
    def eat_shroom(self):
        print("Nnow I am big")


class BigMario(Mario, Shroom):
    pass #When we need a line and do not want to print anything, Same as Null in Kiushal's Language

bm = BigMario()
bm.move()
bm.eat_shroom()



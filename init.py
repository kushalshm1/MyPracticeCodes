class Tuna:

    def __init__(self): # To do initially
        print("Test Text")

    def swim(self):
        print("I am swimming")

flipper = Tuna() # Flipper is an abject and we associated it with class Tuna
flipper.swim() # Nnow this object will use swim function

# We are making an computer game and we are building Ene,ies
class Enemy:
    def __init__(self, x):
        self.energy = x
    def get_energy(self):
        print(self.energy)

jason = Enemy(5) # We created a new enemy and gave him energy 5 using the function
sandy = Enemy(20) # sandy has got more energy than jason

jason.get_energy()
sandy.get_energy()


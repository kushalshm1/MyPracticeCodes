# very important to object oriented programming

# Real life: Like we inherit traits from our parents and ancestors
# Inheritance basically means getting something from someone

class Parent():
    def print_last_name(self):
        print("Sharma")

class Child(Parent): #Here in the () you can type the  name of a class to inherit features from
    def print_first_name(self):
        print("Kushal")
    def print_last_name(self):
        print("Programmer")

kushal = Child()
kushal.print_first_name()
kushal.print_last_name()


#Class Variable
class Girl:

    gender = "female" # This is class variable

    def __init__(self, name):
        self.name = name  #Instance Variable

r = Girl('Rachel')
s = Girl('Stanky')
print(r.gender)
print(s.gender)


# Class variable is default
# Instance vairable is unique to that specific object/instance
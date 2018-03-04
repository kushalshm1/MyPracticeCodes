# What a thread is? and why thery are useful

# Bilding a program is to give your computer a set of instructions, Right?

# Sometimes its useful to breakup a single program and to do multiple things same time
# For example when we are making a programme of messenger
# We will have to use two functions 1. Sending, 2. Recieving
# and the both the functions should execute at same time so we will require threads


import threading

class KushalsMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = KushalsMessenger(name ='Send out Messages')
y = KushalsMessenger(name ='Recieve Messages')
x.start() # Whenever you call start function it goes to that class and hunts for run function
y.start()
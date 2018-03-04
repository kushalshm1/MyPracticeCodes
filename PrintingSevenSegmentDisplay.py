import os
import time
WIDTH = 79
printedMessage = ["","","","","","",""]
message = "kushal".upper()
characters = {
               "K": ["*    *",
                   "*   *",
                   "*  *",
                   "* *",
                   "* *",
                   "*  *",
                   "*   *"],

               "U": ["*   *",
                   "*   *",
                   "*   *",
                   "*   *",
                   "*   *",
                   "*   *",
                   "*****"],
               "S": ["*****",
                   "*",
                   "*",
                   "*****",
                   "    *",
                   "    *",
                   "*****"],

               "H": ["*    *",
                   "*    *",
                   "*    *",
                   "******",
                   "*    *",
                   "*    *",
                   "*    *"],

               "A": ["******",
                   "*    *",
                   "*    *",
                   "*    *",
                   "******",
                   "*    *",
                   "*    *"],

               "L": ["*     ",
                   "*     ",
                   "*     ",
                   "*     ",
                   "*     ",
                   "*     ",
                   "******"],

}

for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + "  ")

offset = WIDTH

while True:
    os.system("cls")
    #print each line of the message, including the offset.
    for row in range(7):
        print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])
    #move the message a little to the left.
    offset -=1
    #if the entire message has moved 'through' the display then
    #start again from the right hand side.
    if offset <= ((len(message)+2)*6) * -1:
        offset = WIDTH
    #take out or change this line to speed up / slow down the display
    time.sleep(0.05)
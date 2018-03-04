#Creadting and writing a file
fw = open('sample.txt', 'w')
fw.write('This file is created using a python script, Sounds Amazing. Right?\n')
fw.write('I like Bacon\n')
fw.close()

#Reading a file
fr = open('sample.txt','r')
text = fr.read()
print(text)
fr.close()
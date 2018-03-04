text = 'Sample Text to Save\n New Line!'
saveFile = open('exampleFile.txt','w')
saveFile.write(text)
saveFile.close()

#Appending to a file
appendMe = '\nNew bit of information'

appendFile = open('exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()



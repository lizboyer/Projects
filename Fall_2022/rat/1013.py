import numpy as np

raction = input("The rat goes like this, that, or this for a while? \n")

if raction == 'this':
    f = open('rat1.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()

if raction == 'that':
    f = open('rat2.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()

if raction == 'this for a while':
    f = open('rat3.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()
#Importing from sys, taking argv
from sys import argv

#seting up file name, which will turn to be ex15_sample.txt
#when we run the script we need to enter: python ex15.py ex15_sample.txt 
script, filename = argv

#opens the file we gave
txt = open(filename)

#this line prints the test form our file
print(f"Here`s your file {filename}:")
print(txt.read())

# thisl ine will print the file again
print("Type the filename again: ")
#You will need to write everything: ex15_sample.txt !!!
file_again = input(">")

#this line opens the file, so that we can see it
txt_again = open(file_again)

#this line prints tie file
print(txt_again.read())
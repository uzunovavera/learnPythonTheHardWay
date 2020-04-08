from sys import argv
#read the WYSS section for how to run this
script, first, second, third = argv

age = input("What is your age?")

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# To execute this you need to open CMD from the folder with the scripts and write:
# python ex13.py one_thing another_thing the last_thing
# You will get result:
# The script is called: ex13.py
# Your first variable is: 1thing
# Your second variable is: 2things
# Your third variable is: 3things

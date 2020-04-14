def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that`s enough for a party!")
	print("Get a blanket. \n")

print("We can just give the function numbers derectly: ")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too: ")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math: ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# this here will be my improvisation of a function, here we go:
def cats_that_jump(cats_count, jump_counts):
	print(f"You have {cats_count} number of cats!")
	print(f"you have {jump_counts} jups of cats!")
	print("Get those cats down!")

#first way of runing the function
print("Here we will give the cats and jumps values: ")
cats_that_jump(5, 20)

#second way
amount_of_cats = 5
amount_of_jumps = 15

cats_that_jump(amount_of_cats, amount_of_jumps)

#third way
print("Lets calculate these things: ")
cats_that_jump(2 + 5, 7 * 7)

#forth way
print("Lets combine two ways: ")
cats_that_jump(amount_of_cats + 10, amount_of_jumps + 2)

#fifth way
cats_count = 6
print("Lets combine all the cats: ", amount_of_cats + cats_count)

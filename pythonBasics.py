# #------------------------Variables: 
# name, lastName, age = 'John', 'Davidson', 23
# print(name, lastName, age)

# #------------------------concatenation
# criminal = 'John'
# crime = 'murder'
# print(f"{name} has committed the crime of {crime}.")

# #------------------------Conditionals 
# print("Can you play this game? Enter you age to see")
# age = int(input())
# if age < 18 and age > 0:
#     print("No, You can't play this game")
# elif age == 18:
#     print('You can just play the game!')
# elif age > 100 or age < 0:
#     print(f'Seriously? you are {age} years old?! STOP KIDDING!!') 
# else: 
#     print("Yes, you are old enough to play the game.")

# #------------------------for_in loop
# names = ['Jack', 'David', 'Ahmad', 'Singh', 'Jamal', 'George']
# for name in names: 
#     print(f"{names.index(name) + 1}. {name}")

# #------------------------while loop
# msg = input("what is password? ")
# while msg != "bananas":
#     print("WRONG!")
#     msg = input("what is password? ")
# print("correct!")

# #------------------------lists
# names = ['Jack', 'David', 'Ahmad', 'Singh', 'Jamal', 'George']
# print(names[len(names) - 1])

# #------------------------Dictionary
# person = {
#     "name": "Colt",
#     "children": ['John', 'George', 'Jenny'],
#     "age": 35
# }
# #another way to make dictionary
# person2 = dict(
#     name = "John",
#     family = ['David', 'John'],
#     age = 12
#     )
# print(person2["age"])

# #------------------------Functions
# def addition(x,y = 10): 
#     return x + y
# print(addition(10))      
 
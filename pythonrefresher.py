age = 22
name = 'Pratap'

isTodayCold = True

# Print name and age and string interpolation
# print("Hello my name is {} and I am {} years old".format(name,age))

""" 

This multi line comment. 

"""

# this is single line comment. 

# if age != 14:
#     print("You are older than 18")
#     print("This is another line")
# else:
#     print("you are younger than 18")



def hello(name, age=0):
    return "Hello {} you are {} years old".format(name, age)


sentence = hello("Mark", 15)
print(sentence)

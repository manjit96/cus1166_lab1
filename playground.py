print("PRACTICING BASIC PROGRAM")

print("Hello World") # Display a message
# Get user input and display a message.
myname = input("What is your name: ")
print("Hello " + str(myname))
# Alternative way to format a string
print("Hello %s" % myname)

print("DONE PRACTICING BASIC PROGRAM")



print("\nPRACTICING VARIABLES")

i = 20
f = 1.14159
b = True
n = None

print(f"Variable i has the value {i}")
print(f"Variable f has the value {f} and its type is {type(f)}")
print(f"Variable b has the value {b}")

#tuple
c = (5,10,15)
print(f" c[0] has the value {c[0]} and is of type: {type(c)}")

#list
names = ["Jon", "Sansa", "Bran"]
names = [10,20,30]
print(f" names[0] has the value {names[0]} and is of type: {type(names)}")

#sets variables
s = set()
s.add(1)
s.add(4)
s.add(6)
print(s)

#dictionary
grades = {"Jon" : "A", "Sansa": "B"}
grades["Jon"]
grades["Bran"] = "C-"

#create an empty directory
mydictionary = dict()

print("DONE PRACTICING VARIABLES")



print("\nPRACTICING CONDITIONALS")

number = input("Enter a number: ")
if (int(number) > 0):
    print("The value entered is positive, meaning greater than 0")
elif (int(number) < 0):
    print("The value entered is negative, meaning less than 0")
else:
    print("The value entered is equal to zero")

print("Done Practicing Conditionals")



print("\nPracticing Loops")

for i in range(5):
    print(i)

for i_idx, i_value in enumerate(range(2,10)):
    print(f"{i_idx} - {i_value}")

print("Done Practicing Loops")



print("\nPracticing Functions")

def is_odd(value):
    value = input("Enter a value: ")
    if (value % 2) != 0:
        print("The number is odd")
    else:
        print("The number is even")

print("Done Practicing Functions")



print("\nPracticing Classes")

class Book:
    def __init__(self, title = "Software Engineering", isbn = ""):
        self.title = title
        self.isbn = isbn

    def printBook(self):
        print(self.title + "," +self.isbn)

print("Done Practicing Classes")



print("PRACTICING BASIC PROGRAM")

print("Hello World") # Display a message
# Get user input and display a message.
myname = input("What is your name: ")
print("Hello " + str(myname))
# Alternative way to format a string
print("Hello %s" % myname)

print("DONE PRACTICING BASIC PROGRAM\n")



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
print(f"c[0] has the value {c[0]} and is of type: {type(c)}")

#list
names = ["Jon", "Sansa", "Bran"]
names = [10,20,30]
print(f"names[0] has the value {names[0]} and is of type: {type(names)}")

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

print("DONE PRACTICING VARIABLES\n")



print("\nPRACTICING CONDITIONALS")

number = input("Enter a number: ")
if (int(number) > 0):
    print("The value entered is positive, meaning greater than 0")
elif (int(number) < 0):
    print("The value entered is negative, meaning less than 0")
else:
    print("The value entered is equal to zero")

print("DONE PRACTICING CONDITIONALS\n")



print("\nPRACTICING LOOPS")

books = ["Hunger Games", "Harry Potter", "Twilight"]
for i in books:
    print(i)

print("DONE PRACTICING LOOPS\n")


print("\nPRACTICING FUNCTIONS")


def is_odd():
    value = input("Enter a value: ")
    if (int(value) % 2) != 0:
        print("The number is odd")
    else:
        print("The number is even")


print(is_odd())

print("DONE PRACTICING FUNCTIONS\n")



print("\nPRACTICING CLASSES")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(val):
        print(f"My name is {val.name} and I am {val.age} years old.")


p1 = Person("Merry", 22)
p1.info()

print("DONE PRACTICING CLASSES")



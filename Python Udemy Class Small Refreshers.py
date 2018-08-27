#misc Python notes from Udemy class
#easy stuff here, tips and tricks
#little things your Tri C class didn't cover

#string formatting
name = "Gabrielle"
print("Hello, {}.".format(name))
age = 88
print("Hello, {}. You are {}.".format(name, age))

print("Hello, {name}. You are {age}.")
#alas, no string interpolation (yet?)

print(name.upper()) #GABRIELLE  name.lower

sentence = "It is a very good day."
print(sentence.replace("good", "great")) #prints great instead

print(sentence[8:12]) #very  this is a slice
print(len(sentence))  #22


#lists. a container that stores objects.
classRoster = ["Sue", "Bob", "Rachel", "Gregg"]
print(classRoster)
print(classRoster[2]) #Rachel
classRoster.insert(2, "Jeff")
print(classRoster)
classRoster.remove("Bob")
print(classRoster)

#others: sort, reverse, pop(returns last element in list and removes it)


#tuples. like a list, but cannot be modified. good for data that won't change.
startDates = (1870, 1905, 1914, 1939)
print(startDates)
#startDates[1] = 1902  THIS WILL GIVE AN ERROR.
#the only way to "change" a tuple: "del"  del(startDates)


#dictionaries. collection of key/value pairs.
warNames = {"WWI": 1914, "WWII": 1939, "Korea": 1951}
print(warNames)
print(warNames["WWII"])  #1939

#update value:
warNames["Korea"] = 1950
print(warNames["Korea"])  #1950

print(warNames.keys())
print(warNames.values())

#copy:
copyOfWarNames = warNames.copy()
del warNames["Korea"]
#warNames.clear  ERASES THE WHOLE DIC


#conditional statement syntax (in addition to ==. see below.).  Madness!
fruit = "apple"
if fruit is "apple" or fruit is "orange":
    print("yummy!")


#you can run python programs from the command terminal by going to the folder then
# "py name-of-program.py"

print("Enter a number:")
number = int(input())
if number % 3 is 0:
    print("Your number is a multiple of 3.")
    if number % 7 == 0:
        print("and a multiple of 7.")
    else:
        print("but not 7.")

#two ways of for looping:
for student in classRoster:
    print(student)

for digit in range(5,13):
    print(digit) #prints 5-12

start = 3
stop = 10
for digit in range(start, stop):
    print(digit) #prints 3-9
    
#simple loop and nested if/else
collectionOfBooks = ["Dune", "Neuromancer", "Rebecca"]
print("Enter the name of the book:")
bookToBeChecked = input()
for book in collectionOfBooks:
    if book == bookToBeChecked:
        print("Yes I have that book.")
        break
else:
    print("I do not have that book.")
#careful about putting that else statement outside the for loop
#otherwise the else will print multiple times if you don't have the book
#or if it's not the first book



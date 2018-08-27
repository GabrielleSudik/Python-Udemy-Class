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


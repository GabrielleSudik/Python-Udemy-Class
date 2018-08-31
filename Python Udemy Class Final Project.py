#Udemy Python Class Challenge
#3+ students in a class
#Rank the top three
#Give $500 to first place, $300 then $100
#Congrats to everyone who scored over 950 in the class
#Tips: students in dictionary with total amounts and sort
#Rewards in tuple
#Condition checks for students meeting standards

print("Hello, teacher. Here is a report of your students and their rewards.")

#made-up grade totals for each student. dictionary.
studentGrades = {"Gregg": 1050, "Rachel": 980, "Jeff": 955, "Merry": 1200,
                 "Chris": 600, "Ellen": 990, "Michael": 880}
#tuple for unchanging rewards
cashRewards = (500, 300, 100)

#confirm it's correct
print(studentGrades)
print(cashRewards)

#sort them by value, then reverse results
studentGrades = sorted(studentGrades.values(), reverse=True)

#confirm that worked
print(studentGrades)

for value in studentGrades.items():
    if value >= 950:
        print("Good job, {}. You did well!", studentGrades.keys)
    else:
        print("You need to improve, {}", studentGrades.keys)



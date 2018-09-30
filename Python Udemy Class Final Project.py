#Udemy Python Class Challenge
#3+ students in a class
#Rank the top three
#Give $500 to first place, $300 then $100
#Congrats to everyone who scored over 950 in the class
#Tips: students in dictionary with total amounts and sort
#Rewards in tuple
#Condition checks for students meeting standards

import operator #per google search

print("Hello, teacher. Let's figure out your students' rewards.")
print()

def readStudentDetails():
    #made up grades: {"Gregg": 1050, "Rachel": 980, "Jeff": 955, "Merry": 1200,
                 #"Chris": 600, "Ellen": 990, "Michael": 880}
    print("Enter the number of students: ")
    numberOfStudents = int(input())
    studentRecord = {} #the dictionary of student marks
    for student in range(0, numberOfStudents):
        print("Enter the name of the student: ")
        name = input()
        print("Enter the final score of the student: ")
        marks = int(input())
        studentRecord[name] = marks
        print()
    return studentRecord

def rankStudents(studentRecord):
    #you can't sort a dictionary for some reason.
    #so convert the dictionary into something else. a tuple.
    #solution with help from google search:
    try:
        sortedStudentRecord = sorted(studentRecord.items(),
                                     key = operator.itemgetter(1), reverse = True)
        print(sortedStudentRecord)
        print("{} is ranked first, with a grade of {}".format
              (sortedStudentRecord[0][0], sortedStudentRecord[0][1]))
        print("{} is ranked second, with a grade of {}".format
              (sortedStudentRecord[1][0], sortedStudentRecord[1][1]))
        print("{} is ranked third, with a grade of {}".format
              (sortedStudentRecord[2][0], sortedStudentRecord[2][1]))
        #those each are first the index position of the pair,
        #then the index position of the name and grade (ie, name always 0, grade always 1)
        print()
        return sortedStudentRecord
    except IndexError:
        print("Please enter at least 3 students on your next try.")
        quit()
    
def rewardStudents(sortedStudentRecord, reward):
    print("{} has received a cash reward of ${}".format
          (sortedStudentRecord[0][0], reward[0]))
    print("{} has received a cash reward of ${}".format
          (sortedStudentRecord[1][0], reward[1]))
    print("{} has received a cash reward of ${}".format
          (sortedStudentRecord[2][0], reward[2]))
    print()

def congratStudents(sortedStudentRecord):
    for record in sortedStudentRecord:
        if record[1] >= 950:
            print("Congrats on scoring a grade of {}, {}.".format
                  (record[1], record[0]))
        else:
            break
    print()
    
#create the whole list of students and their grades by calling readStudentDetails
studentRecord = readStudentDetails()
#create a ranked list of students by passing the whole list to the rankStudents function
sortedStudentRecord = rankStudents(studentRecord)
#create a tuple for the rewards (tuples cannot be changed)
reward = (500, 300, 100)
#pass both sorted list of students and reward info to rewardStudents function
rewardStudents(sortedStudentRecord, reward)
#now let's congrat the students
congratStudents(sortedStudentRecord)



import time
import datetime


# #creating an intrusion detection system detection system
# class Person:
#     def __init__(self,name,occupation):
#         self.name = name
#         self.occupation = name
#     def detect(self):
#         ID = self.name
#         job = self.occupation
#         return detect

# name = input("Enter your name: ")
# occupation = input("Enter your occupation: ")


# #initialize
# person = Person(name, occupation)

# #date/time
# current_datetime = datetime.datetime.now()


# #check if person is intruder
# intruder = "unknown"
# if person.name == intruder:
#     print("Warning!!!!An intuder is detected at:",current_datetime)
# else:
#     print("Welcome,",person.name,"(",person.occupation,")")
#     print("Logged in at:",current_datetime)
    

import datetime

# Creating an intrusion detection system
class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

# Prompt user to enter name and occupation
name = input("Enter your name: ")
occupation = input("Enter your occupation: ")

# Initialize person
person = Person(name, occupation)

# Get current date and time
current_datetime = datetime.datetime.now()

# Define intruder details
intruder_name = "Unknown"  # Default name for intruders
intruder_occupation = "Unknown"  # Default occupation for intruders

# Check if the person is an intruder
if person.name == intruder_name and person.occupation == intruder_occupation:
    print("Warning! Intruder detected at", current_datetime)
else:
    print("Welcome,", person.name, "(", person.occupation, ")")
    print("Logged in at", current_datetime)


    
# Task 1: Advanced Data Extraction

import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York" # provided text

def extractName(text):
    return re.findall(r"(?<=Name: )\w+", text) # Regex to check for 'Name' in input

def extractAge(text):
    return re.findall(r"(?<=Age: )\d+", text) # Regex to check for 'Age' in input

def extractOccupation(text):
    return re.findall(r"(?<=Occupation: )\w+" , text) # Regex to check for 'Occupation' in input

def extractLocation(text):
    return re.findall(r"(?<=Location: )\w+", text) # Regex to check for 'Location' in input

print(extractName(text))
print(extractAge(text))
print(extractOccupation(text))
print(extractLocation(text))
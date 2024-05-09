# Task 1: Code Correction

import re

text = "Contact emails are: johndoe@example.com and jane.doe@example.com"
# emails = re.findall(r"[A-Z0-9._%+0]+@[A-Z0-9.-]+\.[A-Z]{2,}", text) # original code

emails = re.findall(r"[A-Za-z0-9._%+0]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text) # added 'a-z' in the regular expression to detect lowercase characters
print(emails)
# Task 1: Email Extraction Enhancement

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com, exclude@gmail.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude.com)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text) # added '(?!exclude.com) after the @ to exclude that domain

"""
for email in emails: # A for loop can also be use to remove specfic email domains
    if "exclude.com" in email:
        emails.remove(email)
"""
print(emails) # print emails detected
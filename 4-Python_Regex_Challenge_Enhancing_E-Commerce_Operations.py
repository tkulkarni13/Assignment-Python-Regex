# Task 1: Product Description Keyword Tagging

import re

descriptions = [ # Given product descriptions
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

keywords = { # keywords to look for when identifying a product tag or category
            "Electronics": ["tv", "screen", "phone", "gb", "laptop", "headphones", "cable"],
            "Apparel": ["small", "medium", "large", "shirt", "pant", "cotton", "nylon"],
            "Home & Kitchen": ["knife", "spoon", "fork", "stainless steel", "cast iron", "pan", "pot", "ladle", "kitchen"]
            }

def convertPrice(price): # convert '$' to 'USD' for standardized prices
    return re.sub(r"\$", "USD ", price)

def tagProduct(description): # given a product description, this will output a relevant product tag
    for k, v in keywords.items():
        count = 0
        for word in v:
            if word in description.lower(): # make sure to convert description to lowercase for easier comparison
                count += 1
            if (count > 2): # Check if the the description matches at least two keywords before matching a tag to it
                return (k)

# Testing
print(convertPrice("$10.99"))
print(convertPrice("This phone starts at a price of $999.99, but if you want more storage, it will be more expensive."))
for d in descriptions:
    print(tagProduct(d))
"""
 * Copyright (C) Mathstronauts. All rights reserved.
 * This information is confidential and proprietary to Mathstronauts and may not be used, modified, copied or distributed.
"""

# Favourite Animal Dictionary

# Poll the class for their favourite animal, ask for some options in the chat
# OR poll for the following examples: cat, dog, horse

# sample of poll results:
#   cat: 4
#   dog: 6
#   horse: 2

# create dictionary
dict = {
    "cat": 4,
    "dog": 6,
    "horse": 2,
    }

print(dict)  # print the entire dictionary
print(len(dict))  # length is the number of items in the dictionary

# accessing dictionary items
options = dict.keys()
cat_vote = dict["cat"]
votes = dict["cat"] + dict["dog"] + dict["horse"]

print("Options:", options)
print("Cat Votes:", cat_vote)
print("Total Votes:", votes)

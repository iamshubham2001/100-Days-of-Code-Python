"""
Write a python program to translate a message into secret code language.
Use the rules below to translate normal english into secret code language.
"""

# Coding
'''
if:
    the words contains atleast 3 characters, remove the first letter and append it at the end.
    now append three randomcharacters at the starting and the end
else:
    simply reverse the string
'''

# Decoding
'''
if:
    the word contain less than 3 characters, reverse it
else:
    remove 3 random characters from start and end.
    Now remove the last letter and the beginning
'''

# your program should ank whether you want to code or decode


'''
    Author : Sanjay Sukhwani
    Purpose : Filter Function
    Date : 2022-07-22 
    Time : 16:45:57 
'''

# The filter() method filters the given sequence with the help of a function
# Function will tests each element in the sequence to be true or not.
# Syntax : 
#   filter(<function>,<sequence>)

# function that filters vowels
def isVowel(ch):
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        return True
    else:
        return False

# sequence
characterSequence = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','x','c','v','b','n','m']
sent = "Hello World"

print(chr(97))
print(ord('a'))

# using filter function
vowelCharacters = filter(isVowel, characterSequence)
  
print('The Vowels in Squence are : ')
for s in vowelCharacters:
    print(s)
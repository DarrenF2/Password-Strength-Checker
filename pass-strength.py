import numbers
import string
import random

with open ('passphrases.txt','r') as f:
    lines = [line.strip() for line in f]

password = (random.choice(lines))
upper_case = [any([ 1 if c in string.ascii_uppercase else 0 for c in password])]
lower_case = [any([ 1 if c in string.ascii_lowercase else 0 for c in password])]
special_characters = [any([ 1 if c in string.punctuation else 0 for c in password])]
number_characters = [any([ 1 if c in string.digits else 0 for c in password])]



length = len(password)


score = 0 

if length > 5:
    score += 1
if length > 12:
    score =+ 10

if upper_case == True:
    score += 2
if lower_case == True:
    score += 2
if special_characters == True:
    score += 2
if number_characters == True:
    score += 2

if score < 6:
    print("weak_pasword")

if score > 6:
    print("medium_pasword")   

if score > 8:
    print("strong_pasword")             



#print(upper_case)
#print(lower_case)
#print(special_characters)
#print(number_characters)
print(password)
print (score)
#print(lines)
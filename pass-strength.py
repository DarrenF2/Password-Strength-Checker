import numbers
import string
import random

with open ('passphrases.txt','r') as f:
    lines = [line.strip() for line in f]

password = (random.choice(lines))
upper_case = any([ 1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([ 1 if c in string.ascii_lowercase else 0 for c in password])
special_characters = any([ 1 if c in string.punctuation else 0 for c in password])
number_characters = any([ 1 if c in string.digits else 0 for c in password])

items = [upper_case, lower_case, special_characters, number_characters]

score = 0

if upper_case == True:
    score += 2
if lower_case == True:
    score += 2
if special_characters == True:
    score += 4
if number_characters == True:
    score += 2

length = len(password)


if length == 1:
    score += 1
if length > 6:
    score += 4
if length > 12:
    score =+ 10

if sum(items) > 1:
    score += 1
if sum(items) >= 2:
    score += 2
if sum(items) > 3:
    score += 3


if score == 0 or score <= 5:
    print("weak password")

if score <= 7:
    print("medium password")   

if score > 8:
    print("strong password")             




print(password)
print (score)
#print(lines)
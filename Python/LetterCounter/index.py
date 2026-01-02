import os
import sys

# Add the parent directory + libs to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "libs"))

from percentagise import *


usrput = input("put: ")

usrputty = list(usrput)

lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")
numbers = list("1234567890")

letters = 0
nums = 0
chars = 0

lis = []

for i in range(0, len(usrputty)):
    if usrputty[i].lower() in lowercase_letters:
        letters += 1
    elif usrputty[i].lower() in numbers:
        nums += 1
    else:
        chars += 1

lis.append(letters)
lis.append(nums)
lis.append(chars)

print(percentagise(lis, 0))
print(percentagise(lis, 1))
print(percentagise(lis, 2))

#Write a Python program to count the number of characters (character frequency) in a string.
from collections import Counter
test_str = input("Enter a string: \n")
result = Counter(test_str)
print ("Character frequency in the string : \n"+  str(result))
#Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
from itertools import permutations
perms=["".join(p) for p in permutations("aeiou")]
print(perms)
print(len(perms))
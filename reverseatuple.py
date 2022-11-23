#Write a Python program to reverse a tuple.

x = ("apple", "banana", "cherry")
y = list(x)
y.reverse()
x = tuple(y)
print(x)

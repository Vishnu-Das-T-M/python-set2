#Write a password generator in Python.
#Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
import random
import string
print("welcome to password generator")
length=int(input("Enter the length of password:"))
lower=string.ascii_lowercase
upper=string.ascii_uppercase
number=string.digits
symbols=string.punctuation
all=lower+upper+number+symbols
password="".join(random.sample(all,length))
print("Your password is:",password)
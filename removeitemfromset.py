#Write a Python program to remove an item from a set if it is present in the set.

languages={'python','javascript','java'}
if 'java' in languages:
    languages.remove('java')
print(languages)
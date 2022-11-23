#Write a python program to count repeated characters in a string.
from collections import defaultdict
string=input("Enter a string:")
d = defaultdict(int)
for i in string:
    d[i] += 1

for i in sorted(d, key=d.get, reverse=True):
  if d[i] > 1:
      print('%s %d' % (i, d[i]))


#Write a Python program to sort a dictionary by key.
#color_dict = {'red':'#FF0000',
#'green':'#008000',
#'black':'#000000',
#'white':'#FFFFFF'}
from collections import OrderedDict
color_dict = {'red':'#FF0000','green':'#008000','black':'#000000','white':'#FFFFFF'}
ordered_dict=OrderedDict(sorted(color_dict.items()))
print(ordered_dict)
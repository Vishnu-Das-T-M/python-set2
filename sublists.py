#Write a Python program to generate all sublists of a list.


def sub_lists (my_list):
    sub = [[]]
    for i in range(len(my_list) + 1):
        for j in range(i):
            sub.append(my_list[j: i])
    return sub
 
my_list = ['A','B','C']
print(sub_lists(my_list))
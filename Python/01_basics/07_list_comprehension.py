
# list comprehensiona is a shorthand to create a list based on values of existing list

# Syntax:
# newlist = [expression for item in iterable if condition == True]

my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_list = [ele for ele in my_list if ele % 2 == 0] # This will create a list with all the even values in it.
print(even_list)

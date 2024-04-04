

# Cretaing array using array module
from array import array

my_arr = array('i', [1,2,3,4])
print(my_arr)


# creting array using numpy
from numpy import array
my_arr1 = array([1,2,3,4])
print(my_arr1)

# Creating array using list
my_arr2 = [1,2,3,4]
print(my_arr2)

#Accessing array elements
print(my_arr2[2])

# Array methods
my_arr2.append(4)  # Adds element at the end
print(my_arr2)

print(my_arr2.count(4)) # counts the occurrence of the element

my_arr2.pop(2) # removes the element at the index specified else removes last element
print(my_arr2)

my_arr2.remove(2) # removes the first occurence of the element given
print(my_arr2)
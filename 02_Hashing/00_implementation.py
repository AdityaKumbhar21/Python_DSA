# Hashmap is a DS which can store elements in Key -> value pair

#   01 -> "Aditya"  : Here 01 is the key and "Aditya is value"


#Implementing Hashmap in Python

hash_map = {}  # Dict is hashmap in python

hash_map[1] = "Aditya"
hash_map[2] = "Jay"
hash_map[3] = "Sid"

print(hash_map)
print(hash_map[1])  # will print the value with key 1


# to delete an element from hm
hash_map.pop(3) # the element with key 3 will be deleted
print(hash_map)

# The elements can be anything in HashMap

hash_map2 = {
    "Name": "Aditya",
    "isAdult": True,
    "fav_colors":["red","blue"],
    "roll_no": 8
}

print(hash_map2)

# we can delete element from hashmap using del keyword also
del hash_map2["isAdult"]

print(hash_map2)

#inserting array in hashmap

my_arr = [1,2,3,4,5]

hm = {}

for i in range(0,len(my_arr)):
    hm[i] = my_arr[i]

print(hm)
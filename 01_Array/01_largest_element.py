


# # Brute force
def largest_element(arr):
    arr.sort()
    return arr[-1]

#Optimal

def largest_element_optimal(arr):
    n = len(arr)
    largest = int(-1e9)
    for i in range(1,n):
        if(arr[i] > largest):
            largest = arr[i]
    return largest



my_arr = [8,10,5,7,9]
print(largest_element(my_arr))
print(largest_element_optimal(my_arr))
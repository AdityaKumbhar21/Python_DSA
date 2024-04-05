# # Brute force
def second_smallest_element(arr):
    arr.sort()
    return arr[1]

#Optimal

def second_smallest_element_optimal(arr):
    n = len(arr)
    smallest = int(1e9)
    sec_smallest = int(1e9)
    for i in range(1,n):
        if(arr[i] < smallest):
            sec_smallest = smallest
            smallest = arr[i]
        if(sec_smallest != arr[i] and sec_smallest > arr[i]):
            sec_smallest = arr[i]
    return sec_smallest


my_arr = [1, 2, 3, 4, 5]
print(second_smallest_element(my_arr))
print(second_smallest_element_optimal(my_arr))
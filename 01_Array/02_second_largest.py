# # Brute force
def second_largest_element(arr):
    arr.sort()
    return arr[-2]

#Optimal

def second_largest_element_optimal(arr):
    n = len(arr)
    largest = int(-1e9)
    sec_largest = int(-1e9)
    for i in range(1,n):
        if(arr[i] > largest):
            sec_largest = largest
            largest = arr[i]
        if(sec_largest != largest and sec_largest > arr[i]):
            sec_largest = arr[i]
    return sec_largest


my_arr = [1, 2, 3, 4, 5]
print(second_largest_element(my_arr))
print(second_largest_element_optimal(my_arr))
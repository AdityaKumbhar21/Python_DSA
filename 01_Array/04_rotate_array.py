# Left rotate array by k places



def rotate_arr_brute(arr, n, k):
     if k == n:
         return arr
     temp_arr = []
     for i in range(0,k):
          temp_arr.append(arr[i])
   
     for i in range(0,n):
          arr[i] = arr[(k+i) % n]
    
     
     for i in range(n-k, n):
          arr[i] = temp_arr[i - (n-k)]
     return arr

def rotate_arr_brute_right(arr, n, k):
     if k == n:
         return arr
     temp_arr = []
     for i in range(n-k,n):
          temp_arr.append(arr[i])
   
     for i in range(n - 1, k - 1, -1): 
        arr[i] = arr[i - k]
    
     
     for i in range(k):
          arr[i] = temp_arr[i]
     return arr



# Optimal solution:


def reverse_arr(arr,start_ind, end_ind):
     while(start_ind <= end_ind):
          arr[start_ind] , arr[end_ind] = arr[end_ind], arr[start_ind]
          start_ind += 1
          end_ind -= 1

def rotate_arr_opt(arr, n, k): 
     k = k%n
     if k == n:
          return arr

     reverse_arr(arr,0,k-1)

     reverse_arr(arr,k,n-1)

     reverse_arr(arr,0,n-1)

     return arr



# to right rotate array:

     # reverse_arr(arr,0,n-1)
     # reverse_arr(arr,0,k-1)
     # reverse_arr(arr,k,n-1)




arr = [1, 3, 6, 11, 12, 17]
print(rotate_arr_brute(arr, len(arr), 4))
print(rotate_arr_brute_right(arr, len(arr), 4))
print(rotate_arr_opt(arr,6,4))
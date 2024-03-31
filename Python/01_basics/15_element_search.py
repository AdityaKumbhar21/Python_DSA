def linear_search(my_list, key):
    flag = False
    ind = 0
    for i, ele in enumerate(my_list):
        if key == ele:
            flag = True
            ind = i
            break
    if flag == True:
        print("The element is present in the list at the index: ", ind)
    else:
        print("The element is not present in the list")

my_list = [3,4,15,48,56,78,99]
linear_search(my_list, 15)

# Array from 0's and 1's
# I will use bubble sort method
# Consider list from elements with 0 and 1 values

arr = [0,0,0,1,1,0,1,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,0,1,1,1,1]

def bubble_sort (array_obj):

# Keep length of the list in variable for not recalculate it at every iteration

    arr_len = len(array_obj)

# Iterate on every element of the list

    for i in range (arr_len):

# last i elements are already in their places

        for j in range (0, arr_len-i-1):

# Compare two consecutive elements

            if array_obj[j]>array_obj[j+1]:

# Swipe them if the left one is bigger than right one

                array_obj[j], array_obj[j+1] = array_obj[j+1], array_obj[j]

# Run

bubble_sort (arr)
print (arr)

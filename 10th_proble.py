# Remove duplicates from list
# Realization in python

# Assume we have an array like this
array = [1,2,3,4,5,2,3,1,2,5,1,1,'Jack','John','Ken','Jim','Jim','John']

# Create the list where we place the array without duplicates

no_dupl = []

# There are more ways easier than this one but let's use brute force method

def rmv_dplct(arr,unique_arr):
    # put the length of array in variable to avoid recounting it in every itteration
    arr_len = len(arr)

    for i in range(arr_len):
        if not arr[i] in unique_arr:
            unique_arr.append(arr[i])
        
    return unique_arr

# run it

print(rmv_dplct(array,no_dupl))

# also we could use sort and remove or other pythonic ways to do the same

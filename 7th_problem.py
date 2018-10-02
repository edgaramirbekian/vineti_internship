# You have a list of numbers from one to one million
#   and there is a missing number. 
# How would you find the missing number?
# Realisation in Python 3

# Let's create list with one million elements
# and randomly delete one from it

from random import randint

milion_list = [item for item in range(0,1000000)]
print(len(milion_list))
random_index = randint(0,1000000)
milion_list.remove(random_index)
# to see that one element has vanished
print(len(milion_list))

# we are done so let's find that number

def search_item (arr):
    # consider there are no duplicates
    # use the continuity sum formula
    arr = sorted(arr)
    n = len(arr) 
    total = (n)*(n+1)/2
    # if the list had been started from 1 not 0 we must use
    # total = (n+1)*(n+2)/2 formula
    sum_of_arr = sum(arr) 
    return int(total - sum_of_arr) 
    
        

print(search_item(milion_list))
string_user = 'AAABCCDDDD'

# import getsizeof from sys to calculate the sizes of strings

from sys import getsizeof

def cnv(string_item):

# Define string which will contain the converted variant of user string

    convert_str = ''

# Define counter to count each character's quantity in word
    count = 1

# Create loop between [0, length of user string -1] to not get out from string

    for i in range(len(string_item)-1):
        if string_item[i] == string_item[i+1]:
            count += 1
        else:
            convert_str += string_item[i] + str(count)
            count = 1
# Don't forget the last cahracter in the word

    convert_str += string_item[i] + str(count)

# Convert only if we win in memory usage

    if getsizeof(string_item) >= getsizeof(convert_str):
        return convert_str
    else:
        return string_item

print(cnv(string_user))

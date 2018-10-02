string_user = 'AAABCCDDDD'
from sys import getsizeof

def cnv(string_item):
    convert_str = ''
    count = 1
    for i in range(len(string_item)-1):
        if string_item[i] == string_item[i+1]:
            count += 1
        else:
            convert_str += string_item[i] + str(count)
            count = 1
    convert_str += string_item[i] + str(count)

    if getsizeof(string_item) >= getsizeof(convert_str):
        return convert_str
    else:
        return string_item

print(cnv(string_user))


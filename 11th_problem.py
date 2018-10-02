# How would you determine if a string has all unique characters?
# Consider that Capital letter A is the same as a

user_str = input('Write a word :) --- ')

user_str_len = len(user_str)

# Using a flag to know is there repetitive characters

finded = False

for chrctr in range (user_str_len-1):
    if finded == False:
        for i in range (chrctr + 1, user_str_len):
            if user_str[chrctr] == user_str[i]:
                finded = True
            else:
                finded = False

if finded == False:
    print ("Your word contains unique characters")
else:
    print ("Your word has repetitive character")
    
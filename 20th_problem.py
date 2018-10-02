# Longest palindrome

word = input ("Your word please: ")

def longest_poli (the_word):

# Define indicators for iteration

    start = 0
    end = len(the_word)

#Define longest palindrome substring, and left-right borders

    longest_sub, r_border, l_border = 0, 0, 0
    
    for i in range(start, end):

# end + 1 becouse when the_word[i:j] j isn't counting

        for j in range(i+1, end+1):
            sub = the_word[i:j]

# check if substring is the longest polindrome or not

            if sub == sub[::-1] and len(sub) > longest_sub:
                longest_sub = len(sub)
                r_border, l_border = j, i
                
# create the polindrome substring

    result = the_word[l_border:r_border]
    return result, len(result)

print(longest_poli(word))
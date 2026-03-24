import collections

# Check if two strings are anagrams
def str_anargams(first_word:str,second_word:str)->bool:
    first_word=collections.Counter(first_word)
    second_word=collections.Counter(second_word)

    return first_word==second_word
print(str_anargams('listen','silent'))

# Remove all whitespaces from a string
def no_whitespaces(text:str)->str:
    words=text.split(' ')
    new_strig=''.join(words)
    return new_strig

# Count the occurrence of each character in a string
def char_occ(text:str)->dict: # this is faster
    clean_text=no_whitespaces(text)
    char_frequency= collections.Counter(clean_text)
    return char_frequency

def char_occ_manual(text:str)->dict:
    clean_text=no_whitespaces(text)
    d={}
    for char in clean_text:
        d[char]=d.get(char,0)+1
    return d

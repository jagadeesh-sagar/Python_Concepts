'''
Remove duplicates from sorted list in-place

'''
# fast and slow two pointer
def rmv_duplicates(sorted_list:list)->list:
    l=0
    for r in range(1,len(sorted_list)):
        if sorted_list[l]!=sorted_list[r]:
            l+=1
            sorted_list[l]=sorted_list[r]
    print(sorted_list)

rmv_duplicates(sorted_list=[1,2,2,3])

'''
Reverse words in a string - "hello world" → "world hello"
'''

def rev_words_list(text:str)->str:  # without two pointer
    words=text.split(' ')
    reversed_words=' '.join(words[::-1])
    print(reversed_words)

text='hello words'
rev_words_list(text)


def rev_words(text:str)->str:
    words=text.split(' ')
    l=0
    r=len(words)-1

    while(l<r):
        temp=words[l]
        words[l]=words[r]
        words[r]=temp
        r-=1
        l+=1
    print(words)


rev_words(text='hello world this a python')
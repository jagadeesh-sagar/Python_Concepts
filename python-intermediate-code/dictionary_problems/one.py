'''
Find first unique character in a string using dictionary

aabb=>None
loveleetcode->v
aabbccd->d
success->u
'''


def unique_char(word:str)->str:

    d={}

    for letter in word:
        d[letter]=d.get(letter,0)+1
    
    for letter in word:
        if d.get(letter)==1:
            return letter
        

word='aabbccd'
# print(unique_char(word))

'''
Check if two strings are isomorphic - "egg" and "add" are isomorphic

'''

def isomorphic(first_word:str,second_word:str)->str:
    '''
    paper , title -> false
    egg , add -> True

    '''

    d={}
    d1={}

    for i in range(len(first_word)):
        if d.get(first_word[i]) and d[first_word[i]]!=second_word[i]:
            return False
             
        elif d1.get(second_word[i] )and d1[second_word[i]]!=first_word[i]: 
          return False
        
        else:
          d[first_word[i]]=second_word[i]
          d1[second_word[i]]=first_word[i]

    return True

first_word='paper'
second_word='title' 

# print(isomorphic(first_word,second_word))


'''
Group elements by frequency - Return elements sorted by frequency
[1,1,1,2,2,3]  -> [1,2,3]

[4,4,4,6,6,1,1,1,1]-> [1,4,6]

'''
def frequency_grp(list1:list[int])->list[int]:

    d={}
    result=[]

    for i in list1:
        d[i]=d.get(i,0)+1
  
    # sort based on frequency (highest first)  “Take all dictionary keys and sort them according to their frequencies from highest to lowest.”
    result = sorted(d.keys(), key=lambda x: d[x], reverse=True)

    return result
      


print(frequency_grp(list1=[4,4,4,4,6,6,1,1,1,1]))

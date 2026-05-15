'''
Remove element in-place from list - Remove all occurrences of a value
[3,2,2,3] = 3 -> [2,2]

[0,1,2,2,3,0,4,2] = 2-> [0,1,3,0,4]

'''

def rem_occurrences(list1:list[int],n:int)-> list[int]:

    l=list1.copy()
    for i in l:
        if i==n:
            list1.remove(n)
    
    return list1

# rem_occurrences(list1=[0,1,2,2,3,0,4,2],n=2)

def rem_occurences_2(list1,n):
    r,l,count=0,0,0
    length=len(list1)

    while(r<length):
        if list1[r]!=n:
            list1[l]=list1[r]
            l=l+1
        # else:
            # count=count+1
        r=r+1  

    # length=length-count         
    return list1[:l]

print(rem_occurences_2(list1=[3,2,2,3],n=2))
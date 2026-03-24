# Rotate a list by n positions
def rotate_list(list1:list[int],list2:list[int])->list[int]:  #O(n)
    n:int=3
    for i in range(0,len(list1)):
        list2.append(list1[-n+i])

    return list2

def rotate_list_2(list1:list[int])->list[int]: #O(n)
    n:int=3
    rotated=list1[-n:]+list1[:-n]
    return rotated

from collections import deque

def rotate_list_3(list1:list[int])->list[int]:  #O(k)
    n:int=3
    d=deque(list1)
    d.rotate(n)
    return list(d)

list1:list[int]=[1,2,3,4,5,6,7,8,9,10]
list2:list[int]=[]

rotate_list_3(list1)

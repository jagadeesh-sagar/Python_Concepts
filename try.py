# Find the intersection of two lists

def intersection_list(list1:list[int],list2:list[int])->list[int]:

    intersection_list= list(set(list1)&set(list2))
    return intersection_list

list1=[1,2,3,4,5]
list2=[3,4,5]
print(intersection_list(list1,list2))
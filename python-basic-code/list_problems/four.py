# Merge two sorted lists

def merge_two_list(list1:list[int],list2:list[int])->None:
    list1.extend(list2)
    list1.sort()
    print(list1)

list1:list=[1,2,3,4,5,6]
list2=[8,9,9,10,11,13]

merge_two_list(list1,list2)
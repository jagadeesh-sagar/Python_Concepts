'''
Move all zeros to end of list - [0,1,0,3,12] → [1,3,12,0,0]
[1, 2, 0, 0]
[1, 2, 3]
[0,0,0]
[4, 0, 5, 0, 0, 3, 0, 1]
[0, -1, 0, -3, 5]

'''

def zero_end(list1:list)->list:

    l=0
    r=0
    while(r<len(list1)):
        if(list1[r]!=0):
            temp=list1[r]
            list1[r]=list1[l]
            list1[l]=temp
            l+=1
        elif(list1[r]==0 and list1[l]!=0):
            l=r 
        r+=1
        
    return list1

# print(zero_end(list1=[0, -1, 0, -3, 5]))

def zero_end_2(arr: list) -> list:
    l = 0

    for r in range(len(arr)):
        if arr[r] != 0:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1

    return arr

# print(zero_end_2(arr=[0, -1, 0, -3, 5]))

'''👉 Remove Duplicates from Sorted Array (same pattern)

[0,0,1,1,1,2,2,3,3,4] ->[0,1,2,3,4,_,_,_,_,_]

'''


def Rmv_duplicates(arr:list[int])->list[int]:
    l,r=0,0

    while (r<len(arr)):
        if arr[r]!=arr[l]:
            arr[l+1]=arr[r]
            l+=1
        r+=1

    return l+1,arr


# print(Rmv_duplicates(arr=[0,0,0,1,1,1,2,2,3,3,4]))

'''
👉 Partition array (even/odd, negatives/positives)

[3,1,2,4] ->[2,4,3,1] (even/odd)

[-1,2,-3,4,-5,6]->[-1,-3,-5,2,4,6] (negative/postive)

'''

def odd_even(a:list)->list:  # chatgpt says that this swap caues issues so use list to appen(order) swap(no order)
    l=0

    for r in range(len(a)):
        if (a[r]%2==0):
            a[l],a[l+1:r+1]=a[r],a[l:r]  
            l+=1
    return a

print(odd_even(a=[4,6,8,-2]))


# ✅ 2. Stable Partition (order preserved — advanced)

# 👉 Even numbers stay in same order

def odd_even(arr: list) -> list:
    result = []

    # add evens
    for num in arr:
        if num % 2 == 0:
            result.append(num)

    # add odds
    for num in arr:
        if num % 2 != 0:
            result.append(num)

    return result
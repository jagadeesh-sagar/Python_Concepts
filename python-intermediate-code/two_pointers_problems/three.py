'''
Find pair with given difference - Find two numbers with difference k

'''

def k_difference(nums:list,k:int)->bool:
    from collections import Counter
    d1=Counter(nums)

    count=0

    for num in d1:
        s=num+k

        if s in d1 :
            if k!=0:
                count+=1
            elif d1[num]>1:
                count+=1

    return count


print(k_difference(nums=[8, 12, 16, 4, 0, 20],k=4))



# find only duplicates
def list_duplicates(nums:list[int])->list[int]:

    duplicates=[]
    d={}
    for num in nums:
        d[num]=d.get(num,0)+1
    
    for num,count in d.items():
        if count>1:
            duplicates.append(num)
    return duplicates

print(list_duplicates([10,2,4,53,2,4,6,3]))


def list_duplicates_single_loop(nums:list[int])->list[int]:
    seen=set()
    duplicates=set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

print(list_duplicates_single_loop([10,2,4,53,2,4,6,3]))
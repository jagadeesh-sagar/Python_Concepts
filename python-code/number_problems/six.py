# Check if a list is sorted

def is_increasingly_sorted(nums:list[int])->bool:
    for i in range(0,len(nums)-1):
        if(nums[i]>nums[i+1]):
            return False
    return True

def is_decreasingly_sorted(nums:list[int])->bool:
    for i in range(0,len(nums)-1):
        if(nums[i]<nums[i+1]):
            return False
    return True

def sorted_list(nums:list[int])->bool:
    return is_increasingly_sorted(nums) or is_decreasingly_sorted(nums)

if (sorted_list([1,2,3,3,4,5,6])):
    print('sorted')
else:
    print('not sorted')
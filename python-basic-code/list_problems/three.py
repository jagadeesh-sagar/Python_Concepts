# Find the missing number in a list of 1 to n

def miss_num(list1:list[int],n:int)->None: #useful for more than 1 missing numbers
    for i in range(n):
        valule=i+1
        if(list1.__contains__(valule)):
            print('')
        else:
            print(valule)

def miss_num_2(list1:list[int],n)->None:
    expected_sum=n*(n+1)//2
    actual_sum=sum(list1)
    missing_num=expected_sum-actual_sum
    print(missing_num)

def miss_num_3(list1:list[int],n)->None:
    set_list=set(list1)
    for i in range(n):
        num=i+1
        if num not in set_list:
            print(num)

def miss_num_4(list1:list[int],n)->None:
    missing_nos=set(range(1,n+1))-set(list1)
    print(missing_nos)

def find_missing_sorted(list1, n):
    low = 0
    high = len(list1) - 1
    
    # If the last element is n-1, then n is the missing one
    if list1[-1] != n:
        return n
    # If the first element isn't 1, then 1 is missing
    if list1[0] != 1:
        return 1

    while low <= high:
        mid = (low + high) // 2
        
        # Check if the discrepancy starts here
        if list1[mid] == mid + 1:
            # Everything is normal on the left, look right
            low = mid + 1
        else:
            # Something is missing on the left or is exactly at mid
            high = mid - 1
            
    return low + 1

# Test
list1 = [1, 2, 3, 5, 6]
n = 6
print(f"The missing number is: {find_missing_sorted(list1, n)}")

list1=[1,2,5,6]
n=6
miss_num_4(list1,n)


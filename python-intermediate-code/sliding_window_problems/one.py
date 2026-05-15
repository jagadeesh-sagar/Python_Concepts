'''
Maximum sum of k consecutive elements

window_sum + new - old is the key pattern

'''

def consecutive_elements(num_list:list,k:int)->int:

    count,sum_list,left=0,0,0

    max_sum=sum(num_list[:k]) # i used this so that it can handle alll negative numbers too
    # max_sum = float('-inf') start with infinite negative

    for i in num_list:
        sum_list=sum_list+i
        count+=1
        if count==k:
            max_sum=max(sum_list,max_sum)
            sum_list=sum_list-num_list[left]
            left+=1
            count-=1
    return max_sum

print(consecutive_elements(num_list=[1, 9, -1, -2, 7, 3],k=2))


def consecutive_elements_2(num_list:list,k:int)->int:

    if len(num_list)<1:  # handling edge case
        return 0
    
    window_sum=sum(num_list[:k]) # cal 1st window sum so negative can be handled
    max_sum=window_sum

    # slide the window
    for i in range(k,len(num_list)):
        # add new element and remove last one

        window_sum=window_sum+num_list[i]-num_list[i-k]
        max_sum=max(max_sum,window_sum)

    return max_sum

print(consecutive_elements_2(num_list=[1, 9, -1, -2, 7, 3],k=2))

    
# All these work:
test_cases = [
    ([1, 9, -1, -2, 7, 3], 2, 10),
    ([-1, -2, -3,-4], 2, -3),
    ([5, 2, 8, 1, 9], 3, 18),
    ([1, 2, 3, 4, 5], 1, 5),
]

for arr, k, expected in test_cases:
    result = consecutive_elements_2(arr, k)
    print(f"Input: {arr}, k={k}")
    print(f"Expected: {expected}, Got: {result}")
    print(f"✅ Pass" if result == expected else "❌ Fail")
    print()
# //////////////////////////////////////////////////////
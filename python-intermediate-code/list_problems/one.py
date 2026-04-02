'''
Find the longest consecutive sequence - [100, 4, 200, 1, 3, 2] → 4 (sequence: 1,2,3,4)
'''
def cons_seq(list1: list) -> int:
    if not list1:
        return 0

    sorted_unique_list = sorted(list(set(list1)))
    
    if not sorted_unique_list: # Handles cases where list1 might contain non-sortable items or become empty after set conversion
        return 0

    max_consecutive_length = 0
    current_consecutive_length = 0

    # Initialize for the first element if the list is not empty
    if sorted_unique_list:
        max_consecutive_length = 1
        current_consecutive_length = 1

    for i in range(1, len(sorted_unique_list)):
        if sorted_unique_list[i] == sorted_unique_list[i-1] + 1:
            current_consecutive_length += 1
        else:
            # Sequence broke, update max_consecutive_length if current is longer
            max_consecutive_length = max(max_consecutive_length, current_consecutive_length)
            current_consecutive_length = 1  # Reset for a new sequence

    # After the loop, compare one last time to catch the sequence at the end of the list
    max_consecutive_length = max(max_consecutive_length, current_consecutive_length)
    
    return max_consecutive_length

# cons_seq(list1=[1, 2, 2, 3]
# )

def cons_seq_1(list1:list)->int: #o(n)

    sorted_list=sorted(set(list1))
    s=set(sorted_list)

    max_len=0
    seq=1

    for i in sorted_list:
        if i+1 in s:
            seq=seq+1
        else:
            max_len=max(max_len,seq)
            seq=1
    return max_len


print(cons_seq_1(list1=[-2, -1, 0, 2, 3, 4]))


def longest_consecutive(nums: list) -> int:  #O(n)
    num_set = set(nums)
    max_len = 0

    for num in num_set:
        # start of sequence
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            max_len = max(max_len, length)

    return max_len


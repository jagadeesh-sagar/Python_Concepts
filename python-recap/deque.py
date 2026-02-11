'''Pythons deque is implemented as a doubly-linked list of fixed-size blocks, allowing O(1) insertions and deletions
 at both ends while maintaining good cache locality and low memory overhead.
 -> each block is contiguos arrays of 64 elements
 '''
'''
operations at ends are very efficent that's why it is used in such cases compared to list
'''

from collections import deque

q = deque([1, 2, 3])
q.appendleft(0)   # O(1)
q.popleft()       # O(1)

q.append(4)  # O(1)
q.pop()     # O(1)   

# q.remove(n)  # is slower beoz of shifitng just like in lists
q.insert(5,2) # 5 is the place , 2 is the value
print(q)
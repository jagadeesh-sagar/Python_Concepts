'''
1. base case (when to stop the infinte recusrion)
2. recursive case (how we reduce the problem)
3. return 

'''

'''
LC 509 — Fibonacci Number

'''

def fibionacci(n):
    if n<=0:
        return 0
    if n==1:
        return 1

    return fibionacci(n-1)+fibionacci(n-2)

# print(fibionacci(10))


'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

'''

result=[]
def reverseList(head):
    if not head:
        return 
    result.append(head.pop())

    return reverseList(head)

# print(reverseList(head=[1,2,3,4,5]),result)
    

def reverseList2(head):
    if not head:
        return []

    return [head.pop()]+reverseList2(head)

# print(reverseList2(head=[1,2,3,4,5]))


'''
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''

def reverseString(s):

    if not s:
        return []

    return [s.pop()]+reverseString(s)

def reverseString(self, s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    n=len(s)
    def reverse(left,right):
        if left>right:
            return s
        
        s[left],s[right]=s[right],s[left]

        return reverse(left+1,right-1)

    s=reverse(0,n-1)

# print(reverseString(s=["H","a","n","n","a","h"]))

# def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
def reverseString(head):

    if not head or not head.next: # base to find the last node
        return head
    
    new_head=reverseList(head.next)  # move to the next node

    head.next.next=head # reversing the links
    head.next=None # avoiding circulars

    return new_head


'''

24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

'''
def swapPairs(head):

    if not head or not head.next:
        return head

    second=head.next

    rest=swapPairs(second.next) # directly go for nxt pair

    second.next=head 
    head.next=rest

    return second # returning 1st pair

def power(x,n):

    if n==0:
        return 1
    if n<0:
        return 1/power(x,-n)
    else:

     return x*power(x,n-1)

# print(power(2,9))


def power2(x,n):
    if n==0:
        return 1
    if n<0:
        return 1/x*power(x,n+1)

    half=power2(x,n//2)
    # print(half)

    if n%2==0:
        return half*half 
    else:
        return half*half*x

# print(power2(2,9))

'''
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

'''

from functools import lru_cache
@lru_cache(None) # this makes below recursion as O(n) with memorization

def climbStairs(n):  # O(2^n) as it calclated same values multiple time 
    if 0<n<3:
        return n
      
    return climbStairs(n-1)+climbStairs(n-2)

'''
just like fibbonacci .. here we have two options one how many ways using 1 step and 2 steps at a time (adding all ways for each step)

'''
print(climbStairs(44))


def climbStairs2(n):

    result=[1,2]

    for i in range(3,n+1):
        sum_ways=result[-1]+result[-2]
        result.append(sum_ways)

    return result[-1]

print(climbStairs2(n=44))

'''
top-down dynamic programming (memoization).
'''
def climbStairs3(n ,memo={}):

    if n<=2:
        return n 

    if n in memo:
        return memo[n]

    memo[n]=climbStairs3(n-1,memo)+climbStairs3(n-2,memo)

    return memo[n]
'''
we just like pruning same calculations
'''

print(climbStairs3(n=44))




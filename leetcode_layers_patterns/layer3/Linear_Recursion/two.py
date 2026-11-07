'''
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

'''

def mergeTwoLists(list1,list2):

    if not list1:
        return list1
    if not list2:
        return list2

    if list1.val<=list2.val:
        list1.next=mergeTwoLists(list1.next,list2)
        return list1
    else:
        list2.next=mergeTwoLists(list1,list2.next)
        return list2

'''
That's the return-value pattern you should pay attention to.

Recursive call solves the smaller problem and returns its head. The current node then attaches itself to that returned head.

This is a really important recursion pattern for linked lists.

'''


'''
203. Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
'''

def removeElements(head,val):

    if not head or not head.next:
        if not head or head.val!=val:
            return head
        else:
            return None

    if head.val!=val:
        head.next=removeElements(head.next,val) # returning the node pointer link as it valid
        return head
    else:
        head.next=removeElements(head.next,val)
        return head.next # we are reuturining the next pointer link (becoz its node value is not valid so the next ones)


'''
92. Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
 
'''
'''
in this logic the prev and current does move anywhere 


          take this node
               ↓
1 → [4] → 3 → 2 → 5
     ↑
 insert here


'''


def reverseBetween(self, head, left: int, right: int) :
    successor=None

    def reverse(node,n):
        nonlocal successor
        if n==1:
            successor=node.next
            return node

        new_head=reverse(node.next,n-1) 

        node.next.next=node
        node.next=successor

        return new_head
    
    if left==1:
        return reverse(head,right)
    
    head.next=self.reverseBetween(head.next,left-1,right-1)
    return head



def reverseBetween(head,left,right):

    if not head and left==right:
        return head

    dummy=ListNode(0,head)

    prev=dummy

    for _ in range(left-1):
        prev=prev.next

    current=prev.next
    for _ in range(right-left):
        temp=current.next
        current.next=current.next.next
        temp.next=prev.next
        prev.next=temp

    return dummy.next

'''

143. Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''

def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy=head
        if not head or not head.next:
            return

        def rev(head):
            nonlocal dummy

            if head is None:
                return 

            rev(head.next)

            if dummy is None:
                return     

            if dummy == head or dummy.next == head:
                head.next=None
                dummy=None
                return 

            temp = dummy.next
            dummy.next=head
            head.next=temp

            dummy=temp
        
        rev(head)

'''
A short recursive solution is tricky.
The easier way is to use Floyd's turtoise & Hase, reverse the 2nd half & merge.
'''
def reorderList(self, head) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if not head or not head.next:
        return None
    slow=head
    fast=head

    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next

    temp=slow
    rev=slow.next

    while rev.next:
        current_temp=rev.next
        rev.next=rev.next.next
        current_temp.next=temp.next
        temp.next=current_temp

    print(temp)
    rev_second=temp.next
    temp.next=None

    while rev_second and head:
        cur_temp=rev_second
        rev_second=rev_second.next
        cur_temp.next=head.next
        head.next=cur_temp
        head=cur_temp.next

    print(rev_second)



"""

Stage 1 — Very simple recursion
Do these first:
1. LC 50 — Pow(x, n)
   Learn recursion where the function returns a computed result.
2. LC 70 — Climbing Stairs
   Learn how one problem branches into smaller problems.
3. LC 21 — Merge Two Sorted Lists
   ⭐ Very good for linked-list recursion.
   Think: "Let recursion handle the rest; I only decide the current node."
4. LC 203 — Remove Linked List Elements
   Good for understanding how recursion returns a modified linked list.


Stage 2 — Build the "trust recursion" mindset
These are especially useful:
5. LC 92 — Reverse Linked List II
   This is harder than LC 206 and will force you to understand what recursion is returning.
6. LC 234 — Palindrome Linked List
   Good combination of recursion + pointers.
7. LC 143 — Reorder List
   Don't worry if this feels hard. It's a good checkpoint later."""
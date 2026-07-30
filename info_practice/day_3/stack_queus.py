'''
20. Valid Parentheses

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

'''

def valid_parentheses(s:str)->bool:

    stack=[]
    mapping={')':'(',']':'[','}':'{'}

    for ch in s:
        if ch in mapping:
            if not stack or stack[-1]!=mapping[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return len(stack)==0




# print(valid_parentheses(s="([])"))

class MinStack:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        self.min_value=float('inf')
        
    def push(self, val: int) -> None:
        self.stack1.append(val)
        self.min_value=min(self.min_value,val)
        self.stack2.append(self.min_value)
    
    def pop(self) -> None:
        self.stack1.pop()
        self.stack2.pop()
        if self.stack2[-1]==None:
            self.min_value=float('inf')

        else:
            self.stack2[-1]!=self.min_value
            self.min_value=self.stack2[-1]
        # self.min_value=

    def top(self) -> int:
        return self.stack1[-1]
        

    def getMin(self) -> int:
        return self.stack2[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(2)
# obj.push(3)
# obj.push(4)
# obj.push(1)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# # print(param_3,param_4)

def daily_temperatures(temperatures:list[int])->list[int]:

    
    '''
Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

'''
    mono_stack:list[int]=[]
    result=[0]*len(temperatures)

    for i in range(len(temperatures)):

        if not mono_stack or temperatures[mono_stack[-1]]>temperatures[i]:
            mono_stack.append(i)
        else:
            while mono_stack and temperatures[mono_stack[-1]]<temperatures[i]:
                lower_temp_index=mono_stack.pop()
                result[lower_temp_index]=i-lower_temp_index
            mono_stack.append(i)

    return result

'''
here we used monotonic stack of decreasing order -> the elements are placed with rule of decreasing order
if new element larger pop all elements that are smaller that this

this new element becomes next largest element for the poped ones

same logic for increasing order useful for finding nxt smallest number

'''


# print(daily_temperatures(temperatures=[89,62,70,58,47,47,46,76,100,70]))

'''
Use a:

Monotonic Stack

when problems ask things like:

next greater
next smaller
previous greater
previous smaller
nearest greater/smaller



'''

'''
496. Next Greater Element I
Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
'''

def nextGreaterElement(nums1:list[int],nums2:list[int])->list[int]:

    mono_stack=[]
    result=[-1]*len(nums1)
    d={}

    for i in range(len(nums2)):

        if len(mono_stack)==0 or nums2[mono_stack[-1]]>nums2[i]:
            mono_stack.append(i)
        else:
            while mono_stack and nums2[mono_stack[-1]]<nums2[i]:
                lower_temp_index=mono_stack.pop()
                d[nums2[lower_temp_index]]=nums2[i]

            mono_stack.append(i)

    for j in range(len(nums1)):
        if nums1[j] in d:
            result[j]=d[nums1[j]]

    return result
'''
whenever u thinking of O(n2) solution think like this 
O(m+n) for these two seperate loops and 1st loop values save somewhere

'''

# print(nextGreaterElement(nums1=[2,4],nums2=[1,2,3,4]))


def largestRectangleArea(heights: list[int])->int:

    heights.append(0)
    mono_stack=[]
    max_area=0

    for i in range(len(heights)):

        while mono_stack and heights[mono_stack[-1]]>heights[i]:
            high_rect_index=mono_stack.pop()
            height=heights[high_rect_index]

            width=i if not mono_stack else i-mono_stack[-1]-1 
            max_area=max(max_area,height*width)

        mono_stack.append(i)
    return max_area

'''
as we reach smaller rectangles we avoid them as they contribut to lesser area 
so main logic is to find next and prev smaller heights and avoid them completey
'''
largestRectangleArea(heights=[2,1,5,6,2,3])

'''
1793. Maximum Score of a Good Subarray

Example 1:

Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 

Example 2:
Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.

'''            
def maximumScore(nums: list[int], k: int) -> int:

    left = right = k
    minimum = nums[k]
    max_score = nums[k]

    while left > 0 or right < len(nums) - 1:

        if left == 0:
            right += 1

        elif right == len(nums) - 1:
            left -= 1

        elif nums[left - 1] > nums[right + 1]:
            left -= 1

        else:
            right += 1

        minimum = min(minimum, nums[left], nums[right])

        max_score = max(max_score, minimum * (right - left + 1))

    return max_score


maximumScore(nums=[6569,9667,3148,7698,1622,2194,793,9041,1670,1872],k=5)


'''

232. Implement Queue using Stacks
'''
class MyQueue:

    def __init__(self):
        self.queue1=[]
        self.queue2=[]
        

    def push(self, x: int) -> None:

        while(len(self.queue1)!=0):
           self.queue2.append(self.queue1.pop())
        self.queue1.append(x)

        while self.queue2:
            self.queue1.append(self.queue2.pop())

    def pop(self) -> int:
        return self.queue1.pop()

    def peek(self) -> int:
        return self.queue1[-1]
        
    def empty(self) -> bool:
        return 0==len(self.queue1)
'''
in this implmentation the push taking more than 4 operations with some 3n so totallt O(n) for single push
but pop() very less  its 1st approcah check leetcode 232  
'''

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(4)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_4)


class MyQueue_2:

    def __init__(self):
        self.queue1=[]
        self.queue2=[]
        

    def push(self, x: int) -> None:
        self.queue1.append(x)        

    def pop(self) -> int:
        if len(self.queue2)==0:
            # self.queue2=self.queue1[::-1]
            while(len(self.queue1)!=0):
              self.queue2.append(self.queue1.pop())

        return self.queue2.pop()     

    def peek(self) -> int:
        return self.queue2[-1] if len(self.queue2)!=0 else self.queue1[0]
        
    def empty(self) -> bool:
        return len(self.queue1) == 0 and len(self.queue2) == 0
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue_2()
obj.push(4)
param_2 = obj.pop()
obj.push(5)
obj.pop()
obj.pop()
obj.pop()
obj.pop()

# param_3 = obj.peek()
# param_4 = obj.empty()




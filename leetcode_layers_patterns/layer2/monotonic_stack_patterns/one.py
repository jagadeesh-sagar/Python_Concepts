'''

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array,
which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]

'''


def nextGreaterElements(nums: list[int]) -> list[int]:

    stack=[]
    result=[-1]*len(nums)

    for i in range(len(nums)):
        while stack and nums[stack[-1]]<nums[i]:
            index=stack.pop()
            result[index]=nums[i]
        stack.append(i)

    i=0    
    #checking the remaing stack elements again with list
    while stack and i<len(nums) :
        while stack and nums[stack[-1]]<nums[i]:
            index=stack.pop()
            result[index]=nums[i]
        stack.append(i)
        i+=1
    return result

# print(nextGreaterElements(nums=[1,2,3,4,3]))


'''
85. Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

'''

def maximalRectangle(matrix: list[list[str]]) -> int:

    # stack=[]
    max_value=0
    result=[0]*len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if int(matrix[i][j])>0:
                result[j]+=int(matrix[i][j])
            else:
                result[j]=0

        # max_value=max(max_value,largestRectangleArea(heights=result))
        stack=[]
        heights=result.copy()
        heights.append(0)

        for k in range(len(heights)):
            while stack and heights[stack[-1]]>heights[k]:
                index=stack.pop()
                height=heights[index]

                width=k if not stack else k-stack[-1]-1

                max_value=max(max_value,height*width)
            stack.append(k)

    return max_value

# print(maximalRectangle(matrix= [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))

'''
901. Online Stock Span

'''

def StockSpanner(price):

    stack=[]
    result=[]

    for i in range(len(price)):
        count=1

        while stack and stack[-1][0]<=price[i]:
            stock_price=stack.pop()
            stock_days=stock_price[1]
            count+=stock_days

        result.append(count)        
        stack.append([price[i],count])
    return result

# print(StockSpanner(price=[28,14,28,35,46,53,66,80,87,88]))

'''
1475. Final Prices With a Special Discount in a Shop
You are given an integer array prices where prices[i] is the price of the ith item in a shop.

There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.
 

Example 1:

Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
Explanation: 
For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
For items 3 and 4 you will not receive any discount at all.


'''

def finalPrices(prices:list[int])->list[int]:

    stack=[]
    result=prices.copy()

    for i in range(len(prices)):
        while stack and prices[stack[-1]]>=prices[i]:
            index=stack.pop()
            result[index]=prices[index]-prices[i]

        stack.append(i)
    return result

print(finalPrices(prices=[10,1,1,6]))


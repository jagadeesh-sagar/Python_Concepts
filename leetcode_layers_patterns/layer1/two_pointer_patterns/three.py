
'''
845. Longest Mountain in Array
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.


Example 1:
Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:
Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.

cases : [0,1,2,3,4,5,6,7,8,9] => 0
[0,1,0] => 3
[875,884,239,731,723,685]=>4

 

'''

def longestMountain(arr):
    left=0
    right=1
    better=0
    end=0
    start=0
    peak=0

    while(right<len(arr)):

        # skip unitl u find increasing mountian and above condition is just complement
        while right<len(arr) and arr[right]<=arr[left]:
            right+=1 
            left+=1

        if right==len(arr):
            return better if better >=3 else 0
       
        start=left # start of the moutain

        while right<len(arr) and arr[right]>arr[left]:  # mountain increasing
            right+=1
            left+=1
            peak=left-1
        
        while right<len(arr) and arr[right]<arr[left] :  # decreasing mountain
            right+=1 
            left+=1
            end=left

        left=left-1

        if left>peak:          
            better=max(better,(end-start)+1)

        end=0
        peak=0

    return better if better >=3 else 0

# print(longestMountain(arr=[1,2,3,2,1,3,4,5,3,2]))

'''
kk in below code we expanding by finding the peak element rather manually 
finding increasing and decreasing soo that u avoided a lot of cases
'''

def longestMountain2(arr):

    # left=0
    # right=0
    ans=0
    n=len(arr)
    
    if n<3:
         return 0

    for i in range(1,n-1):

        # finding peak element and then expanding both sides
        if(arr[i-1]<arr[i]>arr[i+1]):  
            
            right=i
            left=i

            # Expand left (increasing side)
            while left>0 and arr[left]>arr[left-1]: 
                left-=1

             # Expand right (decreasing side)       
            while right<n-1 and arr[right]>arr[right+1]:    
                right+=1

            ans=max(ans,(right-left)+1)

            i=right  # skipping entire mountain that we just caluclated
   
    return ans

print(longestMountain2(arr=[3,2,1]))
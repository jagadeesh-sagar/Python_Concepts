'''

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23
# '''
def validate(k,piles,h):
    hours=0

    for pile in piles:
        if pile<k:
            hours+=1
        elif pile%k>=1:
            hours+=pile//k
            hours+=1
        else: 
             hours+=round(pile/k)
        
        # import math
        # math.ceil() we can use this too
        # hours += (pile + k - 1) // k  rather than all my logic use this(ceiling expression)

    return hours<=h
    

def minEatingSpeed(piles,h):
    left=1
    right=max(piles)

    while(left<=right):
        mid=(left+right)//2

        if validate(mid,piles,h):
            right=mid-1
        else:
            left=mid+1

    return left
'''
in here the logic is simple the monkey needs to complete all bananas in "h" hours
and in every pile(box) a no of bananas are there
then find the min no of bananas a monkey can eat per hour soo that all piles of banaans will complete
for every pile the monkey will take atleast a hour 

soo wt we have done is that 

we find the max no of banans pile and we cant eat more than that per hour
so we have to find a min element from 1 to max(piles) 

Binary search

1.soo we do binary search on 1 to max (do manually from 1 to max takes o(n) soo we avoid that)

2. for every no we validate wether k no of banana/hour completes all piles

3.1 :in binary search we avoid all left side of mid element if they are not valid
3.2 :if valid we move one step back and again validate

'''
# print(minEatingSpeed( piles = [3,6,7,11], h = 8))

'''
1011. Capacity To Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). 
We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Example 2:
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6

'''

def validate2(weights,capacity,days):
    sum_weights=0
    no_of_days=1

    for weight in weights:
        if sum_weights+weight>capacity:
            sum_weights=0
            no_of_days+=1

        sum_weights+=weight
        print(no_of_days,sum_weights,weight,capacity)

    return no_of_days<=days

def shipWithinDays(weights,days):
    right=sum(weights)
    left=max(weights)

    while (left<=right):
        mid=(left+right)//2

        if validate2(weights,mid,days):
            right=mid-1
        else:
            left=mid+1
    return left
'''

same like above code 
'''

# print(shipWithinDays(weights = [1,2,3,1,1], days = 4))

'''
2279. Maximum Bags With Full Capacity of Rocks
(not a binary search pblm but very close to what i got in infosys exam) 

'''

def maximumBags(capacity,rocks,additionalRocks):

    n=len(capacity)
    capacity_remaining=[0]*n
    max_bags=0

    for i in range(n):
        capacity_remaining[i]=capacity[i]-rocks[i]
    capacity_remaining.sort()

    for remaining in capacity_remaining:

        if remaining > additionalRocks:
            break

        additionalRocks -= remaining
        max_bags += 1

    return max_bags

# print(maximumBags([10,2,2], rocks = [2,2,0], additionalRocks = 100))


'''
"Minimize the maximum"
'''

'''
410. Split Array Largest Sum

Given an integer array nums and an integer k, 
split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
Return the minimized largest sum of the split.
A subarray is a contiguous part of the array.

Example 1:
Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

Example 2:
Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

'''

def validate3(max_sum,nums,k):

    subarrays=1
    subarray_sum=0

    for num in nums:
        if subarray_sum+num>max_sum:
            subarray_sum=0
            subarrays+=1

        subarray_sum+=num        

    return subarrays<=k


def splitArray(nums,k):

    high=sum(nums)
    low=max(nums)

    while(low<=high):
        mid=(low+high)//2

        if validate3(mid,nums,k):
            high=mid-1
        else:
            low=mid+1

    return low

'''
minimize the maximum pattern is simple 
1. find the largest possible (sum of all values)
2. find the smallest possible (highest value : maximum subarray should contain at least that value(greedy))
3. pick a candidate and validate 
4. do the binary search

10 ---------------------- 32
↑                           ↑
minimum possible            maximum possible
answer                      answer


'''

# print(splitArray( nums = [1,2,3,4,5], k = 2))

'''
3069. Distribute Elements Into Two Arrays I

'''

def resultArray(nums):
    n=len(nums)
    if n==1:
        return nums

    last_element_1=nums[0]
    last_element_2=nums[1]

    arr1=[last_element_1]
    arr2=[last_element_2]

    for i in range(2,n):
        if last_element_1>last_element_2:
            arr1.append(nums[i])
            last_element_1=nums[i]
        else:
            arr2.append(nums[i])
            last_element_2=nums[i]

    return arr1+arr2

# print(resultArray(nums=[1,2,14,15]))


'''
1482. Minimum Number of Days to Make m Bouquets

Input: bloomDay(no of days it takes to bloom a flower) = [1,10,3,10,2], m = 3, k = 1(types of flowers per bouqet)
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

'''
def validate4(bloomDay,max_days,bouque,k):
    flower=0
    consecutive_flowers=0

    for bm in bloomDay:

        if bm<=max_days:
            consecutive_flowers+=1
        else:
            consecutive_flowers=0

        if consecutive_flowers==k:
            flower+=1
            consecutive_flowers=0

        if flower==bouque:
            return True
        
    return False


def minDays(bloomDay,m,k):

    low=min(bloomDay)
    high=max(bloomDay)
    n=len(bloomDay)

    flowers_required=m*k
    bouque=m
    if flowers_required>n:
        return -1

    while(low<=high):
        mid=(low+high)//2

        if validate4(bloomDay,mid,bouque,k):
            high=mid-1
        else:
            low=mid+1

    return low

print(minDays([1,10,3,10,2], m = 3, k = 1))
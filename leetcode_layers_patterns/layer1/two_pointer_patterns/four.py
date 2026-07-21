'''

881. Boats to Save People
Medium
Topics
premium lock icon
Companies
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

'''

'''
[1,2,2,3]
'''

def numRescueBoats(people:list[int],limit):

    people.sort()
    print(people)
    right=len(people)-1
    boats_count=0
    left=0

    while(right>=left):

        # adding heavy guy first and searching the light guy who can fit ..
        # we search from sorted left so that if even one left fails all the upcomming left fails
        # so avoid searching complexity .. its greedy approach
        if people[right]+people[left]<=limit:  
            right-=1
            left+=1
        else:
            right-=1
    
        boats_count+=1
    return boats_count

print(numRescueBoats(people=[2,4],limit=5))

# 14378
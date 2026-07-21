'''
//////////// 2-SUM  ///////////////

nums = [2,7,11,15], target = 9
Output: [0,1]

Input:
nums = [3,2,4], target = 6
Output: [1,2]

'''

def two_sum(arr:list[int],target:int)->list[int]:

    d={}

    for i in range(len(arr)):
        num=target-arr[i]

        if num in d:
            return [d[num],i]        
        d[arr[i]]=i

# print(two_sum(arr=[3,2,4],target=6))


def three_sum(nums:list[int],target):
    '''
   [-2,-1,0,1,2]->[[-2,0,2], [-1,0,1]]

   [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]-[[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]

   [0]->[]

    '''

    a=sorted(nums)
    l=0
    n=len(nums)
    result=[]
    

    for i in range(len(nums)):
        if i>0 and a[i]==a[i-1]:
            continue
        l=i+1
        r=n-1

        while(l<r):
            total=a[i]+a[l]+a[r]
            if total==target:
                result.append([a[i],a[l],a[r]])

                l+=1
                r-=1

                while l<r and a[l]==a[l-1]:
                    l+=1
                
                while l<r and a[r]==a[r+1]:
                    r-=1
            elif total<target:
                l+=1
            else:
                r-=1
        
    return result

print(three_sum(nums= [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6],target=0))

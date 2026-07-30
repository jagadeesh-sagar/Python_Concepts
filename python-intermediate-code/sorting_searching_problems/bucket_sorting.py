
'''
bucket sorting algorithm (15/07/2026 , 3:10 pm)

Bucket Sort(o(n))

the main fund of these is to make groups(buckets) add elements to that specific group(bucket) based on sorting

at last sort all them buckets  (group is like bucket 1: 20-30 and bucket 2 : 30-40)

the specific logic below used and but its freq bucket same funda but we here used
 freq(count) as index and value(num) as value to find most freq nums  

 https://chatgpt.com/s/t_6a57568d0ad08191bcdb6f2d34b6adac

'''
from collections import Counter

def top_k(nums,k):
    freq=Counter(nums)

    buckets=[[] for _ in range(len(nums)+1)]

    for num,count in freq.items():
        buckets[count].append(num)

    result=[]
    
    for count in range(len(buckets)-1, 0, -1):
        for num in buckets[count]:
            result.append(num)

            if len(result) == k:
                return result

top_k(nums = [1,1,1,2,2,3],k=2)

'''
Pure bucket sorting example code

with integers
'''

def bucket_sort(arr, bucket_size=10):

    if len(arr)==0:
        return arr
    
    maximum=max(arr)
    minimum=min(arr)

    bucket_count=(maximum-minimum)//bucket_size+1

    buckets=[[] for _ in range(bucket_count)]

    for num in arr:
        index=(num-minimum)//bucket_size  # used to identify how far element goes from minimum bucket(num)
        buckets[index].append(num)


    reseult=[]

    for bucket in buckets:
        bucket.sort()
        reseult.extend(bucket)

    return reseult

print(bucket_sort(arr=[42, 32, 37, 52, 33, 47, 51]))


'''

Pure bucket sorting for floating numbers

'''

def bucket_sort_2(arr):

    n=len(arr)

    buckets=[[] for _ in range(n)]

    result=[]

    for num in arr:
        index=int(num*n)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()
        result.extend(bucket)

    return result


bucket_sort_2(arr=[0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68])
        


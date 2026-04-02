'''
Find the subarray with maximum sum (Kadane's Algorithm)
[-2,1,-3,4,-1,2,1,-5,4]->[4,-1,2,1]

'''

def max_sum(arr:list):

    max_so_far=arr[0] # global_maxima
    current_sum=arr[0]  # local_maxima
    start_index=0
    end_index=0

    for i in range(0,len(arr)):
        # current_sum=max(arr[i],current_sum+arr[i])
        if arr[i]>current_sum+arr[i]:
            current_sum=arr[i]
            start_index=i
        else:
            current_sum=current_sum+arr[i]
        # max_so_far=max(max_so_far,current_sum)
        if max_so_far<current_sum:
            max_so_far=current_sum
            end_index=i

    print(max_so_far,start_index,end_index)
       
max_sum(arr=[-2,1,-3,4,-1,2,1,-5,4])
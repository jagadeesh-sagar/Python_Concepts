'''
selction_sort

here we select the min value and moves them to left side


'''


def selction_sort(arr):
    n=len(arr)-1

    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
                arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

print(selction_sort(arr=[2,13,4,3,55,2,341,23,333]))

'''
# ── 1. Bubble sort ─────────────────────────────────────────────
# Idea: repeatedly swap adjacent pairs that are out of order(greater than comparision) 

is not used in real world

# O(n²) time, O(1) space. Only good for teaching.

'''

def bubble_sort(arr):
    n=len(arr)-1

    for i in range(n):
        for j in range(n-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

print(bubble_sort(arr=[2,13,4,3,55,2,341,23,333]))










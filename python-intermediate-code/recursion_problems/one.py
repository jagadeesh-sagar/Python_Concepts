'''
Power function - Calculate x^n efficiently using recursion

| Input           | Output |
| --------------- | ------ |
| `x = 2, n = 3`  | `8`    |
| `x = 5, n = 2`  | `25`   |
| `x = 2, n = 10` | `1024` |
| `x = 3, n = 0`  | `1`    |
| `x = 2, n = -2` | `0.25` |


'''

def power_recursion(x,n):

    if n==0:
       return 1
    if n<0:
        return 1/power_recursion(x,-n)  #making n positive
    
    return x*power_recursion(x,n-1)


print(power_recursion(2,4))
   
def power_recusion_2(x,n):  # instead O(n) it takes 0(log n) 

    '''
    2^10
→   (2^5)^2
→   ((2^2)^2 * 2)^2
    '''

    if n==0:
        return 1
    
    if n<0:
        return 1/power_recusion_2(x,-n)
    
    half=power_recusion_2(x,n//2)

    if n%2 ==0:
        return half*half
    else:
        return x*half*half
    
print(power_recusion_2(2,4))
# Generate Fibonacci sequence up to n terms
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 

def fibonnaci(num:int)->list[int]:

    fibonnaci_series=[]
    num1=0
    num2=1
    for i in range(1,num+1):

        if i==1:
            fibonnaci_series.append(num1)
            # return fibonnaci_series
        elif i==2:
            fibonnaci_series.append(num2)
        else :
            num3=num1+num2
            num1=num2
            num2=num3
            fibonnaci_series.append(num3)
    return fibonnaci_series

print(fibonnaci(23))

def fibonnaci_list(num:int)->list[int]:

    if num<=0: return []

    if num==1: return [0]

    result=[0,1]

    for _ in range(num-2):
        result.append(result[-1]+result[-2])
    
    return result

print(fibonnaci_list(23))

def fibonacci_gen(num:int)->any:
    '''   
     Generator:
        Doesn’t store 1 million numbers in memory
        Produces one at a time
    '''
    a,b=0,1
    for _ in range(num):
        yield a
        a,b=b,a+b

print(list(fibonacci_gen(23)))

import math

''' golden ratio formula '''
def fibonacci_fast(n: int) -> int:
    # We use n-1 because your list started at 0 (the 0th index)
    # Fibonacci sequence: 0, 1, 1, 2, 3, 5...
    
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    
    # Binet's Formula
    result = (phi**n - psi**n) / math.sqrt(5)
    
    # We round because floating point math can be slightly off (e.g., 12.99999)
    return round(result)

# To get the 23rd number (index 22 if starting at 0)
print(fibonacci_fast(22))


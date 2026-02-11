# Check if a number is prime
import math
def is_prime(num:int)->bool:
    
    if num<2:
        return False
    
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True
print(is_prime(23))

# prime number 2 to num
def prime_numbers(number:int)->list:
    prime_numbers=[]
    for num in range(2,number+1):
        prime=True
     
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                prime=False
                                #  if (is_prime(num)):
        if (prime):     
           prime_numbers.append(num)
    return prime_numbers

print(prime_numbers(58))

# Find factorial of a number (both iterative and recursive)

def factorial(num:int)->int:
    if num==0 or num==1:
        return 1
    else:
        return num*(factorial(num-1))

print(factorial(7))

def factorial_iteractive(nums:int)->int:

    result=1
    if nums==0:
        return result
    for num in range(2,nums+1):      # for num in range(nums-1,0,-1):
        result*=num
    return result

print(factorial_iteractive(6))

print(math.factorial(7))  # in-built
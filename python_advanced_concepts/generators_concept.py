def gen_values():
    yield 1
    yield 2
    yield 3

# genreated_values=gen_values()
# print(next(genreated_values))  unitl we use "next()" the programme pauses there (but not like "return" keyword that stops and returns ) 

for value in gen_values():  # next() is internally called
    print(value)

#///////////////////////////////// without generators////////////////////////////
def get_primes(start,end):
    primes=[]
    for num in range(start,end+1):
        if num<=2:
            continue
        is_prime=True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            primes.append(num)
    return primes
        
primes=get_primes(10,50)

# with generators

def gen_primes(start,end):
    for num in range(start,end+1):
        if num<=2:
            continue
        is_prime=True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            yield num 
            
for prime in gen_primes(10,50):
    print(prime)

# list(gen_primes(1,100))

list_primes=list(gen_primes(1,100))
print(list_primes)

''' use of genearator is that it uses less memory rather then storing sending after sometime it sends quickly which saves time in 
senarioes where i need output for further proccessing

- increaes modularity and reuse -> imagine adding logic like primes ending with 7 then in normal function i need to add logic to function and cant be reused for other primes logic/
but in genrator i can extra logic at the for loop level so that main code be reused again (production and consumption are seperateds)

-save memory,readbility,resuability,maintaninability

uses- use this only when u r prev iteration has no use


'''

'''
generators useful when we have to proccess a collection of items one at a time..
if we use list it takes O(n) memory but generaotrs take only O(1)

use cases like :
    reading a 10 GB log file,
    streaming API results, 
    feeding batches to a model, 
'''
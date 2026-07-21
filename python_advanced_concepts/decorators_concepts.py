'''
decorator is a special function that takes another functionas as a input, 
extends  or modifies its behavoiur without chaning the source code and returns a new function

"wrap a function with extra behavior without touching the function's code."

'''
from functools import wraps

# basic decorator

def decorator(func):
    
    @wraps  # save original functions metadata
    def wrapper(*args, **kwargs):
        print('before')

        result=func(*args, **kwargs)
        print('after')

        return result


    return wrapper

#usage

'''
this is how decorator works but with pythonic beauty '@'
'''

def hello():
    print('hello')
hello=decorator(hello)

# hello()

'''this is how can we write too and arguments are automatically passed'''

@decorator
def add(a, b):
    return a + b

print(add(2, 3))


'''
multiple decorators
'''

# @A
# @B 
# def hello():
#     pass
# # means
# hello = A(B(hello))

'''
B runs first
A runs second
'''

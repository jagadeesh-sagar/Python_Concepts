'''
■ 8.1 Reference counting

cpython tracks how many names point to a object in a field called "ob_refcnt"
if count becoms "0" then it frees the memory -no GC pause needed
=> use "sys.getrefcount(obj)" to inspect it (returns all names count +1 for itself too)

'''

# sys.getrefcount(obj)

import sys 

x=[]
y=x
z=[x]

print(sys.getrefcount(x))

'''
■ 8.2 Garbage collector — handling reference cycles

Reference counting cannot free circular references
=> two objects referencing each other .. neither can be reached soo they ref count is always >0 soo can'nt be removed

python cyclic garbage collectoer  runs peridocially in 3 generations(0=young,1=middle,2=old) to detect cyclics and break them

'''
import gc

class node:
    def __init__(self,n):
        self.n=n
        self.next=None
a=node(2)
b=node(3)

a.next=b
b.next=a  # CYCLE: both refcounts stay >= 1 after del

del a 
del b 

c=gc.collect()  # force cyclic GC to detect and free the cycle
# returns number of unreachable objects collected

print(c)  #2

# ///////////////////////////////
'''
■ 8.4 Integer caching and string interning
'''
# cpython pre-allocates int objects for -5 to 256 as cache to save memory

a=256 
b=256

print(a is b)  # True — same cached object

a=257
b=257

print(a is b,id(a),id(b))  # True in nrml (code optimization) but in REPL its False


'''
mutable defaults in function are dangerous because they are created once and used for all calls 

'''

'''
bug example
'''

def add_item(n,list1=[]):
    list1.append(n)
    return list1

print(add_item(1)) #[1]
print(add_item(2)) # [1,2]
print(add_item(3))  #[1,2,3]

'''
soo to avoid that use "None"
'''

def add_items(n,list1=None):

    if  list1 is None:
        list1=[]
    list1.append(n)
    return list1

print(add_items(1)) #[1]
print(add_items(2)) #[2]
print(add_items(3)) #[3]


'''


Interview Answer

Q: What is __del__ and why should it be avoided for resource cleanup?

A: __del__ is a destructor/finalizer that runs when an object is being garbage collected.
 It is not reliable because Python does not guarantee when it will execute, 
 especially with circular references or different Python implementations. 
 For deterministic cleanup of resources such as files, sockets, or database connections, 
 use context managers (with, __enter__, and __exit__) instead.'''
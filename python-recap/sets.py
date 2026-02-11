# Set stores unique, unordered, hashable elements
s={1,2,3}

s = set()   # ✅ correct
s = {}      # ❌ creates dict

se=set([1,2,3,4])
print(se)

print('/////////////////////////////////////////////////////////////////////////////////////////')
# set comprehension

squares={x*2 for x in range(10)}
print(squares)

print('/////////////////////////////////////////////////////////////////////////////////////////')
# ADDING elements (update) #O(1)

se.add(5)  # single element
se.update([6,7])  # multi elements
print(se)

print('/////////////////////////////////////////////////////////////////////////////////////////')
# Remove(Deletion) #O(1)

se.remove(7)  # throws error if not present
se.discard(6) # no exception
print(se)

a=se.difference(squares)  #{0, 2, 4, 6, 8, 10, 12, 14, 16, 18}-{1, 2, 3, 4, 5}={1, 3, 5}
print(a) #{1, 3, 5}  # temporary value
se.difference_update(squares)  # permanent value
print(se)

x=se.pop()  # removes random element
se.clear()   # removes all

print('/////////////////////////////////////////////////////////////////////////////////////////')

# 5️⃣ Membership testing (VERY FAST 🚀)

if '2' in s:
    print(s)   #O(1)


# ❌ Using mutable elements
# s = {[1, 2]}  # TypeError

print('/////////////////////////////////////////////////////////////////////////////////////////')

# ////////////////////////////////////////////////////////

'''set operations are O(n) higly optimized in c '''

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# union (|)
print(A|B)  # A.union(B)

# difference(-) A-B => B elements are removed from A
print(A-B)  #A.difference(B)

# symmetric diffrence (^)  common elements are removed
print(A^B)  # A.symmetric_difference(B)

# intersection (&) common elements
print(A&B)  #A.intersection(B)

print('/////////////////////////////////////////////////////////////////////////////////////////')

# /////////////////////////////////////////////////////////////////////

''' frozenset is immutable set
-> used for collections
-> used for sets inside sest
-> useful in caching ,keys

'''

s = set([1, 2, 3])
fs = frozenset([1, 2, 3])
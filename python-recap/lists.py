# Python lists are dynamic arrays because arrays provide O(1) indexing, refrences objects not values 
# better cache locality, and lower memory overhead compared to linked lists.
# deletion in python lists are slower becaues they are arrays soo all the array indexing should be changed but not linkedlist
# python append is always O(1) and delete at end also O(1) 
# deletion at start is O(n) 

girls=['anushka','preethi','pragathi','avneeth']

print(girls[-1])
print(girls[0])
print(girls[:2])
girls.append('pavitra') # at end
girls.insert(0,'kousthuba') 
print(girls)
print("______________________")

# /////////////////////////////////////
# List deletion
girls.remove('anushka')  # its slowest ,3rd fastest, raises valueError
del girls[:1] # deletes the element at the index and also slicing is possible,its fastest but no return
girls.pop(1)  # removes element at the index, returns the element ,2nd fastest

for girl in girls:
    print(girl)

# ////////////////////////////////////////////
#List compression

squares=[x**2 for x in range(1,10)]
print(squares)

#/////////////////////////////////////
#List copy
# in 2 ways 1.shallow copy,2.deep copy

# assignment(same object) its not a copy
a = [1, 2, 3]
b = a

b.append(4)
print(a)  # [1, 2, 3, 4]

#shallow copy (Copy the references only) not copies inner lists

# initilization
a = [1, 2, [3, 4]]

b = a.copy()
# or
b = list(a)
# or
b = a[:]

#example

a = [1, 2, [3, 4]]
b = a.copy()

b[0] = 100
print(a)  # [1, 2, [3, 4]]  ✅ unchanged

b[2][0] = 999
print(a)  # [1, 2, [999, 4]] ❌ changed   # inner list are shared but outer list are not shared so shallow copy

print('-------------------------------------------------------------------------')
# deep copy (copies everything recursively )
import copy

a=[1,2,[3,4]]
b=copy.deepcopy(a)

b[2][0]=999
print(a)   # not changed
print(b)

# ////////////////////////////////////////////////////////////////////////////////////////////
 # if in list

if 'pavitra' in girls:
    print(girls)

# /////////////////////////////////////////////////////////////////////////////////////////////
# sort()=>permenantly sorts the list, sorted()=> temporarly sorts the list

users=['zebra','Zebra','jagadeesh','anushka']
users.sort()  # output: ['Zebra', 'anushka', 'jagadeesh', 'zebra']  case sentitive 
# users.sort(reverse=True)
print(users)  #uppercase have asci values comes before lowercase


names = ['val', 'bob', 'mia', 'ron', 'ned']
print(sorted(names)) # temporoary
print(sorted(names,reverse=True))
print(names)

# /////////////////////////////////////////////////////////////////////////////////
# statistics

ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]

oldest=max(ages)
youngest=min(ages)

total_ages=sum(ages)

print(oldest,youngest,total_ages)


friends:str=['jagadeesh','anushka sen','PAvitra','PRETTY']

new_friends=[friend.upper() for friend in friends]
print(new_friends)

'''❌ Modifying dict while iterating'''

'''dict keys are acutally hased that why its
 time complexity for inseret,del,lookups are of O(1)

 keys are implemted using tuple
'''

captical_city={'telangana':'hyderabad','andhrapradesh':"amravathi",'tamilnadu':'chennai'}

print(captical_city.get('tamilnadu'))

print(captical_city['tamilnadu'])
captical_city['karnataka']='bengaluru'
print(captical_city)

print('--------------------------')
for state,city in captical_city.items():
    print(state,city)

print('--------------------------')

for state,city in sorted(captical_city.items(),reverse=True ):
    print(state,city)
  
print('--------------------------')

for state in captical_city.keys():
    print(state)

print('--------------------------')
for city in captical_city.values():
    print(city)

# ////////////////////////////////////////////////////////////////

# deletion

values={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8}

if 'one' in values.keys():
    del values['one']   # del does not return deleted values just like in list 
print(values)  # ⚡ O(1)

deleted_value=values.pop('two')  # returns removed value not key , here : 2
print(deleted_value) # ⚡ O(1)

deleted_last_value=values.popitem()  # removes last added item LIFO
print(deleted_last_value)  # output ('eight', 8) 

all_delete=values.clear()  # deletes everything O(n)  returns None
print(all_delete)

# if we want to delete multiple keys based on logic in iteration

'''if we dont copy into list and it throws error becoz 
the dict size after 1st iteration delete decreses '''

for k in list(captical_city.keys()): 
    print(k)
    del captical_city[k]

print(captical_city)

# ///////////////////////////////////////////////////////////////////////

# dict compression

d={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
c={k:v for k,v in d.items() if k!='b'}  # very useful for filtering
print(c)
print('---------')


# ////////////////////////////////////////////////////////////////////

# dict addition
# if we need to add multiple values

dicti={'a':1}
dicti.update({'b':2,'c':3})

print(dicti)

# same value for multiple keys
keys=['a','b','c','d']
dkeys=dict.fromkeys(keys,0)

print(dkeys)

# merging two dict

dict1={'a':1,'b':2,'c':3}
dict2={'d':4,'e':5,'f':6}

dict3=dict1|dict2

print(dict3)

# ///////////////////////////////////////////////////////////////////////////////////////////
user = [
{
'last': 'fermi',
'first': 'enrico',
'username': 'efermi',
},
{
'last': 'curie',
'first': 'marie',
'username': 'mcurie',
},
]
# /////////////////////////////////////////////////////////////////
for use in user:
    for key,value in use.items():
        print(key,value)
# ////////////////////////////////////////////////////////////////////////

"""The zip() function matches each item in one list to each
item in a second list. It can be used to make a dictionary
from two lists"""

group_1 = ['kai', 'abe', 'ada', 'gus', 'zoe']
group_2 = ['jen', 'eva', 'dan', 'isa', 'meg']

zipping={name:last_name for name, last_name in zip(group_1,group_2)}
print(zipping)

# /////////////////////////////////
aliens = []
# Make a million green aliens, worth 5 points
#
# each. Have them all start in one row.
for alien_num in range(1000000):
    new_alien = {
    'color': 'green',
    'points': 5,
    'x': 20 * alien_num,
    'y': 0
    }
    aliens.append(new_alien)
# Prove the list contains a million aliens.
num_aliens = len(aliens)
print("Number of aliens created:")
print(num_aliens)
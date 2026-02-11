'''shallow copy and deep copy concepts are same as they are in list but tuple are immutable soo shallow copy returns the same object .
 while deepcopy only matter when there is mutable objects inside the tuple like list inside the tuple'''

girls=('anushka','pavitra','tamana','aveenthi')
crushs=['anushka','preethi','pragathi','avneethi']

print(girls[0])
print(girls)
# girls.remove('anushka')  does not work becauce tuple is immutable
a=tuple(crushs) # conveting from list to tuple  , shallow copy is just assignment but actually no use memory waste

crushs.append('aish')

print(a)
print(crushs)

# nested objects

t1=(1,2,3,[4,5]) # here [4,5] are mutable .. deepcopy useful only here when we are copying the tuple

# conditions

if 'anushka' in girls:
    print('hello')

    
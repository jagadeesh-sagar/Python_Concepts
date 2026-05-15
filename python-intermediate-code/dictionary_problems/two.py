'''
Find top K frequent elements in a list

[1,1,1,2,2,3] k=2 -> [1,2]

[4,4,4,6,6,1,1,1,1] k=2 -> [1,4]

[7,7,8,8,8,9] k=1 -> [8]

'''

def k_frequent(list1:list[int],k:int)->list[int]:

    d={}

    for i in list1:
        d[i]=d.get(i,0)+1
    
    result=sorted(d.keys(), key=lambda x:d[x] ,reverse=True)

    return result[:k]

# print(k_frequent(list1=[4,4,4,6,6,1,1,1,1],k=2))


'''
Longest consecutive sequence using hash map

we solved this using list in list_problems/one.py

[100,4,200,1,3,2]-> 4
[0,3,7,2,5,8,4,6,0,1]->9
[9,1,4,7,3,-1,0,5,8,-1,6]->7

'''

def long_consecutive(list1:list[int])->int:

    d={}
    setlist=set(list1)

    for i in setlist:

        if i-1 not in setlist:
            num=i

            while num in setlist:
           
                d[i]=d.get(i,0)+1
                num=num+1
              
    result=sorted(d.values(),reverse=True)     
    return result[0]

print(long_consecutive(list1=[100,4,200,1,3,2]))
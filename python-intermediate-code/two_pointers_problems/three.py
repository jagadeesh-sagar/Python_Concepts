'''
Find pair with given difference - Find two numbers with difference k

'''

def k_difference(list1:list,k:int)->bool:
    if k==0 and len(list1)==len(set(list1)) or len(list1)<2:
        return False
    elif k==0:
        return True
    
    seen=set(list1)  # used set() otherwise with if-conditon it will o(n2) now o(n)

    for num in list1:
        s=num+k

        if s in seen:
            print(num,s)

print(k_difference(list1=[8, 12, 16, 4, 0, 20],k=4))



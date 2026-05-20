'''
Find the majority element - Element appearing more than n/2 times
[3,2,3]  => 3

[2,2,1,1,1,2,2] => 2

[1] =>1

we can also solve using dict but with o(n) and space o(n)

'''

def majority_sorting(list1:list[int]):  # o(n log n)  and o(1)
    list1.sort()

    n=len(list1)//2
    print(list1[n])

# majority_sorting(list1=[5,5,5,2,2])


def Boyer_Moore_Majority_Vote_Algorithm(list1): # 0(n)  and o(1)

    candidate=0
    count=0

    for i in list1:

        if count==0:
         candidate=i

        if i==candidate:
           count+=1
        else:
            count-=1

    print(candidate)


# Boyer_Moore_Majority_Vote_Algorithm(list1=[3,2,3])


'''
Product of array except self - [1,2,3,4] → [24,12,8,6] (without using division)

[2,3,4,5] => [60,40,30,24]

[1,1,1,1] => [1,1,1,1]

[5,2,1] => [2,5,10]


Index	Product of remaining elements
0	       2 x 3 x 4 = 24
1          1 x 3 x 4 = 12 
.....

'''

def product(list1:list[int]):
   product=1

   for i in list1:
      product=product*i

   for i in range(len(list1)):
      list1[i]=product//list1[i]

   print(list1)

# product(list1=[4,3])


def zero_product(list1: list[int]):    # works with zeros too
   suffix_product=1
   prefix_product=1


   n=len(list1)
   result=[1]*n

   for i in range(n):
      result[i]=prefix_product
      prefix_product=prefix_product*list1[i]

   for i in range(n-1,-1,-1):
     
      result[i]=result[i]*suffix_product 
      suffix_product=suffix_product*list1[i]   

   print(result)


zero_product(list1=[1,2,3,0])
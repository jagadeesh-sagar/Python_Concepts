# Check if a number is Armstrong number (153 = 1³ + 5³ + 3³)
def armstrong(num:int)->int:  # its faster but messy and takes more space(list)
    arm_num=[]
    number=num
    digits=len(str(num))
    for i in range(digits):
      digit=number%10
      rev=number//10
      arm_num.append(digit**digits)
      number=rev
    if sum(arm_num)==num:
       print('armstrong')
    else:
        print('not armstrong')

def arm_strong(num:int)->int: # string conversion takes time
   num_str=str(num)
   power=len(num_str)

   total=sum(int(digit)** power for digit in num_str)
   return total

# Find sum of digits of a number
def sum_digits(num:int)->int:
   num_str=str(num)
   total=sum(int(digit) for digit in num_str)
   return total

# Reverse a number
def rev_number(num:int)->int:
   num_str=str(num)
   rev_num=int(num_str[::-1])
   print(rev_num)

def rev_number_maths(num:int)->int:
   rev_num=0
   while(num>0):
      digit=num%10
      rev_num=rev_num*10+digit
      num=num//10
   return rev_num

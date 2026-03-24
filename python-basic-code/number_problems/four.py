# palindrome in numbers

num=int(input('enter a number:'))
rev=0
temp=num

while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10

if temp==rev:
    print('palindrome')
else:
    print('not palindrome')
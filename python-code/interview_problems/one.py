def FizzBuzz(num:int)->None:
    for i in range(1,num+1):
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0:
            print('Fizz')
        elif i%5==0:
            print('Buzz')
        else:
            print(i)

# FizzBuzz(100)

# i%15==0 then divides by both 5,3


def FizzBuzz_string(num:int)->None:
    for i in range(1,num+1):
        output=''

        if i%3==0:
            output+='Fizz'
        if i%5==0:
            output+="Buzz"
        print(output if output else i)

FizzBuzz_string(100)
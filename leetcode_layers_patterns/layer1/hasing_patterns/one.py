'''
LC 166 — Fraction to Recurring Decimal 

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

Note that if the fraction can be represented as a finite length string, you must return it.

 

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"

'''

'''
method 1:
# 10^3=1 mod 33
# 10^n≡1(mod D(denominator)) it can be written as ..Try n=1: 10^1 - 1 = 9 (Not a multiple of 333)
# n=3 10^3-1=999(multiple of 333)
#  the 10^n-1 value should give remainder 0 for denominator the that n is period where repeating char exist

link :https://math.stackexchange.com/questions/377683/length-of-period-of-decimal-expansion-of-a-fraction
link: https://gemini.google.com/app/e49c1de5034a0709?hl=en-IN

10^n -1 = multiple of D ( then n is period of repeating)

its much harder but lets try later
'''

'''
method 2 

when the remainder starts repeating thats repeating part start to end 

'''

def fractionToDecimal(numerator,denominator):
    '''
    this solution has issue of bad flow and floating precision issues
    '''

    d={}
    i=1
    print(numerator/denominator)
    rem=numerator%denominator
    num=numerator

    def prime_factors(den):
        count_2=0
        count_5=0
        d=2

        while d*d<=den:
            while den%d==0:
                if d==2:
                    count_2+=1
                if d==5:
                    count_5+=1
                
                den//=d
            d+=1

        if den>1:
            if den==2:
                count_2+=1
            if den==3:
                count_5+=1  
        return max(count_5,count_2)
    
    while(1):
     
        print(rem,numerator,denominator,i)
        if rem==0:
            return f'{str(num/denominator)[:2]}{str(num/denominator)[2:]}' if i!=1 else str(num//denominator)
        if i!=1:
            if d.get(rem):
                start=d[rem]
                print(start,i,'hi')
                if denominator%2==0 or denominator%5==0:
                    c=prime_factors(denominator)
                    print(c,i,'hello')
                    return f'{str(num/denominator)[:2+c]}({str(num/denominator)[c+2:i+1]})'
                else:
                    return  f'{str(num/denominator)[:2]}({str(num/denominator)[start:i]})'
            else:
                  d[rem]=i

        if rem<denominator: # this condition is useless becoz its always lees
            numerator=rem*10

        rem=numerator%denominator
        
        i=i+1
    
# print(fractionToDecimal(numerator=1,denominator=19))

def fractionToDecimal2(numerator,denominator):

    if numerator ==0:
        return "0"
    
    num=abs(numerator)
    den=abs(denominator)

    res=[]

    if (numerator/denominator)<0:
        res.append('-')

    # adding the integer part
    res.append(str(num//den))
    remainder=num%den

    if remainder!=0: # adding "."
      res.append('.')
  
    seen={}
    while remainder!=0:
        if remainder in seen:
            idx=seen[remainder]  #cycle started at this index
            res.insert(idx,"(")
            res.append(')')
            break

        seen[remainder]=len(res)

        remainder=remainder*10
        res.append(str(remainder//den))
        remainder=remainder%den

    return "".join(res)

# print(fractionToDecimal2(numerator=-7,denominator=-12))


def fractionDecimal3(numerator,denominator):
    from decimal import Decimal ,getcontext

    getcontext().prec=50
    if numerator ==0:
        return "0"
    
    num=abs(numerator)
    den=abs(denominator)
    res=str(Decimal(num)/Decimal(den))
    print(res)

    if (numerator/denominator)<0:
        result='-'
    else:
        result=''
 
    n=1
    def prime_factors(den):
        count_2=0
        count_5=0
        d=2
        factor=None
        factors=[]
        seen={2,5}

        while d*d<=den:
            while den%d==0:
                factors.append(d)
                if d==2:
                    count_2+=1
                if d==5:
                    count_5+=1
                if d not in seen:
                    factor=d                
                den//=d
            d+=1

        if den>1:
            if den==2:
                count_2+=1
            if den==3:
                count_5+=1  
            if den not in seen:
                    factor=d
            factors.append(den)
        return max(count_5,count_2),1 if factor is None else factor
    
    if den%2==0 or den%5==0:
        c,factor=prime_factors(den)
    if (num%den)==0:
        return result+str(num//den)
    
    while(1):
        number=(10**n)-1 

        if den%2==0 or den%5==0:
         
            if number%factor==0:
                result+=f'{res[:2]}{res[2:2+c]}({res[c+2:c+2+n]})' if factor != 1 else f'{res[:2]}{res[2:2+c]}{res[c+2:c+2+n]}'
                return result
            
        elif number%den==0:
    
            result+=f'{res[:2]}({res[2:2+n]})'
            return result
            
        n+=1
   

print(fractionDecimal3(numerator=89,denominator=270))

# 10^3=1 mod 33
# 10^n≡1(mod D(denominator)) it can be written as ..Try n=1: 10^1 - 1 = 9 (Not a multiple of 333)
# n=3 10^3-1=999(multiple of 333)
#  the 10^n-1 value should give remainder 0 for denominator the that n is period where repeating char exist

# print(abs(-3))


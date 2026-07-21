'''
Class method is a method that recives a cls itself as first argument instead of an instance (self)

this cls method is called as alternative constructor (like def __init__)

uses:
    1.we can direclty modify the cls level data not object-level data(look at second example)
    2.in our pblm we need year,month,day for cls init constructor but we are calling cls with string we dont have datetime
    so it throws error (we need to call this Date(2020,04,12) but we generally from even db we get string Date("2026-04-12")
    so we use this method to implemnt logic to retrive the necessary values and pass that to same cls as attributes for __init__
    3. not creates any object instance
    )

'''

class Date:

    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    @classmethod
    def convet_to_date(cls,s):
        y,m,d=map(int,s.split("-"))
        return cls(y,m,d)
    
    def valid_leap_year(self):
        return self.year%4==0 and (self.year % 100 !=0 or self.year%400==0)
    
    @staticmethod  # same like cls method no instance acts a utility helper method
    def is_leap(year):
        return year % 4 == 0 and (
            year % 100 != 0 or year % 400 == 0
        )

date=Date.convet_to_date("2026-06-2")
print(date.valid_leap_year())
print(date.is_leap(2026))  # static method call


'''
2 example
'''

class Employee:

    company = "Google"

    @classmethod
    def change_company(cls, name):
        cls.company = name

    def cat(self):
        return self.company
    

Employee.change_company("india")
e2=Employee()
print(e2.cat())


'''
__slots__
by default all the attributes in cls are stored in __dict__ but they are expensive as they and flexible
soo replace them with slots that are built in C and with fixed size cant increase dynamically
'''


import sys

class SlotCheck:
    __slots__=('year')  # only these are allowed

    def __init__(self,year):
        self.year=year

class NormalCheck:
    def __init__(self,year):
        self.year=year

n=NormalCheck(2020)
s=SlotCheck(2027)

print(sys.getsizeof(s),sys.getsizeof(n))  # 40 , 48 
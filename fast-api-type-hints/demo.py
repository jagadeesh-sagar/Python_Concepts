''' type-hint(type annotations) helps in but python does not force during runtime
1. documentation -> acts as a doc
2. auto completion in code editors/ide
3. error checking 
'''

def greetings(firstname:str,secondname:str)->str:
    full_name=firstname.title()+' '+secondname.title()
    return full_name

full_name=greetings('jagadeesh','sagar')
print(full_name)

print('///////////////////////////////////////////////////////////////////////////////////////////////////////')

def proces_items(items:list[int,int,str]):  #Those internal types in the square brackets are called "type parameters".
    for item in items:
        print(item)

items=[1,2,'jaggu']
proces_items(items)

print('///////////////////////////////////////////////////////////////////////////////////////////////////////')
    
from typing import Union,Optional

# def say_hi(items:Union[str,None]): ->python 3.9+
# def say_hi(name: Optional[str] = None):

def say_hi(items:str|None):  #->python 3.10+
    if items is not None:
        print(items)

say_hi('anushka')

print('///////////////////////////////////////////////////////////////////////////////////////////////////////')

# classes as types

'''Notice that this means "one_person is an instance of the class Person".

It doesn't mean "one_person is the class called Person".'''

class Person:
    def __init__(self,name:str):
       self.name=name

def greet_person(one_person:Person):
    return one_person.name

c=greet_person(Person('hello'))
print(c)

print('///////////////////////////////////////////////////////////////////////////////////////////////////////')

'''
Pydantic models automatically:

Validate data types
Convert/coerce compatible types
Provide default values
Generate helpful error messages
'''

'''
Why No __init__?
Pydantic uses metaclass magic! When you inherit from BaseModel, it:

Automatically generates __init__ based on your type annotations
Adds validation logic before setting attributes
Handles type coercion intelligently
'''

'''
useful in serilization too  (model_dump_json())
'''

from datetime import datetime

from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str='jagadeesh'
    signup_ts:datetime|None
    friends:list[int]=[]

external_data={
    "id":"123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

user=User(**external_data)
print(user.model_dump_json(exclude_defaults=False,indent=2))


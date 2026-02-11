class Person:
  def __init__(self ,name,age):
    self.name=name
    self.age=age
  
  def greet(self):
    print(f"hello, my name is {self.name} and my age is {self.age}")

person1=Person('jaggu',22)
person1.greet()
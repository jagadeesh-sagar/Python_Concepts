# name='Jaggu'
# age=10

# print(type(name))
# print(type(age))
# class Dog:
#   def __init__(self,name,breed,owner):
#     self.name=name
#     self.breed=breed
#     self.owner=owner

#   def __str__(self):
#     return f"the breed is {self.breed}"

#   def bark(self):
#     print("the Dog is barking")

# class Owner (Dog) :
#   def __init__(self,name, breed, owner, address,phone_number):
#     super().__init__(name, breed, owner)
#     self.address=address
#     self.phone_number=phone_number

# owner1=Owner('oreo','golden',"jaggu",'wanaparthy',12345)
# # dog1=Dog('oreo','golden',"jaggu")
# # dog1.bark()
# # print(dog1.owner.address)
# # print(dog1.owner.owner
# # )
# owner1.bark()

class Dog:
  def __init__(self,name,breed,owner):
    self.name=name
    self.breed=breed
    self.owner=owner

  def __str__(self):
    return f"the breed is {self.breed}"

  def bark(self):
    print("the Dog is barking")

class Owner:
  def __init__(self,owner,address,phone_number):
    self.owner=owner
    self.address=address
    self.phone_number=phone_number
    

owner1=Owner('jaggu','wanaparthy',12345)
dog1=Dog('oreo','golden',owner1)
dog1.bark()
print(dog1.owner.address)
print(dog1)

# ///////////////////////////////////////////////////////////////
print('////////////////////////////////////////////////////////////////////////////')
class Student:
  def __init__(self,name,age,college):
    self.names=name
    self.age=age
    self.college=college

  def __str__(self):
    return f'the student name is {self.names}'
  
  def detail(self):
    print(f'the student name is {self.names} and is {self.age} old from {self.college}')

Student1=Student('jagadeesh',17,'smec')
Student1.detail()

class College_students(Student):
  def __init__(self,names,age,college,section,cr):
    super().__init__(names,age,college)
    self.section=section
    self.cr=cr

  def __str__(self):
    return super().__str__()
  
  def full_details(self):
      print(f'the student name is {self.names} and is {self.age} old from {self.college} section {self.section} and cr is {self.cr} ')
      
cs=College_students('jagadeesh',21,'smec','b','raja')

cs.full_details()
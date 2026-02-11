  # def say_hi_to_user(self,user):
  #    print(
  #       f"Sending message to {user.username}: Hi {user.username}, it's {self.username}")


# code starts from here
# Accessing and Modifying Data:
# 1. The traditional way: make the data private and use getters and setters:
from datetime import datetime

class User:
  def __init__(self,username,email,password): #protected is most widely used
     self.username=username # single undersocre "_" represnts  protected(can access outside class) .double underscore "__" represents private attributes (cant access outside of class)
     self._email=email   # protected attribute access modifers are defined with "_" in python unlike in java with "private" keyword
     self.password=password # use double "__" to make them absolute private (u cant acces in class object)(Name Mangled proccess)
  
  '''old way'''
  
  def get_email(self):# it can be achived normally but using setters and getters help us to have better manipualtion and proccessing of attributes
     print(f"Email accessed at {datetime.now()}")
     return self._email # exmaple allows only admins with authorization to view email but not everyone
  
  def set_email(self,new_email): #setters and getters helps us to not to do any stupid operations on important data in other parts of programme by enforcing logic in setters and getters
     if "@" in new_email: #example checking that username is not taken by looking into database or password strength
        self._email=new_email

  '''new way '''
#   @property
#   def email(self):# it can be achived normally but using setters and getters help us to have better manipualtion and proccessing of attributes
#      print(f"Email accessed at {datetime.now()}")
#      return self._email # exmaple allows only admins with authorization to view email but not everyone
#   @email.setter
#   def email(self,new_email): #setters and getters helps us to not to do any stupid operations on important data in other parts of programme by enforcing logic in setters and getters
#      if "@" in new_email: #example checking that username is not taken by looking into database or password strength
#         self._email=new_email
  
  # def get_email(self):
  #    return self._email  #can be used inside the class itself if u use in class object python wont throw error but it's not allowed it's a "convention"
  #print(user1._email) #but it's is bad practice its convention



user1=User('jagadeesh',"Jaggu42@gmail.com","1234")


print(user1.get_email())
user1.set_email("jaggu1234gmail.com")
print(user1.get_email())
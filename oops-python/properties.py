from datetime import datetime

class User:
  def __init__(self,username,email,password): 
      self.username=username
      self._email=email
      self.password=password

  @property # if we suddenly decided to change some attribute to private then in outside cls (i.e objects) we have to write set or get but in propeties you keep the attributes same as it is for so it easy to create private attributes in propety
  def email(self):# it is getter property
      print('Email received')
      return self._email

  @email.setter # the setter should start with attribute name 
  def email(self,new_email):
     if '@' in new_email:
        self._email=new_email
      
user1=User('jagadeesh','jagadeeshsagar40@gmail.com',12345)

print(user1.email)
user1.email='jagadeeshsagar650@gmail.com' #this throws error if setter property is not created
print(user1.email)
 
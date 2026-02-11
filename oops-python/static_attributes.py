# static attributes

''' A static attribute (is also called as class attributes) 
is an attribute that belongs to class itself, not to any specific instance of the class'''

class User:
  user_count=0 #static attributes . it is shared by all class objects

  def __init__(self,username,email):
    self.username=username #instance attribute
    self.email=email #only specific to a particular class object
    User.user_count +=1

  def display_user(self):
    print(f'Username: {self.username}, Email: {self.email}')
  
user1=User('jagadeesh','jagadeeshsagar40@gmail.com')   # user1,user2 are instances
user2=User('jagadeesh','jagadeeshsagar40@gmail.com')
# user1.display_user()
print(User.user_count)
print(user1.user_count)
print(user2.user_count)

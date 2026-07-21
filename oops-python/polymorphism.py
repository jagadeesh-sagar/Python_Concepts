# polymorphism

# The word polymorphism is derived from greek , and means "having multiple forms:"

#poly =many , Morph=forms

class Vehicle:
  def __init__(self,brand,model,year):
    self.brand=brand
    self.model=model
    self.year=year

  def start(self):
    print("vehicle is starting")

  def stop(self):
    print("vehicle is stopping")

  
class Car(Vehicle):
  def __init__(self,brand,model,year,number_of_doors,number_of_wheels):
    super().__init__(brand,model,year)
    self.number_of_doors=number_of_doors
    self.number_of_wheels=number_of_wheels


  def start(self):
    print("car is starting")

  def stop(self):
    print("car is stopping")


class Motorcycle(Vehicle):
  def __init__(self,brand,model,year):
    super().__init__(brand,model,year)
    self.brand=brand
    self.model=model
    self.year=year
 
  def start(self):
    print("bike is starting")

  def stop(self):
    print("bike is stopping")

vehicles:list[Vehicle]=[  #it it called type hinting then we no need that isinstance
  Car("ford","focus",2000,4,6),
  Motorcycle("honds","scoopy",2018)
]

print(vehicles[0].brand)

for vehicle in vehicles:
  # if isinstance(vehicle ,Vehicle):
     print(f"inspecting {vehicle.brand} {vehicle.year} ({type(vehicle).__name__})")
     vehicle.start()
     vehicle.stop()
  # else:
  #    raise Exception('Object is invalid ')


# for vehicle in vehicles:
#    if isinstance(vehicle,Car):
#     #  print(type(vehicle).__name__)
#     #  print(type(vehicle))

#      print(f"insceptinmg {vehicle.brand} {vehicle.year}")

#    elif isinstance(vehicle,Motorcycle):
#      print(f"inspecting {vehicle.brand} {vehicle.year}")
#      vehicle.start_bike()
#      vehicle.stop_bike()

#    else:
#      raise Exception('Object is invalid ')


'''

Polymorphism is the ability of different objects to respond to the same method call in their own way. 
It allows one interface to represent many different forms.
'''

'''
Example 3: Built-in Polymorphism

The same function works on different types.

print(len("hello"))
print(len([1, 2, 3]))
print(len((10, 20, 30, 40)))
'''
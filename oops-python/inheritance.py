# Inheritance

# inheritance is fundamental concept in oops that invloves creating new classes (subclasses or derived classes) based on existing clases(super class or base clase)

# -A Car is a vehicle
# -A Bike is a vehicle

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
  def __init__(self, brand, model, year,number_of_doors,number_of_wheels):
    super().__init__(brand, model, year)
    self.number_of_doors=number_of_doors
    self.number_of_wheels=number_of_wheels

class Bike(Vehicle):
  def __init__(self, brand, model, year,number_of_wheels):
    super().__init__(brand, model, year)
    self.number_of_wheels=number_of_wheels



# class Bike(Car):
#   def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
#     super().__init__(brand, model, year, number_of_doors, number_of_wheels)
 

car=Car("Ford","focus",2000,4,5)
bike=Bike("honda","focscopyus",2018,2)
print(car.__dict__)
print(bike.__dict__)
print(bike.start())
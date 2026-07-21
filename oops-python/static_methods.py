# Static Methods

# A Static method in python is a method that belongs to the class itself rather than any instance of the class.

# To define a static method, we use the '@staticmethod' decorator

'''
When SHOULD You Use Static Methods?

✔ Validation
✔ Helper functions
✔ Business rules
✔ Logic related to class but independent of objects

'''

# Static vs Instane Method Example

class BankAccount:
  MIN_BALANCE=100

  def __init__(self,owner,balance=0): 
    self.owner=owner
    self._balance=balance

  def deposit(self,amount):
    if self._is_valid_amount(amount):
      self._balance+=amount
      self.__log_transaction("deposit",amount)
    else:
      print('Deposit amount must be positive.')
  
  def _is_valid_amount(self,amount): # it is protected method accessd in subclasses and with in class using "self." keyword
    return amount>0

  def __log_transaction(self,transaction_type,amount): # it is private method not accessed outside of class even with in subclasses
    print(f"Logging {transaction_type} of ${amount}. New balance: ${self._balance}")
  
  @staticmethod #it is stored in the class itself and only one copy but not with instance methods 
  def is_valid_interest_rate(rate): # it is not interacting with any class instance
    return 0<= rate<=5
  
  # print(BankAccount.is_valid_interest_rate(/3))  this are '__' methods are allowed only inside cls
  # print(BankAccount._is_valid_amount(20))

account=BankAccount("Alice",500)
account.deposit(200)
# account.__log_transaction('deposit',129) # throws attribute error (explanation is in below)

'''
throws error ->Private methods don’t throw errors due to access restriction.
They raise AttributeError because Python renames them using name mangling.(no explict methods in python)

account._BankAccount__log_transaction('deposit',129) # its correct by the way but not recommended

'''

if (BankAccount.is_valid_interest_rate(7)):
  print(f'this is valid')
else:
  print(f'not valid interest')


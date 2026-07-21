# Encapsulation
# it provides high level of abstraction by hiding the internal implementation using methods by only providing the method names to users

# Encapsulation is the process of hiding an object's internal state and allowing controlled access to it through methods or properties.

class BankAccount:
    def __init__(self):
      self._balance=0.0
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self,amount):
        if amount<=0:
          raise ValueError('Deposit amount must be positive')
        self._balance+=amount

    def withdraw(self,amount):
      if amount<=0:
          raise ValueError('withdraw amount must be positive.')
      if amount>=self._balance:
          raise ValueError("insufficent funds.")
      self._balance-=amount

        
account=BankAccount()
# account.balance=-1
account.deposit(1.99)
print(account.balance)

account.withdraw(1)
account.withdraw(100)

print(account.balance)

from class_practice425 import BankAccount

user1 = BankAccount("13579", "246810", "Pete", 100.00)
user2 = BankAccount("54321", "98765", "Jack", 200.00)

user1.withdraw(100.00)
user2.deposit(100.00)

print(user1.accountName, "$ ", user1.balance)
print(user2.accountName, "$ ", user2.balance)

print(user1)
print(user2)
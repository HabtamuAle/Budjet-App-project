import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")  #create new category called food
food.deposit(1000, "initial deposit")  #putting 1000 (dollars?) into the acc
food.withdraw(10.15, "groceries")  #groceries is the desc
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())  #printing balance of the food acc
clothing = budget.Category("Clothing")  #create new category called clothing
food.transfer(50, clothing)  #transfering money from food into clothing
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")  #create third category
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)  #display statement
print(clothing)

print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
main(module='test_module', exit=False)

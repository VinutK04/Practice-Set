# Predefined Dectionary 
expenses ={"Person1":100, "Person2":200, "Person3":300, "Person4":00, "Person5":00 }
total_amt = 0

# to take the input from the user
# n = int(input("Enter the number of people in the group : "))
# for i in range(n):
#     key = input("Enter Name of a person : ")
#     value = int(input("Enter the amount spent : "))
#     expenses[key] = value

print(expenses)

for amount in expenses.values():
    total_amt += amount
    cost_per_head = total_amt / len(expenses)

print(total_amt)
print(cost_per_head)

for key in expenses:
    returns = expenses[key] - cost_per_head
    if returns < 0 :
        print(f"{key} shoud give {returns}")
    else:
        print(f"{key} shoud get {returns}")
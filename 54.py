# Conditional Statements
# Clever If/Ternary Operator

# <var> = (false_val, true_val) [<condition>]

age = int(input("age: "))
vote = ("yes", "no") [age < 18]

sal = float(input("salary: "))
tax = sal*(0.1, 0.2) [sal > 50000]
print(tax)
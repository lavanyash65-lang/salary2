import sys

if len(sys.argv) == 2:
    salary = sys.argv[1]
else:
    salary = "50000"

salary = eval(salary)
bonus = salary * 0.10
print("Bonus:", bonus)
print("Total Salary:", salary + bonus)

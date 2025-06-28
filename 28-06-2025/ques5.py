//Budget Tracking Application
expenses = {'Food': [100, 150], 'Transportation': [50, 75], 'Entertainment': [75, 100]}
total_expenses = {category: sum(amounts) for category, amounts in expenses.items()}
print("Total Expenses:", total_expenses)

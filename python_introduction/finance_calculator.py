monthly_income = input("Enter your monthly income:")
monthly_expense = input("Enter your total monthly expense:")
monthly_income = int(monthly_income)
monthly_expense = int(monthly_expense)
monthly_saving = float(monthly_income) - float(monthly_expense)
projected_savings = monthly_saving * 12 + (monthly_saving * 12 * 0.05)

print("Your monthly savings are $", monthly_saving)

print("Projected savings after one year, with interest, is: $", projected_savings)

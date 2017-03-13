__author__ = 'Tom Stanley'
print("Electricity Bill Estimator")
cent_per_kwh = float(input("Enter cents per kWh:")) / 100
# Dividing by 100 to turn it into a decimal for calculation.
daily_use_kwh = float(input("Enter daily use in kWh:"))
billing_days = int(input("Enter number of billing days:"))
estimated_bill = float((billing_days * daily_use_kwh) * cent_per_kwh)
print('\nEstimated bill : $ {:.2f}'.format(estimated_bill))





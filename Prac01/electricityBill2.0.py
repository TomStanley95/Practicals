__author__ = 'Tom Stanley'
cent_per_kwh = float(0)
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
print("Electricity Bill Estimator 2.0")
tariff_choice = int(input("Which tariff? 11 or 31:"))
if tariff_choice == 11:
    cent_per_kwh = TARIFF_11
else:
    cent_per_kwh = TARIFF_31
daily_use_kwh = float(input("Enter daily use in kWh:"))
billing_days = int(input("Enter number of billing days:"))
estimated_bill = float((billing_days * daily_use_kwh) * cent_per_kwh)
print('\nEstimated bill : $ {:.2f}'.format(estimated_bill))
# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
current_month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.0


while principal >= extra_payment:
    current_month = current_month + 1
    principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment  
    
    if current_month >= extra_payment_start_month and current_month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    else:
        pass
    print(current_month, round(total_paid, 2), round(principal, 2))

current_month = current_month + 1
principal = principal * (1 + rate/12)
total_paid = total_paid + principal
principal = 0
print(current_month, round(total_paid, 2), round(principal, 2))

print('Total Paid', round(total_paid,2))
print('Month', current_month)

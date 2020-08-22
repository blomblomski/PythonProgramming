late = True
if late:
    print('I need to call my manager!')

late = False
if late:
    print('I need to call my manager!')
else:
    print('No need to call my manager...')

income = 15000
tax_coefficient = 0.0

if income < 10000:
    tax_coefficient = 0.0
elif income < 30000:
    tax_coefficient = 0.2
elif income < 100000:
    tax_coefficient = 0.45

print('I will pay:', income * tax_coefficient, 'in taxes')

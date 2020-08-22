order_total = 247
discount = 100

if order_total > 100:
    discount = 25
else:
    discount = 0
print(order_total, discount, 'Total to pay', order_total - discount)


# Ternary
discount = 25 if order_total > 100 else 0
print(order_total, discount, 'Total to pay', order_total - discount)

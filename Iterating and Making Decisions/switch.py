
day_number = int(input('Please enter what day (number 0 - 6) it is : '))

if 1 <= day_number <= 5:
    day = 'Weekday'
elif day_number == 6:
    day = 'Saturday'
elif day_number == 0:
    day = 'Sunday'
else:
    day = ''
    raise ValueError(str(day_number) + ' is not a valid day number.')

print('The day is', day)
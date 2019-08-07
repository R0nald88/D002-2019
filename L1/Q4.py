i=input('Please enter the year:\n')
i=int(i)
i=i % 4
if i ==0:
    print('Yes, it\'s a leap year')
else:
    print('No, it\'s not a leap year')

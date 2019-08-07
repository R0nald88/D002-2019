i=input('Please enter the year:\n')
i=int(i)
h=i % 4
a=i % 100
c=i % 400
if h ==0:
    if a==0:
        if c==0:
            print('Yes, it\'s a leap year')
        else:
            print('No, it\'s not a leap year')
    else:
        print('Yes, it\'s a leap year')
else:
    print('No, it\'s not a leap year')


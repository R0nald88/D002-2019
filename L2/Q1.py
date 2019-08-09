n=input('Please input an integer:\n')
n=int(n)
i=2
while n>i:
    if n%i==0:
        print('%d is not a prime number' % int(n))
        break
    else:
        if i==n-1:
            print('%d is a prime number' % int(n))
    i+=1

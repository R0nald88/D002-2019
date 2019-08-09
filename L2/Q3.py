p=0
for n in [-120, 14, 93, 320, 1, -999]:
    for n1 in [-120, 14, 93, 320, 1, -999]:
        if n > n1:
            if n>p:
                p=n
        elif n<n1:
            if p<n1:
                p=n1

            

print('The largest number is %d' % p)

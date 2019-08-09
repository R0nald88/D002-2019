i=0
for a in range(1,60):
    for b in range(1,60):
        for c in range(1,60):
            for d in range(1,60):
                p=a+b+c+d
                if p==60:
                    t=a*b+b*c+c*d
                    if i < t:
                        i=t
                    
print('The maximum value of ab + bc + cd is %d' % int(i))                    

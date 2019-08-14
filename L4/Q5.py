def printer(secret, opened):
    i = 0
    a = ''
    try:
        while i < int(len(secret)):
            
            r='_'
            
            for l in opened:
                j=str(secret[int(l)])
                if i == l:
                    r = j
            a= a +r
            i=i+1
            
    except: 
        r='_'
        a= a +r
    print(a, end="\n")

# Note: you might use print(x, end="") to print x without changing line

printer("apple", [1, 2]) # _pp__
printer("orange", [0, 5]) # o____e
printer("cat", []) # ___

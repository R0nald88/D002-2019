a=[]
c=['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
n=0

print('You are going to enter a word 10 times\n i.e. You\'re going to enter 10 words')

while n <10:
    try:
        r = str(input('Please enter a word: '))
        
        for d in c:        
            if r[0]==d:
                a.append(r)
        n+=1
    except:
        continue
print(a)

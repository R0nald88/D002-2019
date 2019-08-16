
print('Welcome to Connect-4\nWould you want to play with computer or play with your friends?\nEnter "1" to play with computer\nEnter "2" to play with your friends\n')
k=int(input('Your choice: '))
pc=0
it=0
col=0
import random
while pc!=1:
    try:
        if k == 2:
            print('Player 1: O\tPlayer 2: X\nEnter the coloumn no. to add your sign!')
            break
        elif k == 1:
            print('You: O\tComputer: X\nEnter the coloumn no. to add your sign!')
            break
        else:
            print('Wrong Input!! Please enter a no. 1 or 2 to confirm your selection')
    except:
        print('Wrong Input!! Please enter a no. 1 or 2 to confirm your selection')
        continue
cells = [[' ',' ',' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]
def printcell(cells):
    print("-" * 29)
    for i in range(0, 6):
        for j in range(0, 7):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 29)
e=0

def check_col(cells):
    for i in range(0, 3):
        for j in range(0, 7):
            if cells[i][j] == cells[i+1][j] == cells[i+2][j] ==cells[i+3][j] != ' ':
                return True
    return False

def check_row(cells):
    for i in range(0, 6):
        for j in range(0, 4):
            if cells[i][j] == cells[i][j+1] == cells[i][j+2]  == cells[i][j+3] != ' ':    
                return True
    return False

def check_diagonal1(cells):
    i=0
    try:
        while i <3:
            for j in range(0, 4):
                if cells[i][j] == cells[i+2][j+2] == cells[i+1][j+1]== cells[i+3][j+3] != ' ':       
                    return True
                i+=1
    except:
        pass
    return False

def check_diagonal2(cells):
    i=0
    try:
       while i <3: 
            for j in range(0, 4):
                i1=5-i
                if cells[i1][j] == cells[i1-1][j+1] == cells[i1-2][j+2]== cells[i1-3][j+3] != ' ':       
                    return True
                i+=1
    except:
        pass
    return False

def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal1(cells) or check_diagonal2(cells):
        return True
    else:
        return False
n=1

while n<43:
    if k == 2:
        try:
            print('Round: %d'% n)
            if n == 1: 
                print('Player 1\'s turn: O')
            printcell(cells)
            c=check(cells)

            if c==False:
                col = int(input("Please enter the column: "))-1
                if not col in range(0,7):
                    print('Wrong Input\nPlease input the no. from range in 1 to 7')
                    continue
                if cells[0][col] != ' ':
                        print('The coloum you choose is full\nPlease enter another column')
                        continue
                for i in range (0,6):
                    row=5-i
                    
                    if not cells[row][col] != ' ':

                        if n % 2 ==0:
                            cells[row][col]='X'
                            print('Player 1\'s turn: O')
                        else:
                            cells[row][col]='O'
                            print('Player 2\'s turn: X')
                        break
            if c==True:
                if n % 2 ==0:
                    e=1
                else:
                    e=2
                break      
            n+=1
        except:
            print('Wrong Input\nPlease input the no. from range in 1 to 7')
            continue
    else:
        try:
            print('Round: %d'% n)
            if n == 1: 
                print('Your turn: O')
            printcell(cells)
            c=check(cells)

            if c==False:
                if (n-1) % 2 !=0:
                    col = random.randint(0,6)
                    while it != 1:
                        
                        if cells[0][col] != ' ':
                            col= random.randint(0,6)
                        else:
                            break

                else:
                    col = int(input("Please enter the column: "))-1
                    if not col in range(0,6):
                        print('Wrong Input\nPlease input the no. from range in 1 to 7')
                        continue
                for i in range (0,6):
                    row=5-i
                    if cells[0][col] != ' ':
                        print('the coloum you choose is full\nPlease enter another column')
                        continue
                    if not cells[row][col] != ' ':
                        if n % 2 ==0:
                            
                            cells[row][col]='X'
                            print('Your turn: O')
                        else:
                            cells[row][col]='O'
                            print('Computer\'s turn: X')
                        break
            if c==True:
                if n % 2 ==0:
                    e=1
                else:
                    e=2
                break      
            n+=1
        except:
            print('Wrong Input\nPlease input the no. from range in 1 to 7')
            continue
print('Game over!!')

if e == 1:
    print('Player 1 wins!!')
elif e==2:
    print('Player 2 wins!!')
else:
    print('However, no one win...')

print('Welcome to Connect-4\nPlayer 1: O\tPlayer 2: X\nEnter the coloumn no. to add your sign!')
cells = [[' ',' ',' ',' '], [' ',' ',' ',' '], [' ',' ',' ',' '],[' ',' ',' ',' ']]
def printcell(cells):
    print("-" * 17)
    for i in range(0, 4):
        for j in range(0, 4):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 17)
e=0

def check_col(cells):
    for i in range(0, 4):
        if cells[0][i] == cells[1][i] == cells[2][i] ==cells[3][i] != ' ':
            
            
            return True
    return False

def check_row(cells):
    for i in range(0, 3):
        if cells[i][0] == cells[i][1] == cells[i][2]  == cells[i][3] != ' ':
            
            
            return True
    return False

def check_diagonal(cells):
    
    if cells[0][0] == cells[2][2] == cells[1][1]== cells[3][3] != ' ':
        
        
        return True
    elif cells[1][2] == cells[2][1] == cells[0][0]  == cells[3][3] != ' ':
        
        
        return True
    return False

def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal(cells):
        return True
    else:
        return False
n=1

while n<17:
    try:
        print('Round: %d'% n)
        if n == 1: 
            print('Player 1\'s turn: O')
        printcell(cells)
        c=check(cells)

        if c==False:
            col = int(input("Please enter the column: "))-1
            for i in range (0,4):
                row=3-i
                if cells[row][col] != ' ':
                    if cells[0][col] != ' ':
                        print('the coloum you choose is full\nPlease enter another column')
                        continue
                else:
                    
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
        print('Wrong Input\nPlease input the no. from range in 1 to 4')
        continue
print('Game over!!')

if e == 1:
    print('Player 1 wins!!')
elif e==2:
    print('Player 2 wins!!')
else:
    print('However, no one win...')

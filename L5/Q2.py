print('Welcome to Tic-Tac-Toe\nPlayer 1: O\tPlayer 2: X\nEnter the coloumn and row no. to add your sign!')

def printcell(cells):
    print("-" * 13)
    for i in range(0, 3):
        for j in range(0, 3):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 13)
e=0

def check_col(cells):
    for i in range(0, 2):
        if cells[0][i] == cells[1][i] == cells[2][i] != ' ':
            return True
            if cells[0][i] == cells[1][i] == cells[2][i] == 'O':
                e=1
            elif cells[0][i] == cells[1][i] == cells[2][i] == 'X':
                e=2
    return False

def check_row(cells):
    for i in range(0, 2):
        if cells[i][0] == cells[i][1] == cells[i][2] != ' ':
            return True
            if cells[i][0] == cells[i][1] == cells[i][2] =='O':
                e=1
            elif cells[i][0] == cells[i][1] == cells[i][2] =='X':
                e=2
    return False

def check_diagonal(cells):
    
    if cells[0][0] == cells[2][2] == cells[1][1] != ' ':
        return True
        if cells[0][0] == cells[2][2] == cells[1][1] =='O':
            e=1
        elif cells[i][0] == cells[i][1] == cells[i][2] =='X':
            e=2
    elif cells[1][1] == cells[2][0] == cells[0][2] != ' ':
        return True
        if cells[0][0] == cells[2][2] == cells[1][1] =='O':
            e=1
        elif cells[i][0] == cells[i][1] == cells[i][2] =='X':
            e=2
    return False

def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal(cells):
        return True
    return False


    

cells = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
n=1

while n<=9:
    try:
        print('Round: %d'% n)
        if n == 1: 
            print('Player 1\'s turn:')
        printcell(cells)

        c = check(cells)
        if c==True:
            break
           
        if c==False:
            col = int(input("Please enter the column: "))-1
            row = int(input("Please enter the row: "))-1
            if cells[row][col] != ' ':
                print("It is taken already\nPlease choose another box")
                
                continue
                
            else:
                if n % 2 ==0:
                    cells[row][col]='X'
                    print('Player 1\'s turn:')
                else:
                    cells[row][col]='O'
                    print('Player 2\'s turn:')
        n+=1
    except:
        print('Wrong Input\nPlease input the no. from range in 1 to 3')
        continue
print('Game over!!')
if e == 1:
    print('Player 1 wins!!')
elif e==2:
    print('Player 2 wins!!')
else:
    print('However, no one win...')

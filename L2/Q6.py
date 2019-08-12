#L2 Q6: Banana Guessing game

#Step 1: Import necessary modules
import random
#Step 2: Welcome Message
print('''Welcome to the Banana Guessing Game
Dave hid some bananas. Your task is to find out the number of bananas he hid.''')
#Step 3: Choose a random number between 1-100
for c in range(1,9):
    n = random.randint(1,100)
# define a flag for found/not found and counter on how many trials
found = False
count = 0
#Step 4: Give three chances to the players 
while count<3:
    count +=1
    r=int(input("Please guess the no. of the banana he hides: "))
    if r>100 or r<1:
        print('Wrong input, please guess the no. in range of 1 to 100')
    else:
        if r>n:
            print('Your guess is too high')
        elif r<n:
            print('Your guess is too low')
        elif r==n:
            found = True
            break
        if count == 3:
            break

    print('Try again!!')
        

#Step 5: Display a message
if found == True:
        print('You got the correct guess in %d trials' % count)
        print('Dave\'s banana are now all yours!')
else:
        print("You failed to find the number of bananas Dave hid!")
        print('He actually hide %d bananas' % n)
        print("Try again next time!")

import random

a = int(input('\n\n hurry up !! give me 2 numbers now !!! do not think too much ..... fast !! \n> '))
b = int(input('\n> '))

if(a<b):
    hidden_number = random.randint(a,b)
else:
    hidden_number = random.randint(b,a)


print(f""" 

**------- Welcome to Guessing Game ! -------**

======= HOW TO PLAY =======
    1 - A Mystery number is hidden out in [{a} <---> {b}]
    2 - you have only 3 attempts to find it 
     
""")


attempts = 3
guessed_number = int(input('>'))
attempts -= 1

while ( attempts != 0 and guessed_number != hidden_number) :
    print("nope .. try again ")
    guessed_number = int(input('> '))
    attempts -=1
    
if(attempts):
    if(guessed_number == hidden_number):
        print(f"whoaaai, you have guessed it right ! \n yes it's the  ---> {hidden_number} <----")
else:
        print('you run out of attempts ,Try Again .. ')




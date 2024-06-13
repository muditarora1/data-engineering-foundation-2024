'''
1. Guessing Game

Challenge: Develop a program that lets a user guess a secret number.
Functionality:
Define a secret number (or store it in a variable).
Use a while loop to repeatedly prompt the user for guesses.
Inside the loop:
Check if the guess is too high, too low, or correct.
Provide feedback to the user based on their guess.
When the guess is correct, print a congratulatory message.
'''
import time

secret_number = 58
while True:
    num = int(input('number= '))
    if num==secret_number:
        print('congo')
        break
    if num<secret_number:
        print('too low')
    else: print('too high')

'''
2. Menu-Driven Program (While Loop Version)

Challenge: Rewrite the menu-driven program using a while loop.
Functionality:
Create a loop that continues until the user chooses to exit.
Inside the loop:
Display a menu with options (e.g., add, subtract, exit).
Use if statements to handle different menu options and perform the corresponding actions (add, subtract, etc.).
'''

while True:
    x = int(input('select 1.add  2.subtract  3.exit'))
    if x==1:
        print('Enter 2 number: ')
        a=int(input())
        b=int(input())
        print(a+b)
    elif x==2:
        print('Enter 2 number: ')
        a = int(input())
        b = int(input())
        print(a - b)
    elif x==3:
        break
    else: print('Invalid input')

'''
3. Countdown Timer

Challenge: Create a program that simulates a countdown timer.
Functionality:
Prompt the user to enter a starting time in seconds.
Use a while loop with a counter variable.
Inside the loop:
Decrement the counter variable by 1 (simulating one second passing).
Print the remaining time.
Once the counter reaches 0, print a message like "Time's up!"
Note: Functionality like time.sleep(1) might not be available in all environments.

This organization clarifies the purpose and steps involved in each challenge.
'''
timee = int(input('enter time in seconds: '))
counter = timee
while counter!=0:
    print(counter)
    counter -= 1
    time.sleep(1)
print('times up')
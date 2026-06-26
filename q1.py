'''
🚆 Railway Ticket Booking System

Problem Statement:
You are tasked with creating a simple railway ticket booking system for a fictional railway company called CodeRail. The system should ask users for their age, travel class, and whether they want a meal included. Based on this input, the system will calculate and display the total ticket price.

🎯 Requirements:

1. Ask the user for their name and age.
2. Ask them to choose a class:

⿡ First Class – ₹1500
⿢ Second Class – ₹1000
⿣ Sleeper Class – ₹500

3. If the passenger is under 5 years old, the ticket is free.

4. If the passenger is a senior citizen (60+), apply a 20% discount.


5. Ask if they want to add a meal:

Yes – ₹200 extra

No – No extra charge




6. Finally, print the passenger details and the final ticket price.'''


print(
'''
=============================
RAILWAY TICKET BOOKING SYSTEM
=============================

=======
WELCOME
=======

'''    
)
name1 = input("enter your name please : ")
age1 = int(input('enter your age please : '))
while True:
    class1 = int(input('''
which class you want to have 
    1. first class = 1500
    2. second class = 1000
    3. sleeper class = 500
please enter the corresponding number to class : '''))
    if class1 == 1:
        print('you have selected FIRST CLASS : ')
        cost1 = 1500
        break
    elif class1 == 2:
        print('you have selected SECOND CLASS : ')
        cost1 = 1000
        break
    elif class1 ==3:
        print('you have selected SLEEPER CLASS : ')
        cost1 = 500
        break
    else :
        print('enter valid input')

if age1 <5:
    cost1 = cost1*0
    print('as passenger age is less than 5 your ticket price is " 0 "')
if age1 >= 60:
    cost1 = cost1*0.8
    print('as you are senior citizen you got 20 % discount on your ticket')

while True:
    meal1 = input('do you want to have meal yes or no { addition of meal will charged 200 extra}')
    if meal1 == "yes":
        cost1 = cost1+200
        break
    elif meal1 == "no":
        break
    else:
        print('please enter valid input')

print(f'''
NAME : {name1}
AGE : {age1}
YOUR FINAL TICKET PRICE WOULD BE : {cost1} ''')


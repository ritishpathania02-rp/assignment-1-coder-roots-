'''
🧠Burger King has launched a self-order kiosk where customers can place their orders using a Python-based system. Your task is to build a simple Burger King order system in Python. The system should:
- Display a menu with 3 items and their prices.
- Let the user choose what they want to order and how many.
- Ask the user if they have a 

coupon code

.
- If the user enters a valid coupon code, apply the discount.
- Display the final bill with or without discount applied.




🧾MENU


  Item                                                             Price (₹)

1. Whopper Burger                                    ₹150
                                


2. Crispy Veg                                         ₹100                                   



3. Chicken Wings                                  ₹120                                







🎟️


Code                                                               Discount

KING50                                                         50% off                                                        

BK20                                                         ₹20 off total                                                        


NOCOUPON                                                  No discount




🎯

Use if-else statements to check coupon codes.

Calculate total price based on the quantity.

Apply the discount accordingly.

Print a at the end.
=====================================================================================================================
=====================================================================================================================
'''

print('''

------WELCOME TO BURGER KING 🍔 ------
      MENU:
      1.WOPPER BURGER : 150
      2.CRISPY VEG    : 100
      3.CHICKEN WINGS : 120

''')

item1 = int(input('ENTER THE ITEM NUMBER (1/2/3) : '))
if item1 == 1:
    amt1 = 150
elif item1 == 2:
    amt1 = 100
elif item1 ==3:
    amt1 = 120
else:
    print('invalid choice')
quan1 = int(input('how much quantity you want : '))
amt1 = amt1*quan1
coup1 = input('do you have coupon code [ yes/no]')
if coup1 == "yes":
    code1 = input('enter your coupon code').lower()
    if code1 == "king50":
        print('valid code you got 50% off')
        d= " 50%"
        amt1d = amt1*0.5
    elif code1 == "bk20":
        print('valid code you got 20% off')
        d = " 20%"
        amt1d = amt1*0.8
    else:
        print('not a valid coupon you got no discount')
        d = " 0%"
        amt1d = amt1

print(f'''  
Applying coupon...
Original Price: {amt1}
Discount Applied: {d}
Final Price: {amt1d}
Thanks for ordering at Burger King! 🍟''')




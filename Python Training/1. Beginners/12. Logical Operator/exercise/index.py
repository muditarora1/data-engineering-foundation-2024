'''
Challenge 1: Scholarship Eligibility

Write a program that prompts the user for their age and grade (as a number).
Use and to check if they are at least 18 years old (age >= 18) and have a passing grade (e.g., grade >= 60).
Print messages based on eligibility:
If both conditions are met: "Eligible for scholarship!"
Otherwise, specify which condition(s) they need to meet (e.g., "Not old enough" or "Grade not high enough").
'''
def func(age,grade):
    if age>=18 and grade>=60:
        print('eligible')
    elif age<18:
        print('underaged')
    else:
        print('grade not high enough')

age = 19
grade = 81

'''
Challenge 2: Discount with Membership or Coupon

Write a program that simulates a discount scenario.
Use or to check if the customer has a membership (has_membership = True) or a valid coupon (has_coupon = "valid").
Apply a discount (e.g., 10%) to the original price if either condition is met.
Print the final price with or without the discount.
'''
has_membership = True
has_coupon = "valid"
price=100
if has_coupon=='valid' or has_membership==True:
    discount=10
else:
    discount=0
print(price-(price*discount/100))

'''
Challenge 3: Weekday Check with Negation

Write a program that prompts the user to enter a day of the week (e.g., "Monday").
Use not to check if it's not the weekend (weekend days are "Saturday" or "Sunday").
Print messages based on the day:
If it's not the weekend: "It's a weekday!"
Otherwise: "It's the weekend!"
'''
day = 'saturday'
if day == 'saturday' or 'sunday':
    print('its weekend')
else:
    print('its a',day)

'''
Challenge 4: Login with Combined Conditions

Write a program that prompts the user for a username and password.
Use a combination of and and not to check:
Username is correct (correct_username = "user123")
Password is not empty (password != "")
Print messages based on login attempt:
If both conditions are met: "Login successful!"
Otherwise, specify the issue (e.g., "Incorrect username" or "Empty password").
'''

correct_password = '1234'
correct_username = "user123"
username = "user123"
password = '1234'
if password != '':
    if username == correct_username and password == correct_password:
        print('Login successful!')
    else:
        print('incorrecr user or pass')
else:
    print('Empty pass')

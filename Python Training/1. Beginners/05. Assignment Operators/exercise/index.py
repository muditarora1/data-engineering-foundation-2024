'''
Challenge 1: Shorthand Updates
Objective: Utilize shorthand assignment operators to modify a variable's value.

Steps:

Initialize a variable named count with a value of 5.
Add 3: Update count by adding 3 using the += operator. Print the new value.
Subtract 2: Update count by subtracting 2 using the -= operator. Print the new value.
Multiply by 4: Update count by multiplying it by 4 using the *= operator. Print the new value.
Divide by 2: Update count by dividing it by 2 using the /= operator. Print the new value.
'''

count = 5
count +=3
print(count)
count -=2
print(count)
count *=4
print(count)
count /=2
print(count)

'''
Challenge 2: Increment and Decrement
Objective: Explore the increment (++) and decrement (--) operators.

Steps:

Initialize two variables: x with a value of 10 and y with a value of 20.
Increment x: Increase x by 5 using the x += 5 operator (equivalent to x = x + 5). Print the updated value of x.
Decrement y: Decrease y by 3 using the y -= 3 operator (equivalent to y = y - 3). Print the updated value of y.
'''

x,y =10,20
x += 5
y -= 3
print(x,y)

'''

'''
total = 100
item1 = 25
item2 = 30
total -= item1 + item2
print(total)

'''Challenge 4: Augmented Assignment with Strings
Objective: Modify strings using the += operator for concatenation.

Steps:

Initialize a variable named message with the value "Hello".
Concatenate string: Append " World!" to the end of message using the += operator: message += " World!". Print the final message.
'''

a = 'Hello'
a+= ' World!'
print(a)

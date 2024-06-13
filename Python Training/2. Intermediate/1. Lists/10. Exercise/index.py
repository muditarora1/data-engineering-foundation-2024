'''
Basic List Creation
Challenge 1: Create lists in different ways.

Using square brackets: Create a list of your favorite colors.
Using the list() function: Create a list from a string (e.g., list("hello")).
Using list comprehension (bonus challenge): Create a list of squares from numbers 1 to 5 (e.g., [x**2 for x in range(1, 6)]).
'''

l1 = ['blue','orange']
l2 = list('blue')
l3 = [i**2 for i in range(1,6)]
print(l1,l2,l3)

'''
Accessing List Elements
Challenge 2: Access elements in a list of fruits.

Access the first and last element using indices (0 and -1).
Print a specific element by index (e.g., the element at index 2).
'''
fruits = ['apple','orange','kiwi','litchi']
print(fruits[0])
print(fruits[-1])
print(fruits[1])

'''
Modifying Lists
Challenge 3: Update and remove items in a list of numbers.

Update the value at a specific index (e.g., change the element at index 1 to a new value).
Use negative indexing to modify elements from the end (e.g., change the second-to-last element).
'''
fruits[1] = 'banana'
fruits[-2] = 'pineapple'
print(fruits)

'''
Removing List Items
Challenge 4: Remove items from a grocery list.

Remove a specific item by value (e.g., "milk") using the remove() method.
Remove the element at a specific index using the pop() method.
'''
fruits.remove('banana')
print(fruits)
fruits.pop(1)
print(fruits)

'''
Multi-Dimensional Lists
Challenge 5: Create a two-dimensional list for a tic-tac-toe board.

Initialize the board with empty elements (e.g., with "-" or None).
Challenge 6: Create a three-dimensional list for a Rubik's cube.

Initialize each element with a color representing a cube face.
'''
ttt = [['-','-','-'], ['-','-','-'], ['-','-','-']]
print(ttt[0])
print(ttt[1])
print(ttt[2])

rubiks_cube = [[['blue'],['blue'],['blue'],['blue'],['blue'],['blue'],['blue'],['blue'],['blue']],
               [['white'],['white'],['white'],['white'],['white'],['white'],['white'],['white'],['white']],
               [['red'],['blue'],['blue'],['blue'],['blue'],['blue'],['blue'],['blue'],['blue']],
               [['yellow'],['blue'],['blue'],['blue'],['blue'],['blue'],['blue'],['blue'],['blue']],
               [['green'],['blue'],['blue'],['blue'],['blue'],['blue'],['blue'],['blue'],['blue']],
               [['orange'],['blue'],['blue'],['blue'],['blue'],['blue'],['blue'],['blue'],['blue']]]

'''
Iterating Through Lists
Challenge 7: Iterate through a list of names.

Use a for loop to iterate through the list and print each name.
Print the index and element together using enumerate() (e.g., "(0, Alice)" for the first element).
'''

for i in fruits:
    print(i)

print(tuple(enumerate(fruits)))

'''
List Unpacking
Challenge 8: Unpack elements from a student information list.

Create a list of student information (name, age, grade).
Use list unpacking to assign these values to separate variables.
'''
l = ['mudit',10,'a1']
name,age,grade = l
print(name,age,grade)
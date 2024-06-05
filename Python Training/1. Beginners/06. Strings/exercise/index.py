'''
Challenge 1: Working with Quotes and Multiline Strings
Write a program that uses double quotes to store a famous quote.

Then, write a program that uses triple quotes (either ''' #or """) to create a multiline poem or paragraph. Print both the quote and the poem/paragraph.

'''
Challenge 2: Concatenation Fun
Write a program that creates two variables: first_name and last_name. Concatenate them with a space in between to form a full name and print it.

Then, try a more elaborate concatenation: create a greeting message by combining a string literal with the full name variable.
'''
a = 'my name is '
name = 'mudit'+ ' ' + 'arora'
a += name
print(a)

print(len(name))

'''
Challenge 4: Indexing and Slicing Adventures
Write a program that prompts the user to enter a word and then prints the first and last characters of the word using 
indexing (e.g., word[0] for first character).

Next, modify the program to extract a substring using slicing. Prompt the user for the starting and
ending indices (consider using int() to convert input to integers) and print the extracted substring.
'''

a = input('enter a name ')
print(a[0],a[-1])

x,y = int(input('Enter start indice')), int(input('Enter end indices'))
print(a[x:y])

print(a.upper())
print(a.strip())

name = "Hussain"
age = 20
city = 'Jodhpur'
formatted_string = f"My name is {name}, I am {age} years old and a resident of {city} city."
print(formatted_string)

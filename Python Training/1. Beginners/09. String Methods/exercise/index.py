'''
Challenge 3: Checking String Start and End

Prompts the user to enter a string and a character.
Uses startswith() to check if the string starts with the character.
Uses endswith() to check if the string ends with the character.
Prints messages based on the results.
'''

filename = "example.txt"
starts_with = filename.startswith("example")
ends_with = filename.endswith("/.txt")
print(starts_with)  # True
print(ends_with)

sentence = "I like programming in Java."
new_sentence = sentence.replace("Java", "Python")
print(new_sentence)  # I like programming in Python.

'''
Challenge 5: Finding Substring Positions

Prompts the user to enter a sentence and a word.
Uses find() to find the first occurrence of the word (returns -1 if not found).
Uses index() to find the first occurrence of the word (raises ValueError if not found).
Prints the index (if found by find()) and handles the potential ValueError.
Demonstrates the difference between find() and index().
'''

name = 'Mudit Arora'
print(name.find('r'))
print(name.index('r'))

sentence = "Python    is a powerful programming language"
words = sentence.split(" ")
print(words)

sentence = ' '.join(words)
print(sentence)

sen1,sen2 = sentence.split('powerful')[0], sentence.split('powerful')[1]

print(sen1,'thala', sen2)


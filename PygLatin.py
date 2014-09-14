"""Pig Latin is a language game, 
where you move the first letter of the word to the end and add "ay." 
So "Python" becomes "ythonpay." 

To write a Pig Latin translator in Python, here are the steps we'll need to take:

1. Ask the user to input a word in English.
2. Make sure the user entered a valid word.
3. Convert the word from English to Pig Latin.
4. Display the translation result."""

print 'Welcome to the Pig Latin Translator!'

# Start coding here!
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
    word = original.lower()
    first = word[0]
    new_word = word[1:len(word)]
    new_word = new_word + first + pyg
    print new_word
else:
    print 'empty'
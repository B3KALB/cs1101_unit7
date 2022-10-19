 
#Unit 7 Programming Assignment
 
alphabet = "abcdefghijklmnopqrstuvwxyz" # this is the variable that holds our alphabet string to compare to
 
test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] # this is the list assigned to the
# variable test_dups that has three duplicates and two non-duplicates
 
test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]  # this is a list assigned to
# the variable test_miss that has 3 strings, one duplicate string, one word, and one sentence
 
# From Section 11.2 of:
# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press.
def histogram(s): # this is our function histogram being defined and takes a string as a parameter
   d = dict() # this is our variable "d" that holds an empty dictionary in "= dict()" that is used to store data
   for c in s: # this is our for loop that iterates through the string and "c" becomes our counter variable
       if c not in d: # this is our if conditional statement that checks a negative "in" against variable "d"
           d[c] = 1 # this is the command that says if there isn't one, make one count
       else: # this is the else condition
           d[c] += 1 # this is the command that says if there is one, add another to count
   return d  # this is the return statement that says, once the for loop is done, give back variable "d"
 
# Part 1
def has_duplicates(s): # this is the function being defined and takes a string as a parameter
   h = histogram(s) # this is where we call our function histogram, pass in the argument of string and assign
   # "h" as the variable name
   for i, j in h.items(): # this is our for loop that iterates through and finds the value of the items of "h"
       if j > 1: # this is our if condition statement that says if the value of "j" is more than 1, do this
           return True # this is boolean return statement that gives us the value of True
   return False # this acts as both the else and the return giving back a value of False if the above condition
   #  isn't met
 
for s in test_dups: # this is our for loop that iterates through variable "test_dups" and "s"is our counter
   if has_duplicates(s): # this is our if statement that calls our "has_duplicates" function and passes in the
   # string as an argument
       print(f"{s}: has duplicates") # this is displays our value and tells you it has duplicates
   else: # this is our else default that says if other conditions not met, do this
       print(f"{s} : has no duplicates") # this displays our value and tells you that it doesn't have duplicates
 
# Part 2
def missing_letters(s): # this is our function "missing_letters" that passes in a parameter string
   h = histogram(s) # this is our variable "h" that has been assigned the call function and passes in an argument
   # string
   new_words = [] # this is our variable "new_words" that has been assigned the value of empty list
   for letter in alphabet: # this is our for loop that iterates through the alphabet variable and assigns each
   # value to the counter of "letter"
       if letter not in h: # this is our conditional that says if  the variable "letter" isn't present in variable
       # "h" then do this
           new_words.append(letter) # this is where the letter, through the .appended method, are adding letter to
           # the variable "new_words"
   return "".join(new_words) # this is the return that gives us the default method of .join to add the values into
   # the new_words variable
 
for s in test_miss: # this is the for loop that iterates through "test_miss" and "s" becomes our counter variable
   new_words = missing_letters(s) # this is our function call being assigned to a variable and has an argument
   # passed in
   if len(new_words): # this is our conditional statement that says if new_words has a length then do this
       print(f"{s}: is missing letters: {new_words}") # this is our display that shows the variable "s" and that it
       # is missing the letters stored in the variable "new_words"
   else: # this is the default response that says if "new_words" has no length, then do this
       print(f"{s}: uses all the letters") # this is our display that shows the value of the variable "s"

# Part1 outputs

# zzz: has duplicates # this is the result of the function "has_duplicates(s)" and the pt1 for loop
# dog : has no duplicates # this is the result of the function "has_duplicates(s)" and the pt1 for loop
# bookkeeper: has duplicates # this is the result of the function "has_duplicates(s)" and the pt1 for loop
# subdermatoglyphic : has no duplicates # this is the result of the function "has_duplicates(s)" and the pt1 for 
# loop
# subdermatoglyphics: has duplicates # this is the result of the function "has_duplicates(s)" and the pt1 for loop

# Part2 outputs

# zzz: is missing letters: abcdefghijklmnopqrstuvwxy # this is the result of the function "missing_letters(s)" and 
# the pt2 for loop
# subdermatoglyphic: is missing letters: fjknqvwxz # this is the result of the function "missing_letters(s)" and 
# the pt2 for loop
# the quick brown fox jumps over the lazy dog: uses all the letters # this is the result of the function 
# "missing_letters(s)" and the pt2 for loop
# Welcome to Unit 7 Programming Assignment! This will be your last programming assignment for this course.

# Start with the following Python code.   

alphabet = "abcdefghijklmnopqrstuvwxyz" # this is the variable that holds our aplhabet string to compare to

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] # this is the list assigned to the
# variabvle test_dups that has three douplicates and two non-duplicates 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]  # this is a list assigned to
# the variable test_miss that has 3 strings, one duplicate string, one word, and one sentence

# From Section 11.2 of: 
# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 
def histogram(s): # this is our function histogram being defined and takes a string as a parameter
    d = dict() # this is our variable "d" that hods an empty dictionary in "= dict()" that is used to store data
    for c in s: # this is our for loop that iterates through the string and "c" becomes our counter variable
        if c not in d: # this is our if conditioanal statement that checks a negetive "in" against variable "d"
            d[c] = 1 # this is the command that says if there isnt one, make one count
        else: # this is the else condition
            d[c] += 1 # this is the command that says if there is one, add another to count
    return d  # this is the return statement that says, once the for loop is done, give back variable "d" 


# Part 1
# Write a function called has_duplicates that takes a string parameter and returns True if the string has any 
# repeated characters. Otherwise, it should return False.  

def has_duplicates(s): # this is the function being defined and takes a string as a parameter 
    h = histogram(s) # this is where we call our function histogram, pass in the argument of string and assign 
    # "h" as the variable name 
    for i, j in h.items(): # this isour for loop that iterates through and finds the value of the items of "h"
        if j > 1: # this is our if condition statement that says if the value of "j" is more than 1, do this
            return True # this is boolean return statement that gives us the value of True
    return False # this acts as both the else and the return giving back a value of False if the above condition
    #  isn't met

# Implement has_duplicates by creating a histogram using the histogram function above. 
# Do not use any of the implementations of has_duplicates that are given in your textbook. 
# Instead, your implementation should use the counts in the histogram to decide if there are any duplicates. 

# Write a loop over the strings in the provided test_dups list. 
# Print each string in the list and whether or not it has any duplicates based on the return value of 
# has_duplicates for that string. For example, the output for "aaa" and "abc" would be the following. 

# aaa has duplicates
# abc has no duplicates 

# Print a line like one of the above for each of the strings in test_dups. 

for s in test_dups: # this is
    if has_duplicates(s): # this is
        print(f"{s}: has duplicates") # this is
    else: # this is
        print(f"{s} : has no duplicates") # this is

# Part 2
# Write a function called missing_letters that takes a string parameter and returns a new string with all the 
# letters of the alphabet that are not in the argument string. 

def missing_letters(s): # this is
    h = histogram(s) # this is
    new_words = [] # this is
    for letter in alphabet: # this is
        if letter not in h: # this is
            new_words.append(letter) # this is
    return "".join(new_words) # this is



# The letters in the returned string should be in alphabetical order. 

# Your implementation should use a histogram from the histogram function. 
# It should also use the global variable alphabet. 
# It should use this global variable directly, not through an argument or a local copy. 
# It should loop over the letters in alphabet to determine which are missing from the input parameter. 

# The function missing_letters should combine the list of missing letters into a string and return that string. 

# Write a loop over the strings in list test_miss and call missing_letters with each string. 
# Print a line for each string listing the missing letters. 
# For example, for the string "aaa", the output should be the following. 
# aaa is missing letters bcdefghijklmnopqrstuvwxyz 

# If the string has all the letters in alphabet, the output should say it uses all the letters. 
# For example, the output for the string alphabet itself would be the following. 
# abcdefghijklmnopqrstuvwxyz uses all the letters 

# Print a line like one of the above for each of the strings in test_miss. 
for s in test_miss: # this is
    new_words = missing_letters(s) # this is
    if len(new_words): # this is
        print(f"{s}: is missing letters: {new_words}") # this is
    else: # this is
        print(f"{s}: uses all the letters") # this is
# Submit your Python program. It should include the following. 

# The provided code for alphabet, test_dups, test_miss, and histogram. 
# Your implementation of the has_duplicates function. 
# A loop that outputs duplicate information for each string in test_dups. 
# Your implementation of the missing_letters function. 
# A loop that outputs missing letters for each string in test_miss. 
# Also submit the output from running your program. 

# Your submission will be assessed using the following Aspects.

# Does the program include a function called has_duplicates that takes a string parameter and returns a boolean?
# Does the has_duplicates function call the histogram function? 
# Does the program include a loop over the strings in test_dups that calls has_duplicate on each string? 
# Does the program correctly identify whether each string in test_dups has duplicates? 
# Does the program include a function called missing_letters that takes a string parameter and returns a string? 
# Does the missing_letters function call the histogram function?
# Does the missing_letters function use the alphabet global variable directly?
# Does the program include a loop over the strings in test_miss that calls missing_letters on each string?
# Does the program correctly identify the missing letters for each string in test_miss, including each string 
# that "uses all the letters"?

# output

# zzz: has duplicates # this is
# dog : has no duplicates # this is
# bookkeeper: has duplicates # this is
# subdermatoglyphic : has no duplicates # this is
# subdermatoglyphics: has duplicates # this is
# zzz: is missing letters: abcdefghijklmnopqrstuvwxy # this is
# subdermatoglyphic: is missing letters: fjknqvwxz # this is
# the quick brown fox jumps over the lazy dog: uses all the letters # this is
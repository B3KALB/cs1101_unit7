# Welcome to the Unit 7 Discussion Forum!

# Implement your own Python code examples to describe how tuples can be useful with loops over lists and 
# dictionaries.
 
# Do not copy code from the textbook or any other source. 

# Your descriptions and examples should include: the zip function, the enumerate function, and the items method. 

# The code and its output must be explained technically whenever asked. The explanation can be provided before 
# or after the code, or in the form of code comments within the code. For any descriptive type question, Your 
# answer must be at least 150 words.

# End your discussion post with one question related to programming fundamentals learned in this unit from which 
# your colleagues can formulate a response or generate further discussion. 
# Remember to post your initial response as early as possible, preferably by Sunday evening, 
# to allow time for you and your classmates to have a discussion.

# When you use information from a learning resource, such as a textbook, be sure to credit your source and include 
# the URL. Continue to practice using APA format for citations and references.

first = 'Jen', 'Blake', 'Hank', 'Hazel' # first is the variable that defines my first name tuple
last = ['Brockway', 'Brockway', 'Brockway', 'Brockway'] # last is the variable that defines the last name list
Eye = {
    "Girl": "Blue",
    "Boy": "Hazel",
    "LittleBoy": "Green",
    "LittleGirl": "Green"
} # Eye is the name of the dictionary that we will use for the code below

def the_zip_function(first, last): # this is the zip function that zips through two parameters that are passed in

    for full_name in zip(first, last): # this is our for loop that does the heavy lifting and goes through our 
        # tuple and list

        print(f'My name is: {full_name}') # this displays our tuple value and our list value blended into one value
    
the_zip_function(first, last) # this calls our function and passes in one tuple and one list as arguments

# output
# My name is: ('Jen', 'Brockway')
# My name is: ('Blake', 'Brockway')
# My name is: ('Hank', 'Brockway')
# My name is: ('Hazel', 'Brockway')

def the_enumerate_function(first): # this creates our enumerate function and passes in a tuple as a parameter

    for i,j in enumerate(first): # this is our for loop that goes through the parameter and assigns an index to
        #  each value
    
        print(f'Family order: {(i + 1)} and name: {j}') # this is our display that shows the index minipulated by 
        # one and the value for each index

the_enumerate_function(first) # this calls our function and passes in a tuple as an argument

# output
# Family order: 1 and name: Jen
# Family order: 2 and name: Blake
# Family order: 3 and name: Hank
# Family order: 4 and name: Hazel

def items_method(eye_color): # this defines our function and passes in a dictionary as a parameter

    color = eye_color.items() # this assigns all of the items in out parameter to a value of color
    
    for eyes in color: # this is our for loop that goes through the items in color and assigns them to the value of 
        # eye
    
        print(f'I am a: {eyes} : is the color of my eyes.') # here we display each item in our dictoinary through
        # the value of eyes 
        
items_method(Eye) # this is function call with out dictionary argument passed in

# output
# I am a: ('Girl', 'Blue') : is the color of my eyes.
# I am a: ('Boy', 'Hazel') : is the color of my eyes.
# I am a: ('LittleBoy', 'Green') : is the color of my eyes.
# I am a: ('LittleGirl', 'Green') : is the color of my eyes.

# references:

# https://greenteapress.com/thinkpython2/thinkpython2.pdf\

#  https://realpython.com/python-enumerate/

# https://www.programiz.com/python-programming/online-compiler/
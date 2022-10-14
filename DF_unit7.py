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
first = 'Jen', 'Blake', 'Hank', 'Hazel'
last = ['Brockway', 'Brockway', 'Brockway', 'Brockway']
Eye = {
    "Girl": "Blue",
    "Boy": "Hazel",
    "LittleBoy": "Green",
    "LittleGirl": "Green"
}

def the_zip_function(first, last):
    for full_name in zip(first, last):
        print(f'My name is: {full_name}')
    

the_zip_function(first, last)

def the_enumerate_function(first):
    for i,j in enumerate(first):
        print(f'Family order: {(i + 1)} and name: {j}')

the_enumerate_function(first)

def items_method(eye_color):
    color = eye_color.items()
    for eyes in color:
        print(f'I am a: {eyes} : is the color of my eyes.')
        
items_method(Eye)

# references:

# https://greenteapress.com/thinkpython2/thinkpython2.pdf
# Learning Journal Unit 7

# From Section 11.5 of: 
# Downey, A. (2015). Think Python: How to think like a computer scientist. 
# Needham, Massachusetts: Green Tree Press. 
dicky= {
    "key1": "zero",
    "key2": "one",
    "key3": 2,
    "key4": "three",
    "key5": "4",
    6: 5,
    "7": "six"
} # this is the dictionary that I made to be used in this project. It consitsts of several keys assigned string 
# values, and a key that is an integer value. then as values we have several strings and two integers to show 
# diversity in the program 

def original_dict(d): # this is the function that returns our original dictionary and has d passed in as a 
# perameter
    dict_items = d.items() # this is the variable that we assigne the value of our parameter and the .items method
    print(dict_items) # this is the display statement to show the items in our parameter
original_dict(dicky) # this is the function call with the argument of "dicky" passed in

def invert_dict(d): # this is the
    inverse = dict() # this is the
    for key in d: # this is the
        val = d[key] # this is the
        if val not in inverse: # this is the
            inverse[val] = [key] # this is the
        else: # this is the
            inverse[val].append(key) # this is the
    print(f"dict_inverse({inverse})")  # this is the
invert_dict(dicky) # this is the

# outputs
# dict_items([('key1', 'zero'), ('key2', 'one'), ('key3', 2), ('key4', 'three'), ('key5', '4'), (6, 5), ('7', 'six')])
# dict_inverse({'zero': ['key1'], 'one': ['key2'], 2: ['key3'], 'three': ['key4'], '4': ['key5'], 5: [6], 'six': ['7']})


# My dictionary in perticular is not very useful except that it does a good job of showing the flexibility of the 
# program. Weather you are using inegers, strings or strings with inegers, as long as the key is uniuqe, it will
# work. Now an instance when this kind of srting device may be really useful is if it were set up as your contact 
# list the key could be the first name and the value could be the last name. idealy the inverted_dict function 
# should switch those for you.  But, we get the part where a key needs to be uniuque, if we have two Brittanys', 
# one wouldnt show, but if you had two lastnames of Addams, you would have the same issue. So, perhaps you could 
# make the key the fullname and the value the phone number. that would make both uniuqe and make it useful to invert

# references:
# https://greenteapress.com/thinkpython2/thinkpython2.pdf


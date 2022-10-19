# Learning Journal Unit 7
# Construct a Python dictionary that returns a list of values for each key. 
# The key can be whatever type you want. 

# Employ the dictionary so that it could be useful for something meaningful to you. 
# Provide at least three different items in it. Implement the dictionary yourself. 
# Do not copy the design or items from some other source. 

# Next consider the invert_dict function from Section 11.5 of your textbook. 

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
}

def original_dict(d):
    dict_items = d.items()
    print(dict_items)
original_dict(dicky)

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    print(f"dict_inverse({inverse})") 
invert_dict(dicky)
# Modify this function so that it can invert your dictionary. 
# In particular, the function will need to turn each of the list items into separate keys in the inverted 
# dictionary. 

# Run your modified invert_dict function on your dictionary. Print the original dictionary and the inverted one. 

# Include your Python program and the output in your Learning Journal submission. 

# Describe what is useful about your dictionary. Then describe whether the inverted dictionary is useful or 
# meaningful and why. 

# outputs
# dict_items([('key1', 'zero'), ('key2', 'one'), ('key3', 2), ('key4', 'three'), ('key5', '4'), (6, 5), ('7', 'six')])
# dict_inverse({'zero': ['key1'], 'one': ['key2'], 2: ['key3'], 'three': ['key4'], '4': ['key5'], 5: [6], 'six': ['7']})

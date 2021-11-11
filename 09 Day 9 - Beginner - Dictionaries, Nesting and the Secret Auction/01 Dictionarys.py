programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# Retrieving items from a dictionary
# print(programming_dictionary["Bug"])

# Adding items to a dictionary
# programming_dictionary["Variable"] = "A value that can change."
# print(programming_dictionary)

# Creating empty dictionarie
# empty_dict = {}
# empty_dict["Key"] = "Values"
# print(empty_dict)

# Wipe out a dictionary
# programming_dictionary.clear()
# print(programming_dictionary)

# Edit an item in dictionary
# programming_dictionary["Bug"] = "yash Patel"
# print(programming_dictionary)

# Loop through the dictionary
# While looping throuth the dictionary the result will be only key
for things in programming_dictionary:
    print(things)
    # Below line will print the values and above line will print the keys
    print(programming_dictionary[things])
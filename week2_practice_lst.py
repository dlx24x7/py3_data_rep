"""
Week 2 examples
Date: Jan 25 2020
Author Conrad U
"""
# Example 1
# Enter code here
prime = [2, 3, 5, 7, 11, 13]
print(prime[1], prime[3], prime[5])

# Output
#3 7 13

# Example 2
example_list = [2, 3, 5, 7, 11, 13]

# Prints first and last elements of a list by creating a new list

firstlast_list = [example_list[0], example_list[-1]] 
print(firstlast_list)


# Output
#[2, 13]

# Example 3
# Create a list formed by excluding the first and last items of example

example_list = [2, 3, 5, 7, 11, 13]

# Uncomment and complete
middle_list = example_list[1:-1]
print(middle_list)


# Output
#[3, 5, 7, 11]

# Example 4
# Create a list formed by 8 copies of True and 8 copies of False

truefalse_list = 8 * [True] + 8 * [False]
print(truefalse_list)


# Output
#[True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False]

# Example 5
# Create a list of words form a string consisting of words separated by space

quote = "Bring me a shrubbery"
word_list = quote.split(" ")
print(word_list)


# Output
#['Bring', 'me', 'a', 'shrubbery']

# Example 6
def word_count(text, word):
    """
    Given a string text consist of words separate by spaces and a string word
    (with no spaces), return the number of times that word appears in the text
    """
    text_list = text.split(" ")
    # print(text_list) 
    return text_list.count(word)


# Tests

print(word_count("this pigdog is a fine pigdog", "pigdog"))
print(word_count("this pigdog is not a dog", "dog"))
print(word_count("this pigdog is not a pig", "pigdog"))

# Output
#2
#1
#1

# Example 7
# Initial list
list1 = [2, 3, 5, 7, 11, 13]

# Another reference to list1
list2 = list1

# Print out both lists
print(list1)
print(list2)

# Update the first item in second list to zero
list2[0] = 0

# Print out both lists
print(list1)
print(list2)

# Explain what happens to list1 in a comment

# Answer - list1 and list2 are references to the same list
# Updating an item in one list mutates the other list


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[0, 3, 5, 7, 11, 13]
#[0, 3, 5, 7, 11, 13]

# Example 8 
# Initial list
list1 = [2, 3, 5, 7, 11, 13]

# Make a copy of list1
list2 = list(list1)

# Print out both lists
print(list1)
print(list2)

# Update the first item in second list to zero
list2[0] = 0

# Print out both lists
print(list1)
print(list2)

# Explain what happens to list1 in a comment
#list() takes an iterable object as input and 
# adds its elements to a newly created list
# list2 is a brand new list



# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[0, 3, 5, 7, 11, 13]

# Example 9 
def list_max(numbers):
    """
    Given a list of numbers, return the maximum (largest) number
    in the list
    """
    return max(numbers)

# Tests
print(list_max([4]))
print(list_max([-3, 4]))
print(list_max([5, 3, 1, 7, -3, -4]))
print(list_max([1, 2, 3, 4, 5]))


# Output
#4
#4
#7
#5

# Example 10
def concatenate_ints(int_list):
    """
    Given a list of integers int_list, return the integer formed by
    concatenating their decimal digits together
    """
    item_cat = ""
    for item in int_list:
        #print("item", item)
        item_string = str(item)
        item_cat = item_cat + item_string
    return item_cat

# Tests
print(concatenate_ints([4]))
print(concatenate_ints([4, 0, 4]))
print(concatenate_ints([123, 456, 789]))
print(concatenate_ints([32, 796, 1000]))


# Output
#4
#404
#123456789
#327961000
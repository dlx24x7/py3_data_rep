"""
week1_practice
This is the week one practice for data structures
"""
string1 = "It's just a flesh wound"
string2 = "It's just a flesh wound"	
string3 = "It's just a flesh wound"	
string4 = """It's just a flesh wound"""

print("Example 1")
print(string1)
print(string2)
print(string3)
print(string4)
print(" ")

# Create a string formed by selecting the first and last letters of example_string
print("Example 2")
example_string = "It's just a flesh wound"
print(example_string)

solution_string = example_string[0] + example_string[-1]
print(solution_string)
print(" ")

# Output should be 
#It's just a flesh wound
#Id

# Create a string formed by selecting all but the first and last letters of example_string
print("Example 3")
example_string = "It's just a flesh wound"
print(example_string)

solution_string = example_string[1:-1]
print(solution_string)

# Output should be 
#It's just a flesh wound
#t's just a flesh woun

print("Example 4")
# Create a string formed by selecting the first three characters of example_string
# plus the last three characters of example_string
example_string = "It's just a flesh wound"
print(example_string)

#solution_string = example_string[0:3] + example_string[-3:-1] + example_string[-1]
solution_string = example_string[:3] + example_string[-3:]
print(solution_string)

# Output should be 
#It's just a flesh wound
#It'und

print("Example 5")
def echo(call, repeats):
    """
    Echo the string call to the console repeats number of time
    Each echo should be on a separate line
    """
    print((call + "\n") * repeats)
    return



# Tests
echo("Hello", 5)
echo("Goodbye", 3)

# Output
#Hello
#Hello
#Hello
#Hello
#Hello
#Goodbye
#Goodbye
#Goodbye

print("Example 6")

def is_substring(example_string, test_string):
    """
    Function that returns True if test_string
    is a substring of example_string and False otherwise
    """

    # enter one line of code for substring test here
    if (example_string.find(test_string) >= 0):
        return True
    else: 
        return False

# Tests

example_string = "It's just a flesh wound."

print(is_substring(example_string, "just"))
print(is_substring(example_string, "flesh wound"))
print(is_substring(example_string, "piddog"))
print(is_substring(example_string, "it's"))
print(is_substring(example_string, "It's"))

# Output
#True
#True
#False
#False
#True
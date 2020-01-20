"""
Slicing strings.
"""

word = "everything"

# Selecting substrings
print("line 1:", word[1:5])
print("line 2:", word[5:9])

# Open ended slices
print("line 3:", word[5:])
print("line 4:", word[:4])

# Using negative indices
print("line 5:", word[-3:])
print("line 6:", word[2:-3])

# Indexing past the end
print("line 7:", word[8:20])
print("$" + word[22:29] + "^")

# Empty slices
print(word[6:6])
print(word[4:2])

# example of creating a sentence
country = "France"
capital = "Paris"
sentence = "The capital of {} is {}.".format(country, capital)
print(sentence)

# next example of creating a sentence
mood1 = "happy"
mood2 = "sad"
sentence1 = "I feel {0}, do you feel {0}?  Or are you {1}? I'm not sure if we should be {0}.".format(mood1, mood2)
print(sentence1)

# third example of formatting
name1 = "Pierre"
age1 = 7
name2 = "May"
age2 = 13

line1 = "{0:^7} {1:>3}".format(name1, age1)
line2 = "{0:^7} {1:>3}".format(name2, age2)
print(line1)
print(line2)

# last example of formatting
num = 3.283663293
output = "{0:>10.3f} {0:.2f}".format(num)
print(output)
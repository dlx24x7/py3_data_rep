"""
Python data Representations - strings
Quiz 1
"""
#print("Grail"[-1])
print("coconut"[-1], "num 1")
print("coconut"[6], "num 2")
print("coconut"[-6], "num 3")
#print("coconut"[7], "num 4")

#print("Castle Anthrax"[7:])
print("Sir Robin"[:3], "num 1")
print("Sir Robin"[0:3], "num 2")
print("Sir Robin"[1:4], "num 3")
print("Sir Robin"[1:3], "num 4")


string1 = "A"
string2 = "AB"
string3 = "CD"
print (string1 in string2)
print (4*string1)
print (string1 + string2)
#print (string2 - string1)

print(string2.index(string1))
#print(string3.index(string1))

print("{0}{1}{2}".format("abra", "cad", "abra"))

def count_vowels(word): 
    """
    takes the string word as input and returns the number of lower case values
    """
    num_a = word.count('a')
    print("Number of a is", num_a)
    num_e = word.count('e')
    print("Number of e is", num_e)
    num_i = word.count('i')
    print("Number of i is", num_i)
    num_o = word.count('o')
    print("Number of o is", num_o)
    num_u = word.count('u')
    print("Number of u is", num_u)
    return num_a + num_e + num_i + num_o + num_u

#print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))

def demystify(l1_string):
    """
    takes a string composed of characters "l" and "1" and returns a string replacing "l" by "a" and "1" by b
    """
    string_a = (l1_string.replace("l","a"))
    string_b = (string_a.replace("1", "b"))
    return string_b

print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))
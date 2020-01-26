"""
Python data represenations - Lists
Quiz 2, Week 2
January 26, 2020
"""
# Question 1
print("Question 1")
#print(list(range(0,4,1)))
#print(list(range(0,5)))
#print(range(0,5))
#print(list(range(0,5,1)))
print(list(range(1,6)))
print(range(1,6))
#print(list(range(5))
print(list(range(1,6,1)))

# Question 2
print(" ")
print("Question 2")
my_list = ["This", "course", "is", "great"]
print(len(my_list))
print(my_list[-1])
print(my_list[3])

# Question 3
print(" ")
print("question 3")
new_even_list = 2*my_list
print(new_even_list)
new_odd_list = list(new_even_list)
new_odd_list.append("Possibly?")
print(new_odd_list)
print("ans 1")
print(new_even_list[0 : len(new_even_list) // 2])
print(new_odd_list[len(new_odd_list) // 2 + 1 : len(new_odd_list)])
print("ans 2")
print(new_even_list[: len(new_even_list) // 2])
print(new_odd_list[len(new_odd_list) // 2 :])
print("ans 3")
print(new_even_list[0 : len(new_even_list) // 2 - 1])
print(new_odd_list[len(new_odd_list) // 2 : len(new_odd_list)])
print("ans 4")
print(new_even_list[0: len(new_even_list) // 2])
print(new_odd_list[len(new_odd_list) // 2 : len(new_odd_list)])

# Question 4
print("")
print("Question 4")
n = 4
m = 5
init_list = list(range(1, n))
print(init_list)
final_list = init_list * m
print(final_list)
print("the length is", len(final_list))
print((n-1)* m)
print(n + m)
print(n * (m -1 ))
print(n * m)

# Question 5
print("")
print("question 5")
n = 6
test_string = "xxx" + " " * n + "xxx"
print(test_string)
split_list = test_string.split(" ")
print(split_list)
print("the len of split_list is", len(split_list))
print(n + 1)
print(2)
print(3)
print(n)

# Question 6
print("")
print("question 6")
print("ans 1")
list1 = list(range(1, 10))
print("list 1", list1)
list2 = list(list1)
print("list 2", list2)
list2[0] = 0
print("list 2", list2)
print("list 1", list1)

print("ans 2")
list1 = list(range(1, 10))
print(list1)
list2 = list1
list2[0] = 0
print(list1)
print(list2)

print("ans 3")
list1 = list(range(1, 10))
print(list1)
list2 = [] + list1
print(list2)
list2[0] = 0
print(list2)
print(list1)

print("ans 4")
list1 = list(range(1, 10))
print(list1)
list2 = list1[:]
print(list2)
list2[0] = 0
print(list2)
print(list1)

print("Question 7")
def strange_sum(numbers):
    sum = 0
    count = 0
    for item in numbers: 
        #print(item)
        if (item % 3) != 0: 
            sum = sum + item
    return sum
print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))    
print(strange_sum(list(range(123)) + list(range(77))))
        
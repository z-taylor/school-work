# Write a program that first gets a list of integers from input. The input begins with an integer indicating the number of integers that follow. Then, get the last value from the input, which indicates a threshold. Output all integers less than or equal to that last threshold value.

# Ex: If the input is:
# 5
# 50
# 60
# 140
# 200
# 75
# 100

# the output is:
# 50
# 60
# 75

# The 5 indicates that there are five integers in the list, namely 50, 60, 140, 200, and 75. The 100 indicates that the program should output all integers less than or equal to 100, so the program outputs 50, 60, and 75.

# Such functionality is common on sites like Amazon, where a user can filter results.


my_list = list()
my_list_len = int(input())

for n in range (0, my_list_len):
    my_list.append(int(input()))

user_val = int(input())

for n in my_list:
    if n <= user_val:
        print(n)
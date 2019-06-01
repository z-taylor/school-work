# Write a program whose input is a string which contains a character and a phrase, and whose output indicates the number of times the character appears in the phrase.

# Ex: If the input is:
# n Monday

# the output is:
# 1

# Ex: If the input is:
# z Today is Monday

# the output is:
# 0

# Ex: If the input is:
# n It's a sunny day

# the output is:
# 2

# Case matters.

# Ex: If the input is:
# n Nobody

# the output is:
# 0

# n is different than N.

## 

my_string = input()
my_char = my_string[0]
my_string = (my_string.replace(my_char, '', 1)).strip()
count = 0
  
for i in my_string: 
    if i == my_char: 
        count += 1
  
print (count)
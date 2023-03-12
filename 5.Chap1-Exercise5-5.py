# My own split and join:
# In this exercise create two functions:
# ✅ my_split : which splits sentence given as first argument using second argument as a separator character to separate list items. Function returns a list of items.
# ✅ my_join : which joins list given as first argument to a string separated with character given as second argument. Function returns a string.
# 🚨In this exercise you are not allowed to use Python split and join functions.

# Write your code below this line 👇


# Define my_split function:
def my_split(s, sep=' '):
    s = s.lstrip(sep)
    if sep in s:
        pos = s.index(sep)
        found = s[:pos]
        remainder = my_split(s[pos + 1:])
        remainder.insert(0, found)
        return remainder
    else:
        return [s]


# Define my_join function:
def my_join(my_split, delimiter):
    string = str(my_split.pop(0))
    while my_split:
        string += delimiter + str(my_split.pop(0))
    return string


# 🚨 Don't change the code below 👇
sentence = str(input("Please enter sentence: "))
print(my_join(my_split(sentence, ' '), ','))
print(my_join(my_split(sentence, ' '), '\n'))

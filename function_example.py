def my_func(param1="default"):
    """
    THIS IS THE DOCSTRING
    :param param1:
    :return:
    """
    print("Hello world from my first Python function: {}!".format(param1))


my_func()


def add_num(num1, num2):
    """
    THIS IS A SIMPLE ADDITION FUNCTION
    :param num1:
    :param num2:
    :return:
    """
    return num1+num2


var = add_num(2, 3)
print("var is: ", var)
var = add_num("2", '3')
print("var is: ", var)
# This shows that Python doesn't care about the types of the input


def add_num_type_checking(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1 + num2
    else:
        return "I need integers."


var = add_num_type_checking(2, 3)
print("var is: ", var)
var = add_num_type_checking("2", '3')
print("var is: ", var)


my_list = [1,2,3,4,5,6,7,8,9]


def bool_even(num):
    return num % 2 == 0


evens = filter(bool_even, my_list)
print("evens is: ", list(evens))


# Lambda expression, aka anonymous function and just use Python keyword lambda
evens_2 = filter(lambda num: num % 2 == 0, my_list)
print("evens_2 is: ", list(evens_2))

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.
# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True


def array_check(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False


list1 = [1, 1, 2, 3, 1]
print("array_check result: ", array_check(list1))
list1 = [1, 1, 2, 4, 1]
print("array_check result: ", array_check(list1))
list1 = [1, 1, 2, 1, 2, 3]
print("array_check result: ", array_check(list1))


# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'


def string_bits(my_str):
    result = ""
    for i in range(len(my_str)):
        if i % 2 == 0:
            result = result + my_str[i]
    return result


print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if len(a) > len(b):
        return a[(len(a) - len(b)):] == b
    elif len(a) < len(b):
        return b[(len(b) - len(a)):] == a
    else:
        return a == b


print(end_other('Hiabc', 'abc'))  # True
print(end_other('AbC', 'HiaBc'))  # True
print(end_other('abc', 'abXabc'))  # True


# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def double_char(my_str):
    result = ""
    for i in range(len(my_str)):
        result = result + my_str[i]
        result = result + my_str[i]
    return result


print(double_char("The"))
print(double_char("AAbb"))
print(double_char("Hi-There"))


# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
    teen = range(13, 20)
    if a in teen:
        a = fix_teen(a)
    if b in teen:
        b = fix_teen(b)
    if c in teen:
        c = fix_teen(c)
    return a + b + c


def fix_teen(n):
    if n == 15 or n == 16:
        return n
    else:
        return 0


print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))


# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    even_nums = list(filter(lambda n: n % 2 == 0, nums))
    return len(even_nums)


print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))

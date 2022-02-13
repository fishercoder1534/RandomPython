def add(*args):
    """
    This shows one use of * in Python: it indicates this function takes in non-key argument and a variable length of arguments
    :param args:
    :return:
    """
    return sum(args)


print(add(1, 2, 3, 4, 5))


def print_food(**kwargs):
    """
    Here double asterisk( ** ) is also used as **kwargs, the double asterisks allow passing keyword argument.
    This special symbol is used to pass a keyword arguments and variable-length argument list.

    Keyword arguments (or named arguments) are values that, when passed into a function,
    are identifiable by specific parameter names.
    A keyword argument is preceded by a parameter and the assignment operator, = .

    Keyword arguments can be likened to dictionaries in that they map a value to a keyword.
    :param kwargs:
    :return:
    """
    for items in kwargs:
        print(f"{kwargs[items]} is a {items}")


print(print_food(fruit ='cherry', vegetable ='potato', boy ='srikrishna'))

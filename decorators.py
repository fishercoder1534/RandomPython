s = 'GLOBAL VARIABLES'


def simple_func():
    """
    locals() and globals() are two convenient Python built in function calls.
    """
    my_local_var = 10
    print(locals())
    print(globals()['s'])
    print("All global variables are: ", globals())


simple_func()


def hello(name="Steve"):
    return "Hello " + name


print(hello())


def hello_2(name="Steve"):
    print("The hello_2() function has been run!")

    def greet():
        return "This string is inside greet()"

    def welcome():
        return "This string is inside welcome()"

    if name == "Steve":
        return greet()
    else:
        return welcome()


x = hello_2()

print(x)


def hello_3():
    return "Hi Steve"


def other(func):
    """
    we could pass in func to denote this function takes in another function as a parameter!!!
    :param func:
    :return:
    """
    print("Hello")
    print(hello_3())


other(hello_3())


def new_decorator(func):

    def wrap_func():
        print("Code here before executing func()")
        func()
        print("Func() has been called")

    return wrap_func


@new_decorator
def func_needs_decorator():
    print("This function is in need of a decorator!")


# This below line could be replaced by using @new_decorator on the function
# func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()

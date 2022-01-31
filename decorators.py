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

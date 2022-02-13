def create_cubes(n):
    """
    This is a traditional way of generating sequences, not super memory efficient as it'll generate all values once and store them in memory
    :param n: n
    :return:
    """
    result = []
    for x in range(n):
        result.append(x**3)
    return result


for x in create_cubes(10):
    print(x)


def create_cubes_yield_approach(n):
    """
    This is using a more memory efficient way of creating sequences: yield
    :param n:
    :return:
    """
    for x in range(n):
        yield x**3


for x in create_cubes_yield_approach(10):
    print(x)


def gen_fibo_traditional_approach(n):
    a = 1
    b = 1
    output = []
    for i in range(n):
        output.append(a)
        a, b = b, a + b
    return output


for x in gen_fibo_traditional_approach(10):
    print(x)


def gen_fibo_yield_approach(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


for x in gen_fibo_yield_approach(10):
    print(x)


def simple_gen():
    for x in range(3):
        yield x


for number in simple_gen():
    print(number)

g = simple_gen()
print(g)
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) # this will throw StopIteration error


s = 'hello'
# for letter in s:
#     print(letter)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(s_iter.__next__())
print(s_iter.__next__())
# print(s_iter.__next__())

# Tuples are immutable just as Strings
my_tuple = (1, 2, 3)
print(my_tuple[0])

try:
    my_tuple[0] = 'something new'  # this is going to throw errors
except TypeError:
    print("Caught TypeError.")

my_tuple_list = [(1,2),(3,4),(5,6)]
for t in my_tuple_list:
    print("t is: ", t)

for (t1, t2) in my_tuple_list:
    print("t1 is: ", t1)
    print("t2 is: ", t2)

for t1, t2 in my_tuple_list:
    print("t2 is: ", t2)
    print("t1 is: ", t1)

# while lists and dictionaries are mutable and accept assignments
my_list = [1, 2, 3]
print(my_list[0])
my_list[0] = 4
print(my_list[0])

# Sets, similar to a dict, it uses {} when printing out
my_set = set()
my_set.add(1)
my_set.add(0.01)
my_set.add(12.98)
my_set.add(1)
my_set.add(3)
my_set.add(2)
print("my_set: ", my_set)

uniq = set([1, 1, 1, 1, 1, 2, 2, 2, 2, 4, 4, 4, 4, 3, 3, 3, 3])
print("uniq: ", uniq)

for i in range(5):
    print("i is: ", i)


# The tuple() builtin can be used to create tuples in Python.
# In Python, a tuple is an immutable sequence type.
# One of the ways of creating tuple is by using the tuple() construct.
t1 = tuple()
print('t1 =', t1)

# creating a tuple from a list
t2 = tuple([1, 4, 6])
print('t2 from a list =', t2)

# creating a tuple from a string
t1 = tuple('Python')
print('t1 from a string =', t1)

# creating a tuple from a dictionary
t1 = tuple({1: 'one', 2: 'two'})
print('t1 from a dict =', t1)

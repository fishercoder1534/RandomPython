# How to run this program:
# In terminal, run $python3 dict.py

print("Hello world!")

my_dict = {"key1": 123, "key2": "a_string", "key3": 123.32,
           "key4": {'123_321': ['abc', 1, True, 'grabMe']}}
print("first_item: ", my_dict['key1'])
print("second_item: ", my_dict['key2'])
print("third_item: ", my_dict['key3'])
print("fourth_item: ", my_dict['key4'])
print("a cool item is: ", my_dict['key4']['123_321'][3])
print("my_dict: ", my_dict)

# dict is mutable
my_dict['key1'] = 456
print("my_dict: ", my_dict)
my_dict['key5'] = 'new item'
print("my_dict: ", my_dict)

print("Program finished!")

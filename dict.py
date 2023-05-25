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


def main():
    print("Hello World!")
    r_key = "123"
    metric_name = "great_metric"
    validation_result_dict = {r_key: ("good", "")}
    update_dict = {r_key: ["bad", "bad_{}".format(metric_name)]}
    validation_result_dict.update(update_dict)
    print("validation_result_dict is: {}".format(validation_result_dict))


if __name__ == "__main__":
    main()

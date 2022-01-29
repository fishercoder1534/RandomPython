# How to run this program:
# In terminal, run $python3 hello.py

print("Hello world!")

txt = "Viel Glück!"
print("Before encoding, txt: ", txt)
print("After encoding with UTF-8, x: ", txt.encode())  # without specifiying encoding scheme, UTF-8 is used

print("After encoding with ascii, x: ", txt.encode(encoding="ascii",errors="namereplace"))

# for _ in range(10):
#     print("Hello world!")

my_list = [1, 2, 3]
print("Before assignment, my_list: {}".format(my_list))

my_list = ["New Item", 2, 3]
print("After assignment, my_list: {}".format(my_list))

print("Program finished!")

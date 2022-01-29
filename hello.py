# How to run this program:
# In terminal, run $python3 hello.py

print("Hello world!")

txt = "Viel Glück!"
print("Before encoding, txt: ", txt)
print("After encoding with UTF-8, x: ", txt.encode())  # without specifiying encoding scheme, UTF-8 is used

print("After encoding with ascii, x: ", txt.encode(encoding="ascii",errors="namereplace"))

# for _ in range(10):
#     print("Hello world!")

s = 'django'
print(s[0])
print(s[-1])
print(s[:4])
print(s[1:4])
print(s[4:])

var = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# [] means a list, {} means a dict,
# so there is list inside the dict and inside list and inside dict. ^ ^
print("printing out var from nested dict: ", var['k1'][0]['nest_key'][1])

print("Program finished!")

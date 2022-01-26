# How to run this program:
# In terminal, run $python3 hello.py

print("Hello world!")

txt = "Viel Glück!"
print("Before encoding, txt: ", txt)
print("After encoding with UTF-8, x: ", txt.encode())  # without specifiying encoding scheme, UTF-8 is used

print("After encoding with ascii, x: ", txt.encode(encoding="ascii",errors="namereplace"))

print("Program finished!")

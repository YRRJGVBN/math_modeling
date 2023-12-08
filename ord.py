text = "Hello"
 
for symbol in text:
    print(ord(symbol), end="; ")

    codes = [119, 111, 114, 108, 100]
symbols = ""

print()

for code in codes:
    symbols += chr(code)
 
print(symbols) 
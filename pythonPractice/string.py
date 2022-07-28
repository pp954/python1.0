a = """jcdnasvjavja
jvaajsvdasjv
jvnasjdvoakdsvolk"""
print("\n", a)

a = '''kasdnvakv
vnakrvav'''

print("\n", a)

print("extract one character of the string.")
x = "apple"
print("\n", x[2])

print("loop through the string")
for i in x:
    print("\n", i)

print()
y = "Hello,world!"
print("\nlength of the string", len(y),"\n")

print("to check if a certain phrase or character is present in a string")
txt="the best things in life are free!"
print("free" in txt)
print("\n","apple" not in txt)

if "free" in txt:
    print("\nyes, 'free' is present.")

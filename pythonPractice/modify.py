a=" Hello,World! "
print(a.upper())
print("\n",a.lower())
print("\n",a.strip()) #removes whitespace and returns "Hello,World"
print("\n",a.replace("H","J")) #replace H with J
print("\n",a.split(",")) #returns[' Hello','World! ']
a="Mary"
b="Con"
print("\n",a+b) #string concatenation
print("\n",a+" "+b)

#format strings
txt = "My name is PP. I am {} years old."
print("\n",txt.format(20)) # My name is PP. I am 20 years old.
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))#I want to pay 49.95 dollars for 3 pieces of item 567.





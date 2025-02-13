
# 1. creation and modification of strings
# str()

a =344
b=type(a)
print(b)
print(str(a))   # 344

#upper()

a="hello"
print(a.upper())  # HELLO   #converts all the letters to upper case

#lower()

a="HELLO"
print(a.lower())  # hello   #converts all the letters to lower case

a= "hello world"
print(a.capitalize()) # capitalize the first letter

#title()
a="hello world"
print(a.title())  # Hello World

#strip()
a=" hello world "
print(a.strip())  # hello world
#searching and replacing strings
#find()
a="hello world" 
print(a.find("world"))  # 6 #returns the index of the first occurence of the substring

#replace()
a="hello world"
print(a) # hello world
print(a.replace("world","python")) # hello python

#count 
a="banana"
print(a.count("a"))#counts occurrences of substring

#startswith()
a="hello world"
print(a.startswith("hello")) # True

#endswith()
a="hello world"
print(a.endswith("world")) # True

# 3. splitting and joining strings
#split()
a="a,b,c,d"
print(a.split(",")) # ['a', 'b', 'c', 'd']

#join()
a=["a","b","c","d"]
print(",".join(a))  # a,b,c,d   #joins the elements of the list with the string

#partition 
a = "hello world"
print(a.partition(" ")) #splits a string into three parts: before, separator , after.

#splitnes
a="hello\nworld"
print(a.splitlines()) #splits astring by line breaks.

# 4. string validation 

# isalpha()
a="hello"
print(a.isalpha()) # True

#isdigit()
a="123"
print(a.isdigit()) # True

#isalnum()
a="hello123"
print(a.isalnum()) # True

#isspace()
a=" "
print(a.isspace()) # True
#islower()
a="hello"
print(a.islower()) # True
#isupper()
a="HELLO"
print(a.isupper()) # True
#istitle()
a="Hello World"
print(a.istitle()) # True

# 5. formatting strings
#format()
a="hello"
b="world"
print("{} {}".format(a,b)) # hello world

#f-string
a="hello"
b="python"   
print(f"hello,{b}") # hello python

#6. string Alignment
#ljust()
a="hello"
print(a.ljust(10,"-")) # hello -----
#rjust()
a="hello"
print(a.rjust(10,"-")) # -----hello
#center()
a="hello"
print(a.center(10,"-")) # --hello---

#7. string encoding and decoding
#encode()
a="hello"
print(a.encode()) # b'hello'
#decode()
a=b'hello'
print(a.decode()) # hello
 
 #8. case swapping
#swapcase()
a="Hello World"
print(a.swapcase()) # hELLO wORLD


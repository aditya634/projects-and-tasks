# String Function : 

print("\ncapitalize : ")
# capitalize function -> Make the first letter in uppercase of the string

str="My name is KHAN, I am the KING."
capitialized = str.capitalize()
print(capitialized)     # OUTPUT : My name is khan, i am the king !


print("\nisupper : ")
# isupper function() -> check whether the string is in upper case or not

str1 = "hello"
str2 = "HELLO"
str3 = "HelLO"
print(str1.isupper())  # False
print(str2.isupper())  # True
print(str3.isupper())  # False

print("\nupper : ")
# upper() -> change the string to upper case

str1 = "hello"
str2 = "HELLO"
str3 = "HelLO"
print(str1.upper())  # HELLO
print(str2.upper())  # HELLO
print(str3.upper())  # HELLO


print("\nislower : ")
# islower function() -> check whether the string is in lower case or not

str1 = "hello"
str2 = "HELLO"
str3 = "HelLO"
print(str1.islower())  # True
print(str2.islower())  # False
print(str3.islower())  # False

print("\nlower : ")
# lower() -> change the string to lower case

str1 = "hello"
str2 = "HELLO"
str3 = "HelLO"
print(str1.lower())  # hello
print(str2.lower())  # hello
print(str3.lower())  # hello

print("\nswapcase : ")
# swapcase() -> It will convert the upper case into lower case & lower case into upper case

str1 = "My name is JOKER"
str2 = "Hello WorlD"
print(str1.swapcase())
print(str2.swapcase())

print("\ncount :")
#  count() -> Returns the number of times a specified value occurs in a string
# Also we can set the starting & ending point for searching
# Syntax : str.count(<string_to_search>,<start>,<end>)

str ="This is Boy"

print(str.count("is"))      # 2
print(str.count("is",3))    # 1
print(str.count("is",3,5))  # 0
print(str.count("id",3,5))  # 0


print("\nisalpha :")
# isalpha : it will check whether the given string have alphabets or not

str1 = "THESE are alphabets"
str2 = "This is special @,#,$,%,^,9,2,9"
str3 = "HelloWorld"
print("Alphabets only in str1 : ",str1.isalpha())   # False   
print("Alphabets only in str2 : ",str2.isalpha())   # False
print("Alphabets only in str3 : ",str3.isalpha())   # True


print("\nisalnum :")
# isalnum : it will check whether the given string have (alphabets and numbers) or not

str1 = "THESE are alphabets"
str2 = "This is special @,#,$,%,^,9,2,9"
str3 = "HelloWorld"
str4 = "HelloWorld1234"
str5 = "01234"
print("Alphabets only in str1 : ",str1.isalnum())   # False
print("Alphabets only in str2 : ",str2.isalnum())   # False
print("Alphabets only in str3 : ",str3.isalnum())   # True
print("Alphabets only in str4 : ",str4.isalnum())   # True
print("Alphabets only in str5 : ",str5.isalnum())   # True


print("\nisdigit :")
# isdigit : it will check whether the given string have numbers only or not

str1 = "THESE are alphabets"
str2 = "This is special @,#,$,%,^,9,2,9"
str3 = "HelloWorld"
str4 = "HelloWorld1234"
str5 = "01234"
print("Alphabets only in str1 : ",str1.isdigit())   # False
print("Alphabets only in str2 : ",str2.isdigit())   # False
print("Alphabets only in str3 : ",str3.isdigit())   # False
print("Alphabets only in str4 : ",str4.isdigit())   # False
print("Alphabets only in str5 : ",str5.isdigit())   # True


print("\nparition :")
# parition : this method searches for a specified string, and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.

str = "This is my food don't eat"
print(str.partition("my"))                          # ('This is ', 'my', " food don't eat")
print(str.partition("eat"))                         # ("This is my food don't ", 'eat', '')
print(str.partition("This is my food don't eat"))   # ('', "This is my food don't eat", '')


print("\njoin :")
# join(<tup>) : it takes all items in an iterable and joins them into one string.
tup1 = ("This is my food don't ", 'eat', '')
tup2 = ('', "This is my food don't eat", '')

print("String : "," ".join(tup1))   # String :  This is my food don't  eat
print("String : ","@".join(tup2))   # String :  @This is my food don't eat@
print("String : ","#".join(tup1))   # String :  This is my food don't #eat#


print("\nindex :")
# index : helps to find the location of the substring from the string
# Also we can set the starting & ending point for searching
# Syntax : str.count(<string_to_search>,<start>,<end>)
#     01234567890
str= "Hello world, welcome to my world"
print(str.index("welcome"))         # 7
# print(str.index("hello"))         # ERROR
print(str.index("Hello"))           # 0
print(str.index("world"))           # 6
print(str.index("world",7))         # 6
# print(str.index("world",7,20))    # ERROR
# print(str.index("world",-1))      # ERROR
# print(str.index("dlrow",-1))      # ERROR
# print(str.index("yellow"))        # ERROR


print("\nfind : ")
# find : finds the first occurrence of the specified value and if not found return -1.

str="Hello this is my world welcome to my world"

print(str.find("this"))         # 6
print(str.find("there"))        # -1
print(str.find("my",1,20))      # 14
print(str.find("my",-1,-20))    # -1 (Not Check for negative locations)


print("\nisspace :")
# isspcae : it will check whether the given string is space or not

str1 = "THESE are alphabets"
str2 = "This is special @,#,$,%,^,9,2,9"
str3 = "        "
str4 = "HelloWorld1234"
str5 = "01234"
print("Spaces only in str1 : ",str1.isspace())   # False
print("Spaces only in str2 : ",str2.isspace())   # False
print("Spaces only in str3 : ",str3.isspace())   # True
print("Spaces only in str4 : ",str4.isspace())   # False
print("Spaces only in str5 : ",str5.isspace())   # False


print("\nstrip, lstrip, rstrip :")
# strip : Remove spaces at the beginning and at the end of the string:
# lstrip : Remove spaces at the left side of the string
# rstrip : Remove spaces at the right side of the string
str1 = "       this    is     world     "
str2 = "   this iis     "
print("Trimmed str1 : ",str1.strip(),"!")   # False
print("Trimmed str2 : ",str2.strip(),"!" )  # True

print("Left Trimmed str1 : ",str1.lstrip(),"!")   # False
print("Left Trimmed str2 : ",str2.lstrip(),"!")   # True

print("Right Trimmed str1 : ",str1.rstrip(),"!")   # False
print("Right Trimmed str2 : ",str2.rstrip(),"!")   # True


print("\nreplace :")
# replace : it will replace the given string into the required string
# also we can define how many changes we have to made using third parameter 

str="Open my computer on your computer , how can i open my computer on your computer"

print("computer replaces to PC : ",str.replace("computer", "PC"))
# Open my PC on your PC , how can i open my PC on your PC
print("computer replaces to PC : ",str.replace("computer", "PC",2))
# Open my PC on your PC , how can i open my computer on your computer


print("\ntitle :")
# title : Converts the first character of each word to upper case

str = "My name is KHAN, I am the KING"
print("Each word letter is in upper case : ",str.title())

str2 = "My Name Is Khan, I Am The King"
str3 = "My NAME Is Khan, I Am The King"
str4 = "My name Is Khan, I Am The King"
print("Is str2 in title format : ",str2.istitle())      # True
print("Is str3 in title format : ",str3.istitle())      # False
print("Is str4 in title format : ",str4.istitle())      # False


print("\nstartswith & endswith :")
# startswith , endswith :
# startswith : Returns true if the string start with the specified value
# endwith : Returns true if the string ends with the specified value

str="My name is khan"

print("Is str starts with My : ",str.startswith("My"))  # True
print("Is str starts with my : ",str.startswith("my"))  # False
print("Is str ends with Khan : ",str.endswith("Khan"))  # False
print("Is str ends with khan : ",str.endswith("khan"))  # True


print("\nisnumeric : ")
# isnumeric : Returns True if all characters in the string are numeric

str1="Hello 12345"
str2="12345"

print("Is all characters in str1 are in number form : ",str1.isnumeric())
print("Is all characters in str2 are in number form : ",str2.isnumeric())


print("\nisascii : ")
# isascii : Check if all the characters in the text are ascii characters

str1="Hello 12345"
str2="12345"

print("Is all characters in str1 are in number form : ",str1.isascii())
print("Is all characters in str2 are in number form : ",str2.isascii())


print("\nisdecimal : ")
# isdecimal : Returns True if all characters in the string are not decimals

str1 = "123"
str2 = "123.45"

print("Is str1 in decimal form :",str1.isdecimal())
print("Is str2 in decimal form :",str2.isdecimal())


print("\nlen :")
# len : Used to calculate the length of the string :

str="This is String"
tup1 = ("this","is","string")

print("Length of string :",len(str))
print("Length of tuple :",len(tup1))
print("Length of first element of tuple :",len(tup1[0]))
print("Length of string \"this\" :",len("this"))

print("\nzfill :")
# zfill : method adds zeros (0) at the beginning of the string, until it reaches the specified length.

str1 = "500"
str2 = "50"
str3 = "Hello"

print("Adding 0s to make length 10 in str1 : ",str1.zfill(10))
print("Adding 0s to make length 10 in str2 : ",str2.zfill(10))
print("Adding 0s to make length 10 in str3 : ",str3.zfill(10))
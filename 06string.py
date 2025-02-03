name="rohit singh"
guru='Radhe Radhe'
print(name,guru)

#how to print "he said,"i want to eat an apple "

print("he said,\"i want to eat an apple ")
print('he said,"i want to eat an apple ')

#using triple quotes
triple='''Ek baar bolo,
sb Radhe Radhe,
radhe bolne sb negativity dur hote hi'''
print(triple)

print(triple[0])
print (triple[3])
print(triple[-1])
print(triple[-10])
print(triple[20])

#print on echaracte using loop
for character in name:
    print(character)


for i in name:
    print(i)


# string silicing
nam="Krishna, Radhe"
print(nam)

print(nam[0:7])

# add space in count
print(nam[0:11])

print(nam[0:14])
print(len(nam))
print(nam[:14])


fruit="mango"
print(len(fruit))

# negative silicing
print(fruit[-5:-2])
print(fruit[-5:])


#string are mutable
#string methods
a="rohit"
print(len(a))
print(a.upper())
print(a)
print(a.lower())
print(a)

#rstrip():removes any trialing characters

c="rohit ***"
print(c.rstrip("*"))

d="***rohit***"
print(d.strip("*"))

#split():the string method reeplaces all the occurrence of a string with another string
e="rohit rahul ravan"
print(e.split(" "))


#captalize: to captalize the method turn only the irst character

blogheading="rohit is good "
print(blogheading.capitalize())

#center method
str1="welcome to my blog"
print(str1.center(50))

#count method

str2="welcome to my blog"
print(str2.count("o"))

#find=return the first occurences of element not found then return -1

str3="My name is rohit raj"
print(str3.find('is'))
print(str3.find("ishh"))

print(str3.index('is'))

#isalpha():The isalpha() method checks if all characters in a given string are alphabetic. It returns True if every character in the string is a letter and False if the string contains any numbers, spaces, or special characters.
str4="Rohitr08"
print(str4.isalpha())
str5="rohit"
print(str5.isalpha())
str6="1234"

#isalnum():check the number of string letter
print(str6.isalnum())
#islower():return all lowercase are true then false
#isprintable():return given string are printable true otherwise false.
str7="radhe radhe"
print(str7.isprintable())
str8="radhe   radhe "
print(str8.isprintable())

str9="radhe radhe\n"
print(str9.isprintable())

#isspace=if only contain white space then true otherwise false
str10="radhe Rradhe radhe radhe radhe radhe"
print(str10.isspace())
str11=" "
print(str11.isspace())

#istitle= if only true the first letter of are capital otherwise false

str12="World"
print(str12.istitle())
str13="Rohit is Godd boy"
print(str13.istitle())

#swapcase=convert lower to upper to lower
#title=convert into capital letter
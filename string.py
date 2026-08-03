"""# sting - slicing

name = "tonmoy mohajan"

print(name[0:7])
print(name[::-1])


fruit = "mango"
print(fruit[-3:-1])


# looping throgh the string

name = "tonmoy"
for character in name:
    print(character)

# string upper and lower

name = "tonmoy"
print(name.upper())
print(name.lower())

# rstrip

gun = "AK47!!!"
print(gun.rstrip("!"))
"""

"""# replace

gun = "AK47"

print(gun.replace("AK47", "Ump"))

# split

name = "tonmoy mohajan 01"

print(name.split())

# capitalize

blog = "introduction to string"

print(blog.capitalize())

# center

name = "tonmoy"

print(name.center(25))

# count

number = "11111"

cou = number.count("1")
print(cou)

# endswith()

str1 = "welcome to the console !!!"
print(str1.endswith("!!!"))

str1 = "welcome to the console !!!"
print(str1.endswith("to", 4, 10))

# find()

str1 = "hello guys"

print(str1.find("guys"))
"""
# isalnuam

str1 = "hello guys"

print(str1.isalnum())

# isalpha()

str1 = "hell00"

print(str1.isalpha())

# is lower()

pr = "hello world"
print(pr.islower())

# printable()

pr = "hello \n"
print(pr.isprintable())

# isspace()

pr = "      "
print(pr.isspace())

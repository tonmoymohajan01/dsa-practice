from array import *
value = array('i',[1,2,3,4,5,6])
for i,x in enumerate(value):
    if i < len(value)-1:
        print(x,end = " , ")
    else:
        print(x,end = " ")

print("\n")

value1 = array('d',[1.4,2.3,4.5,6.7,8.9,5.6])
for i in value1:
    print(i)

print("\n")

character = array('u',["a","b","c","d","e"])
for x in character :
    print(x)

print("\n")

#print type code 

Roll_Number = array('i',[1,2,3,4,5])
result = Roll_Number.typecode
print(result)

print("\n")

# array reverse 

Roll_Number = array('i',[1,2,3,4,5])
Roll_Number.reverse()
for x in Roll_Number:
    print(x,end = " ")

print("\n")

#data insert , append 

Roll_Number = array('i',[1,2,3,4,5])
Roll_Number.insert(2,6)
Roll_Number.append(100)
Roll_Number[2] = 60
print(Roll_Number)

print("\n")

#copy array 

Roll_Number = array('i',[1,2,3,4,5])
copy_array = array(Roll_Number.typecode,(x*3 for x in Roll_Number))
for i in copy_array:
    print(i)

print("\n")

#pop array 


Roll_Number = array('i',[1,2,3,4,5])
Roll_Number.pop(3)
print(Roll_Number)

print("\n")

#array slicing 

val = array('i',[1,2,3,4,16,6,7])
new_value = val[2:5]
print(new_value)

print("\n")

val1 = array('i',[1,2,3,4,16,6,7])
new_value = val1[0:-2]
print(new_value)

#reverse easily 

val3 = array('i',[1,2,3,4,16,6,7])
new_value = val3[::-1]
print(new_value)

print("\n")

#array append user 

number = array("i",[])
input_length = int(input("enter the first number :"))
for i in range(0,input_length):
    number.append(int(input("enter the user vlaue :")))
print(number)

print("\n")

#vlaue search 

value = array('i',[1,2,34,5])
search_value = value.index(34)
print(search_value)

print()

#Numpy import 

from numpy import *

#Linspace 
val = linspace(10,20,5)
for x in val:
    print(x)


#Arange
val = arange(10,20,5)
for x in val:
    print(x)

#logspace 

val = logspace(1,3,2)
for x in val:
    print(x)

#array stored in zero
number = zeros(10)
for x in number :
    print(x)

#array stored in one
number = ones(10)
for x in number :
    print(x)

#array stored in any value
number = full(10,5)
for x in number :
    print(x)

Two_dimensional_array = array([[1,2,3],[4,5,6],[7,8,9]])
print(Two_dimensional_array)

three_dimensional_array = array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(three_dimensional_array)

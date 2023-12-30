# print("hello world")
# print("hello rohit")

# name = "Rohit"
# age = 22

# # print(name, age)

# # now we can update the variable
# name = "ankit"
# age = 23.04

# print(name, age)

# is_active = False
# print(is_active + 1)


# # Assignment assignment
# first_name = "Tony "
# last_name = "Stark"
# age = 51
# is_genius = True

# print(first_name + " " + last_name)
# print(first_name + "'s" , age)
# print(is_genius)


# ALL INPUT STORED AS STRING IN PYTHON
# all_input = input("what is your name or enter your name:- ")
# print("hello" + " " + all_input)
# print(type(all_input))


# #type conversion
# int()
# float()
# str()
# bool()



# old_age = input("enter your age: ")
# new_age = int(old_age) + 2
# print(new_age)



# x = input("enter :")
# y = int(x)
# z = bool(x) + bool(y)
# print(z)
# print(type(x))
# print(type(y))
# print(type(z))

# inp = input("enter the any number : ")
# print(type(inp))
# # a = int(inp)
# # print(type(a))

# a = float(inp)
# print(type(a))
# print(a)



# #print sum of two numbers
# a = input("enter the first number: ")
# b = input("enter the second number: ")

# sum = int(a) + int(b)
# print("sum of two numbers is " , sum)



#STRINGS

# name = "RohIT BHArti"
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name)


# name = "RohIT BHArti"
# print(name.find('I'))
# print(name.find('i'))
# print(name.find('Bharti'))
# print(name.find('BHArti'))



# name = "Rohit Bharti"
# print(name.replace('Rohit Bharti',"Virat Kohli"))
# print(name.replace('Bharti',"Sharma"))
# print(name.replace('i',"Sharma"))
# # name = "Replace"
# print(name)
# print("R" in name)
# print("z" in name)
# print("rohit" in name)
# print("Rohit" in name)



# # Arithmetic operators
# print(5+2)
# print(5-2)
# print(5*2)
# print(5 / 2)
# print(5 // 2)
# print(5 % 2)
# print(5 ** 2)

# reult = 2+2*3
# print(reult)

# reult = 2+2/3
# print(reult)




# #Comparision
# print(3 == 3)
# print(3 == (2+1))
# print(3 != 3)


# #Logical Operators
# print(3>5 or 2>1)
# print(3>5 and 2>1)
# print(not 2>1)
# print(not 3>5 and 2>1)


# # age = 24
# age = int(input("enter you age: "))

# if age >= 18:
#     print("you are adult")
#     print("you can vote")

# elif age >= 3 and age < 18:
#     print("you are school going boy")

# else:
#     print("you are children")




# # Calculator
# first = int(input("enter first number:-"))
# operator = input("enter operator like +,-,*,/,%: ")
# second = int(input("enter second number:-"))

# # or
# # first = int(first)
# # second = int(second)

# if operator == "+":
#     print("sum of given numbers is : ", (first + second))

# elif operator == "-":
#     print(first - second)

# elif operator == "*":
#     print(first * second)

# elif operator == "/":
#     print(first / second)

# elif operator == "%":
#     print(first % second)

# else:
#     print("unknown operator")






# #while loop

# # i = 1
# # while i<=10:
# #     print(i)
# #     i +=1

# # i = 1
# # while i<=5:
# #     print(i * "*")
# #     i +=1

# i = 10
# while i>0:
#     print(i * "*")
#     i -=1






# rang = range(5)
# print(rang)


# for i in range(5):
#     print(i)

# for item in range(5):
#     print((item + 1 ) * "*")



#List
# marks = [99,22,3,4,5,6,7,8,9,10,11,12,13,"rohit","ankit"]
# print(marks)

# print(marks[0])
# print(marks[5])
# print(marks[-1]) #-1 is for last
# print(marks[-2]) #-2 second last

# print(marks.index(3)) #index of
# print(marks.index("rohit"))

# print(marks[0:2]) #2 not include
# print(marks[3:10])
# print(marks[0:(len(marks)+1)])

# #infinite loop
# i = 1
# while i <= 5:
#     print(1)
    


# marks = [99,22,3,4,5,6,7,8,9,10,11,12,13,"rohit","ankit"]
# for score in marks:
#     print(score)


# marks = [99,78,94]

# #using APPEND add marks from end
# marks.append(100)
# marks.append("rohit")


#add on particular index then use INSERT
# marks.insert(0, 45)
# marks.insert(1, 100)
# print(marks)

#CHECKING
# print(100 in marks)

# marks = [99,78,94]

# print(len(marks))

# i = 0
# while i < len(marks):
#     print(marks[i])
#     i = i+1


# marks = [99,78,94]
# marks.clear()
# print(marks)


# students = ["rohit","rahul", "ankit", "mohan", "mohit","subhash"]

# print("Break...")
# for student in students:
#     if(student == "ankit"):
#         break; #break the loop when ankit found as a student
#     print(student)

# print("Continue...")

# for student in students:
#     if(student == "mohan"):
#         continue; #run the loop again when a student name's mohan
#     print(student)


#TUPLE
#cannot modify(delete/update)
# marks = 98,88,66,1,2,3,4,99,1,2,3,4,99,99  #this is also called tuple

# # marks = (98,88,66,1,2,3,4,99,1,2,3,4,99,99)
# # marks[0] = 100
# print(marks.count(99))
# print(marks.index(99))
# print(marks)


# [] = list => ARRAY
# () = tuple
# {} = sets -> unique value store

# marks = {1,2,3,4,4,5,2,3,4}

# for mark in marks:
#     print(mark)










# #DICTIONARY => OBJECT

# marks = {
#     "english" : 97,
#     "maths" : 96,
#     "hindi" : 97,
#     "science" : 100
# }
# print(marks)
# print(marks["hindi"])

# #ADD
# marks["social science"] = 92
# print(marks)

# #update 
# marks["social science"] = 96
# print(marks)




#FUNCTION

# 1) in-built functions => int(), float(), string(), bool()
# 2) module functions => math
# 3) user-defined functions => UserDefinedFunction

# import math
# print(dir(math))

# from math import sqrt
# print(sqrt(16))

# #if you needed all functions then use *
# from math import *
# print(sqrt(3))




# def finction_one(a,b):
#     sum = a + b
#     print(sum)

# finction_one(2,3)


def finction_one(first, second = 25):
    sum = first +  second
    print(sum)

finction_one(32,33)
finction_one(32)
finction_one(100)
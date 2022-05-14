
# grade = 90
# condition = grade >=90

# if condition:
#     # execute when true
#     print("Your grade is A")
# else:
#      # execute when False
#      print("Your grade is not A")


# import numbers


# num1 = eval(input("Enter the first number: "))
# num2 = eval(input("Enter the second number: "))
# try:
#     print("1", isinstance(num1,str))
#     print("2", isinstance(num1,str))
#     if isinstance(num1, str) or isinstance(num2, str):
#          print("Data type not allowed! Please specify a numerica is true")
#     else:
#         if num1 > num2:
#             largerVal = num1
#         else:
#             largerVal = num2

# print("The larger value is " + str(largerVal))
# except:
#     print("Data not allowed!")

# answer = eval(input("How many gallons does a ten gallon hat hold"))

# if (.5 <= answer <= 1):
#     print("Good, ", end="") # Good, it holds about 3/4 of a gallon
# else:
#     print("No, ", end="")# No, it holds about 3/4 of a gallon
# print("it holds about 3/4 of a gallon")

# first_num= eval(input("Enter first number"))
# second_num= eval(input("Enter second number"))
# third_num= eval(input("Enter third number"))

# max = first_num


# if second_num > max:
#     max= second_num
# if third_num > max:
#     max = third_num
# print("The largerst number of three number is" + str(max)+".")

# numbers = [1,20, 90]

# print(max(numbers))

from contextlib import redirect_stderr
from queue import Empty


# numbers = []

# first_num= eval(input("Enter first number"))
# numbers.append(first_num)
# second_num= eval(input("Enter second number"))
# numbers.append(second_num)
# third_num= eval(input("Enter third number"))
# numbers.append(third_num)
# msg= "The largerst number of three number is" + str(max(numbers))+"."
# print(msg)



# color = input ( "Enter a color ( BLUE or RED) : ")
# mode = input ("Enter a mode (STEADY or FLASHING): ")
# color = color.upper()
# mode = mode.upper()

# result = ""

# if color == "BLUE":
#     if mode == "STEADY":
#         result = "Clear View."
#     else: # mode is FLASHING
#         result = "CLouds Due"
# else: #Color is RED
#         if mode == "STEADY":
#             result = "Rain Ahead"
#         else: #mode is FLASHING
#             result = "Snow Ahead."
# print("The weather forecast is", result)



# #Evalaute profit
# # Obtain input from user
# costs = eval(input("Enter total costs:"))
# revenue = eval(input("Enter total revenue: "))
# # Determine and display profit or loss
# if costs == revenue:
#     result = "Break even"
# else:
#     if costs< revenue:
#         profit = revenue - costs
#         result = "Profit is ${0:...2f}.".format(profit)
#     else:
#         loss = costs - revenue
#         result = "Loss is ${0:...2f}.".format(loss)
# print(result)



## Bestow graduation honors
# Requesr grade point average 

# gpa = eval( input('Enter your gpa: '))
# # Determine if honors are warranted
# if gpa >= 3.9:
#     honors = " summa cum laude"
# elif gpa >= 3.6:
#     honors = "magna cum laude"
# elif gpa >= 3.3:
#     honors = "cum luade"
# else:
#     honors = "."
#     # Display conclusion
# print(" You graduated" + honors)

# ## Request two numbers and find their sum. Validate the input
# num1= input("Enter first number: ")
# num2 = input("Enter second number: ")
# # Display sum if entries are valid Otherwise, inform
# # the user where invalid entries were made
# if num1.isdigit() and num2.isdigit():
#     print("The sum is " , str(eval(num1)+ eval(num2))+ ".")
# elif not num1.isdigit():
#     if not num2.isdigit():
#         print("Neither entry was a proper number.")
#     else:
#         print("The first entry was not a proper number.")
# else:
#         print ("The second entry was not a proper number.")

# if 7:
#     print("This will run..")
# if[]:
#     print("This will not run...")
# if [1,2,99]:
#     print("This will run...")
# if True:
#     print("This will run...")
# if False:
#     print("This will not run...")

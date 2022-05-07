
# i = 0 # iterator / incrementor 
# while i < 10:
#     print("Hello World! " +str(i)) 
#     i += 1 # i = i + 1


# num =1 
# while num <= 5:
#     print(num)
#     num += 1 # Increase the value of num by 1.

# print("The program displays a famous movie quotations.")


# resps = ("1","2","3")
# resp = "0"

# while resps not in resps:
#     resp = input ("Enter 1, 2 or 3 : ")
#     if resp == "1" :
#         print("Plastic.")
#     elif resp == "2" : 
#         print("Rosebud " )
#     elif resp == "3" :
#         print("This's all folks.")


# from functools import total_ordering


# count = 0 
# totla = 0

# print("(Enter -1 to terminate program)")

# num = eval(input("Enter a nonnegative number: "))#5
# min = num 
# max = num

# while num != -1:
#     count += 1 
#     total += num
#     if num < min:
#         min = num
#     if num > max:
#         max = num
#     num = eval(input("Enter a nonnegative number: "))#5

# if count > 0:
#     print("Min: ",  str(min))
#     print("Max: ", str(max))
#     print("Average: ", str (total / count))
# else:
#     print("No nonnegative numbers were entered")

# list1 = [300, 1, 2, 3, 60]
# list1.sort() # [1,2,3,60,,300]

# list1[0] #1 Lowest number in the list
# list1[-1]#300 - Largest Number in the list

# from re import I


# I = 0 
# balance = eval (input("Enter initial deposit: "))
# rate = eval(input( "Enter the amount rate of return: "))
# while balance < 1000000:
#     break
#     balance += .04 * balance # balance = (balance * .04)
#     i +=1
# print("In ", str(i), "years you will have a million dollars.")


print("Enter a number from the menu to obtain a fact")
print("1. Capital")
print("2. National Bird")
print("3. National Flower")
print("4. Quit\n")
while True:
    num = int(input("Make a selection from the menu: "))
    if num == 1:
        print("Washinton,Dc is the capital of the United States")
    elif num == 2:
        print("The American Bald Eagle is the national bird.")
    elif num == 3:
        print("The rose is the national flower. ")
    elif num == 4:
        break 
    
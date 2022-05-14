# # # num1 = 1
# # # num2 = 10
# # # num3 = 1000
# # # sum_of_all_numbers = num1 + num2 + num3

# # # print("Sum is {0:n}".format(sum_of_all_numbers))

# # from pickletools import string1


# # list_of_numbers = [1, 10, 1000]

# # #print(sum(list_of_numbers))
# # print(list_of_numbers)  
# # list_of_numbers.clear()
# # print(list_of_numbers)  
# # list_of_numbers.append(100)
# # list_of_numbers.append(100)
# # list_of_numbers.append(100)
# # list_of_numbers.append(100)

# # list_of_numbers2=[3,100,5]

# # list_of_numbers.extend(list_of_numbers2)
# # print(list_of_numbers) 

# # l1=[1,32,4]
# # l2= [100,200,300]
# # l3= l1+l2
# # print(l3)

# # words = ["Spam", "Wink", "Hi","My", "In"]
# # words.insert(len(words),"Hello")

# # print("Words=======>")

# # grades = [] 
# # num = float(input("Enter the first grade:"))
# # grades.append(num)
# # num = float(input("Enter the Second grade:"))
# # grades.append(num)
# # num = float(input("Enter the third grade: "))
# # grades.append(num)
# # num = float(input ("Enter the fourth grade: "))
# # grades.append(num)
# # num = float(input("Enter the fifth grade: "))
# # grades.append(num)

# # grades.append(num)
# # minimumGrade = min(grades)
# # grades.remove(minimumGrade)
# # minimumGrade = min(grades)
# # grades.remove(minimumGrade)
# # average = sum(grades) / len(grades)
# # print("Average Grade: {0:.2f}".format(average))

# # grades.append(1)
# # grades.append(2)
# # grades.append(4)
# # grades.append(9)

# # print("grades",grades)

# # length = len(grades)
# # print("length",length)
# # print("sliced:",grades[0:2])


# #print("sliced:", grades[1:5])
# str1="a,b,c"
# parts = "a,b,c".split(",")

# print("parts: ", parts)
# lines = ("To", "Be", "or", "Not","to", "be")

# print("lines before join: ", lines)

# joined = " ".join(lines)

# print("joined ", joined)

# infile =  open("Data.txt","r")
# print("infine", infile)
# names= []
# #Using the for loop to populate the names array with names
# for line in infile:
#     names.append(line.rstrip())
# #Close the Data.txt file to presever memory 
# infile.close()
# names_using_list_comprehension = [line.rstrip() for line in infile]
# print("names_using_list_comprehension: ", names_using_list_comprehension
# infile.close()

# infile= open("Grades.txt","r")
# list_of_numbers = [eval(line)for line in infile]
# infile.close()

# list_of_names = ("Lucas", "John", ["A",(1, 2, 3), "C"])

# print("list_of_names", list_of_names[2][1][-1])

list1 = ["A", "B", "C"]
list2 = list(list1)
list2.append("D")
print(list1)

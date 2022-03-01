# from pickletools import string1


# print("one", "two", "three", sep= ",")

# print("Hello")  
# print("World!")


# print("a\tb\tc") # a  b   c
# print("a\tb\tc\nd\te\tf")


# print("\\Hello World!\\") # "Hello World!"
# ## Demonstrate justification of output
# print("123456789012345678901234567")
# print("Rank". ljust(5), "Player".ljust(20), "Hr" .rjust(3), sep="")
# print('1'. center(5), "Barry Bonds".ljust(20), "762".rjust(3), sep="")
# print('2'. center(5), "Hank Aaron".ljust(20), "755".rjust(3), sep="")
# print('3'. center(5), "Babe Ruth".ljust(20), "714".rjust(3), sep="")

# print("There are {0}% probability that the stock market will crash tomorrow and {1}% probablity that it will rally!".format(10,50))
# print((string1).foramt(10,50))

# print("0123456789012345678901234567")
# print("{0:^5s}{1:<20s}{2:>3s}".format("Rank","Player","HR"))
# print("{0:^5n}{1<20s}{2>3n}".format (1,"Barry Bonds", 762))
# print("{0:^5n}{1<20s}{2>3n}".format (2,"Hank Aaron", 755))
# print("{0:^5n}{1<20s}{2>3n}".format (3,"Babe Ruth", 714))
from pickletools import string1


print("The area of {0:s} is {1:,d} sqaure miles." .format("Texas",268820))
string1 = "The population of {0:s} is {1:2%} of the U.S. population."
print(string1.foramt("Texas", 26448000/ 309000000))
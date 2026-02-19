"""
# author: Vlad
# date: FEB 19
# 0.3 - Repetition Review Exercises
# """

# # Task 1: Write a program to calculate the factorial of any number that the user enters using a loop. Ex. 5! = 5*4*3*2*1 = 120
# # Your code goes here

# number = int(input("Please input the number: "))
# count = 0 
# value = 1  
# for i in range(number):
#     value = value * (number - count)
#     count += 1

# print(f"The factorial of {number}! is: {value}")


# # Task 2a: Write a program that asks for five marks and computes the average, rounded to 1 decimal place.
# # Your code goes here
# mark = 0 
# for i in range(5):
#     all = int(input("Enter grade: "))
#     mark = mark + all
    
# avarage =  mark / 5 
# print(f"The average grade is {avarage}%")
# # 2b)  Modify the program from task 2a to also output the lowest and highest mark WITHOUT lists.
# # Your code goes here
# lowest = 100
# highest = 0
# mark = 0 
# for i in range(5):
#     all = int(input("Enter grade: "))
#     mark = mark + all
    
#     if all > highest:
#         highest = all

#     if lowest > all:
#         lowest = all
    
    
# avarage =  mark / 5 
# print(f"The average grade is {avarage}%. The highest mark is {highest}% and the lowest mark is {lowest}% ")


# # 2c)  Modify the program from task 2b to check if the mark entered is between 0 and 100. Keep asking user for input until they give a valid grade.
# # Your code goes here
# lowest = 100
# highest = 0
# mark = 0 
# count = 0
    
# while(count !=5  ):
#     grade = int(input("Enter grade: "))
#     if   0 <= grade <= 100:
#         mark = mark + grade
#         if grade > highest:
#             highest = grade

#         if lowest > grade:
#             lowest = grade
#         count += 1
#     else:
#         print("Invalid mark")

# avarage =  mark / 5 
# print(f"The average grade is {avarage}%. The highest mark is {highest}% and the lowest mark is {lowest}% ")

"""
author: Vlad
date: FEB 19
0.3 - Repetition Review Exercises
"""

# Task 1: Write a program to calculate the factorial of any number that the user enters using a loop. Ex. 5! = 5*4*3*2*1 = 120
# Your code goes here

number = int(input("Please input the number: "))
count = 0 
value = 1  
for i in range(number):
    value = value * (number - count)
    count += 1

print(f"The factorial of {number}! is: {value}")


# Task 2a: Write a program that asks for five marks and computes the average, rounded to 1 decimal place.
# Your code goes here
mark = 0 
for i in range(5):
    all = int(input("Enter grade: "))
    mark = mark + all
    
avarage =  mark / 5 
print(f"The average grade is {avarage}%")
# 2b)  Modify the program from task 2a to also output the lowest and highest mark WITHOUT lists.
# Your code goes here
lowest = 100
highest = 0
mark = 0 
for i in range(5):
    all = int(input("Enter grade: "))
    mark = mark + all
    
    if all > highest:
        highest = all

    if lowest > all:
        lowest = all
    
    
avarage =  mark / 5 
print(f"The average grade is {avarage}%. The highest mark is {highest}% and the lowest mark is {lowest}% ")


# 2c)  Modify the program from task 2b to check if the mark entered is between 0 and 100. Keep asking user for input until they give a valid grade.
# Your code goes here
lowest = 100
highest = 0
mark = 0 
count = 0
    
while(count !=5  ):
    grade = int(input("Enter grade: "))
    if   0 <= grade <= 100:
        mark = mark + grade
        if grade > highest:
            highest = grade

        if lowest > grade:
            lowest = grade
        count += 1
    else:
        print("Invalid mark")

avarage =  mark / 5 
print(f"The average grade is {avarage}%. The highest mark is {highest}% and the lowest mark is {lowest}% ")


# 2d)  Modify the program to ask the user to enter -1 when done entering marks.
# Your code goes here


lowest = 100
highest = 0
mark = 0 
count = 0
    
while(count !=5  ):
    grade = int(input("Enter grade: "))
    if   0 <= grade <= 100:
        mark += grade
        if grade > highest:
            highest = grade

        if lowest > grade:
            lowest = grade
        count += 1
    elif grade == -1:
        all = count
        count = 5
    else:
        print("Invalid mark")

avarage =  mark / all 
print(f"The average grade is {avarage}%. The highest mark is {highest}% and the lowest mark is {lowest}% ")


# Task 3a) Determine the largest of n positive integers entered the user.
# The program should loop until a negative value is read (aka, use Sentinel Value).
# Your code goes here

highest = 0 
number = 0 
count  = 0
while(count !=1 ):
    number = int(input("Enter positive number: "))
    if number > highest:
        highest = number
    elif number == -1:
        count = 1

print(f" The highest number inputted is: {highest}")


# 3b) Modify the program to find the two largest integers.
# Your code goes here
largest = 0
second_largest = 0
count = 0


while (count !=1 ):
    number = int(input("Enter positive number: "))
   
    if number == -1:
        count = 1
    elif number > largest:
        second_largest = largest  
        largest = number          
    elif number > second_largest:
        second_largest = number          


print(f"The largest number inputted is: {largest}. The second largest number is {second_largest}")




# Task 4) Use the random module to choose a number between 1 and 100.
# Then print all the factors of that number.
# Ask the user if they wish to play again – loop until the user enters “No” (sentinel value).
# Your code goes here
import random


answer = input("Do you want to play the factor game? Type yes or no: ")


while answer.lower() != "no":
   
    num = random.randint(1, 100)
   
    for i in range(1, num + 1):
        if num % i == 0:
            print("The number", i, "is a factor of", num)
   
    answer = input("Do you want to play the factor game? Type yes or no: ")




# Task 5) One useful technique when analyzing a number is to use a loop and the modulus operator to extract each digit
# from the end.
# Consider this code:
count = 0
num = int(input("Enter a positive integer: "))


while (num >= 1):
    digit = num % 10
    if digit == 7:
        count += 1
    num = num // 10
   
print(f"Number of sevens:{count}")


# Use this above code to do the following:
# Count the number of sevens in a positive integer.

count = 0
num = int(input("Enter a positive integer: "))


while (num >= 1):
    digit = num % 10
    if digit == 7:
        count += 1
    num = num // 10
   
print(f"Number of sevens:{count}")


# Count the number of odd digits, and the number of even digits, in a positive integer.
odd= 0
even = 0
count = 0
num = int(input("Enter a positive integer: "))


while (num >= 1):
    digit = num % 10
    if digit % 2 == 0:
        odd += +1
    else:
        even +=1
    num = num // 10
   
print(f"There are {even } even digits and {odd} odd digits in this number." )








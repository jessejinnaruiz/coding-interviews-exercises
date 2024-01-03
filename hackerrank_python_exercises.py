#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the oddNumbers function below. Return a list of only the odd numbers between the two integers l & r.
def oddNumbers(l, r):
    list = []
    odds = []
    for num in range(l,r):
        list.append(num)
        num = num +1
    for element in list:
        if element % 2 == 0:
            continue
        else:
            odds.append(element)
    return odds


# print(oddNumbers(9, 16))

# Intro to Python practice problems on Hackerrank!
# Python if-else problem:
""" Given an integer, n, perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
"""

#!/bin/python3

import math
import os
import random
import re
import sys


# n = int(input().strip())
# if n % 2 != 0:
#     print('Weird')
# elif n % 2 == 0 and n in range(2,6):
#     print('Not Weird')
# elif n % 2 == 0 and n in range(6,21):
#     print('Weird')
# elif n % 2 == 0 and n > 20:
#     print('Not Weird')

# Arithmetic Operators
"""The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
"""

# if __name__ == '__main__':
# a = int(input())
# b = int(input())

def solution(a, b):
    print(a + b)
    print(a - b)
    print(a * b)

# solution(3, 2)

# Division 
"""Read two integers and print two lines. The first line should contain integer division,  // . The second line should contain float division,  / .
You don't need to perform any rounding or formatting operations.
"""
def division_solution(a, b):
    print(a // b)
    print(a / b)

# division_solution(9, 2)

# Loops
# Read an integer N. For all non-negative integers i < N, print i ** 2
def square_nonneg_integers():
    n = int(input())
    i = 0
    for element in range(n):
        print(i ** 2)
        i = i +1

# square_nonneg_integers()



# Write a function -- You are given the year, and you have to write a function to check if the year is leap or not.
"""In the Gregorian calendar three criteria must be taken into account to identify leap years:
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
"""

def is_leap(year):
    leap = False
    # print('This is leap evaluating as: ' + str(leap))
    # print('This is not leap evaluating as: ' + str(not leap))
    if year % 400 == 0:
        leap = not leap
    elif year % 100 == 0:
        leap = leap
    elif year % 4 == 0:
        leap = not leap

    return leap

# year = int(input())

# print(is_leap(year))


# Print function -- 
"""Read an integer N.
Without using any string methods, try to print the following: 123...N"""

# n = int(input())
def print_string_numbers(n):
    string = ''
    for i in range(1, n+1):
        string = string + str(i)
    return string

# print(print_string_numbers(n))


# Find the Runner-Up Score!
"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.
# """
# n = int(input())
# arr = map(int, input().split())
# print(n)
# print(arr)
def find_runner_up(scores):
    the_scores = []
    for element in arr:
        the_scores.append(element)
    the_max = max(the_scores)

    the_unique_scores = []
    for element in set(the_scores):
        the_unique_scores.append(element)

    sorted_list = sorted(the_unique_scores)
    return sorted_list[-2]

# print(find_runner_up(arr))

# List comprehensions
"""You are given three integers x, y and z representing the dimensions of a cuboid along with an integer N. 
You have to print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of (i + j + k) 
is not equal to N."""
# Example using loops:
# x = int(input()) 
# y = int(input()) 
# n = int(input()) 
# ar = [] 
# p = 0 

# for i in range( x + 1 ) : 
#     for j in range( y + 1): 
#         if i+j != n: 
#             ar.append([]) 
#             ar[p] = [ i , j ] 
#             p+=1 
# print(ar)

# Example using list comprehensions:
# x = int (input()) 
# y = int (input()) 
# n = int (input()) 
# print([ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )])

# solution!
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# print([ [i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if( (i + j + k) != n)])


# Nested lists
"""Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
"""
# gradebook = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     person = []
#     person.append(name)
#     person.append(score)
#     gradebook.append(person)

# scores = []
# for element in gradebook:
#     scores.append(element[1])
# second_lowest = sorted(list(set(scores)))

# for name, score in gradebook:
#     # print(name, score)
#     if score == second_lowest:
#         print(name)
# print(gradebook)
# for element in gradebook:
#     if element[1] == min(scores):
#         gradebook.remove(element)
#         scores.remove(element[1])
#         print(scores)
#     if element[1] == min(scores):
#         print(element[0])
# print(gradebook)

##################### STATS ###########################
# Day 0: Mean, Median, and Mode

# n = int(input())
# numbers = (input()).split(' ')
# numbers = [int(element) for element in numbers]
# sorted_numbers = sorted(numbers)
# # mean
# mean = sum(sorted_numbers)/n

# #median
# index_for_div = round(n/2)
# if n % 2 != 0:
#     median = (sorted_numbers[index_for_div])
# else:
#     median = ((sorted_numbers[index_for_div-1]+sorted_numbers[index_for_div])/2)

# #mode
# counts = {}
# for num in sorted_numbers:
#     counts[num] = counts.get(num, 0) + 1

# freq = 0
# mode = 0
# for val, count in counts.items():
#     if count > freq:
#         mode = val
#         freq = count 
#     elif count == freq and val < mode:
#         mode = val

# print(mean) 
# print(median)
# print(mode)

# Weighted mean

n = int(input())
scores = (input())
weights = (input())
scores_list = scores.split(' ')
weights_list = weights.split(' ')

scores_numbers = [int(element) for element in scores_list]
weights_numbers = [int(element) for element in weights_list]

weighted_scores = []
for score, weight in zip(scores_numbers, weights_numbers):
    weighted_score = score * weight
    weighted_scores.append(weighted_score)
weighted_mean = sum(weighted_scores)/sum(weights_numbers)
print(round(weighted_mean, 1))
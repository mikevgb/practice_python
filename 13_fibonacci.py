# -*- coding: utf-8 -*-

#  Write a program that asks the user how many Fibonnaci numbers to generate and
#  then generates them. Take this opportunity to think about how you can use 
#  functions. Make sure to ask the user to enter the number of numbers in the 
#  sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers 
#  where the next number in the sequence is the sum of the previous two numbers 
#  in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

num = int(raw_input("How many Fibonnaci numbers would you like to generate? "))

def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

for x in range(num):
    print(fibo(x))
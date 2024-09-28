"""
Solutions to module 1
Student: Anton Lindbro
Mail: anton.lindbro.8243@student.uu.se
Reviewed by: Divya
Reviewed date: 11/10-24
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have testcode running at the top level (i.e. outside the main function)
you have to remove it before uploading your code into Studium!
Also remove all trace and debugging printouts!

You may not import any packages other than time and math and these may
only be used in the analysis of the fib function.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documatation and and doesn't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""

import time
import math

def multiply(m: int, n: int) -> int:
    if n == 0 or m == 0: #Base case for when either of the numbers are zero we return 0
        return 0 
    else:  
        return m + multiply(m, n-1) #To improve this we could check wich of m or n is smaller and use the samller number for the recursive calls


def harmonic(n: int) -> float:              
    if n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1) #Recursively adds 1/n to get the recursive sum


def get_binary(x: int) -> str:              
    if x == 0:
        return '0'
    elif x == 1:
        return '1'
    elif x < 0: #Checks if x is negative and if it is adds a minus sign infront
        x = abs(x)
        return '-' + get_binary(x)
    else:
        return get_binary(x // 2) + str(x % 2)# Using modulus with 2 to get the zero or the one and then typecast to str


def reverse_string(s: str) -> str:        
    if len(s)<=1:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])#return the last character of the sting plus the rest reversed


def largest(a):                     
    if len(a) <= 1:#If the lengt of the list is 1 return that element
        return a[0]
    elif a[0] > a[1]:# If the first element is larger than the largest in the rest return that
        return largest(a[2:] + [a[0]])
    else:
        return largest(a[1:])#Otherwise return the largest in the rest of the list


def count(x, s: list) -> int:                
    if len(s) == 0:#Empty list returns 0
        return 0
    elif len(s) == 1 and s[0] == x:#List with one element that matches returns 1
        return 1
    elif type(s[0]) == list:#Checks sublists
        return int(s[0] == x) + count(x, s[0]) + count(x, s[1:])
    else:
        return int(s[0] == x) + count(x, s[1:])#Typecast boolean to int to reduce the number of if statements 


def bricklek(f: str, t: str, h: str, n: int) -> list:  
    if n == 0:#No blocks gives no moves
        return []
    else:
        return bricklek(f, h, t, n-1) + [f'{f}->{t}'] + bricklek(h,t,f, n-1) #Move from f to h n-1 blocks then move the last block from f to t 
    #then move n-1 blocks from h to t 


def fib(n: int) -> int:                      
    """ Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_mem(n, memory = None): #Fib_mem from the instuction document
    if memory is None:
        memory = {0: 0, 1: 1}
    if n not in memory:
        memory[n] = fib_mem(n-1, memory) + fib_mem(n-2, memory)
    return memory[n]

def main():
    print('\n\nCode for analysing fib and fib_mem\n')

    starttime = time.perf_counter()#Time the execution of fib(15)
    fib(15)
    endtime = time.perf_counter()
    executiontime1 = endtime - starttime
        
    starttime = time.perf_counter()#Time the execution of fib(20)
    fib(20)
    endtime = time.perf_counter()
    executiontime2 = endtime - starttime
    
    print((executiontime2/executiontime1) - 1.618**5)#If this difference is close to zero we have verified the complexity 1.618^n
    
    c = (executiontime2/(1.618**20) + executiontime1/(1.618**15))/2 #Calculate the consant c for this machine
    
    fib50 = c * 1.618**50 #Estimate execution time for fib(50)
    fib100 = c * 1.618**100 #do the same for fib(100)
    
    print(fib50, fib100/31556926) # print out the execution times in seconds for fib(50) and in years for fib(100)
    
    
    starttime = time.perf_counter()# Time fib_mem(100)
    fib_mem(100)
    endtime = time.perf_counter()
    executiontime3 = endtime - starttime
    
    print(fib_mem(100), executiontime3)
    
    print('\nBye!')


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 8: Time for the tile game with 50 tiles:
    By using the formula given in example 11 we get that 2^50 - 1 = 1.13 * 10^15
    That means if it took 1 second to move a tile it would take 36 million years to move all 50
  
  
  
  Exercise 9: Time for Fibonacci:
    The above code in main gives an answer close to zero so that verifies that the execution time for the algorithm grows
    as 1.618^n
    
    And the call fib(50) would take aproximately 1 hour to run and the call fib(100) would take 2.6 million years
    
    
  Exercise 10: Time for fib_mem:
  fib(100) = 354224848179261915075
  The execution time was 10^-4 seconds
  
  
  Exercise 11: Comparison sorting methods:
  Insertion sort:
  11 days for 10^6 elements 
  32 thousand years for 10^12 elements
  
  Merge sort:
  33 minutes for 10^6
  5 weeks for 10^12
  
  
  Exercise 12: Comparison Theta(n) and Theta(n log n)
  for any n greater than 10^10 A willl be faster than B
  
"""

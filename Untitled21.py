#!/usr/bin/env python
# coding: utf-8

# In[4]:

# Given a number (greater than 2), print two prime numbers whose sum will be equal to
# the given number, else print -1 if no such number exists.
def sum_of_primes(num):
    isPrime = 1
    for i in range (2,int(num/2),1):
        if(num % i == 0):
            isPrime = 0
            break
    return isPrime

num = int(input("Enter a number : "))
flag = 0;
i = 2
for i in range (2,int(num/2),1):
    if(sum_of_primes(i) == 1):
        if(sum_of_primes(num-i) == 1):
            print(i,num-i )
            flag = 1;
if (flag == 0):
    print(n,"cannot be expressed as the sum of two prime numbers")


#Given a list L and integer K, find the maximum for each and every contiguous subarray
# of size K. Write a function that takes the list as input and returns the output as a list.


def printMax(arr, n, k):
    max = 0
   
    for i in range(n - k + 1):
        max = arr[i]
        for j in range(1, k):
            if arr[i + j] > max:
                max = arr[i + j]
        print(str(max) + " ", end = "")
   
if __name__=="__main__":
    arr = [5,6,7,8,7,6,3]
    n = len(arr)
    k = 2
    printMax(arr, n, k) 


# In[ ]:





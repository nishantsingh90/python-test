#!/usr/bin/env python
# coding: utf-8

# In[ ]:
# Write a function to check whether the string is a palindrome. The function should take a
# string as input. If found to be a palindrome, print “is palindrome” else print “not

def isPalindrome(s): 
    return s == s[::-1] 
s = "noon"

x = isPalindrome(s) 
  
if x: 
    print("ispalindrome") 
else: 
    print("No")


# In[5]:
# Write a function that takes a path to a txt file as input and returns a list containing the
# number of words and sentences in the file.

file = open("test.txt", "r")

number_of_lines = 0
number_of_words = 0

for line in file:
  line = line.strip("\n")


  words = line.split()
  number_of_lines += 1
  number_of_words += len(words)
  

file.close()

print("lines:", number_of_lines, "words:", number_of_words)


# In[15]:

# Write a function that will take a sentence as input in the form of a string. Remove all but
# the first occurrence of every duplicate word in the sentence. Return the modified
# sentence.
string1 = "I write code. I love to code."
words = string1.split()
print (" ".join(sorted(set(words), key=words.index)))


# In[18]:
# Write a function that will take a string as input and return a new string without
# consonants.

def removeconsonants(x):
    for char in x:
        if char in 'aeiou':
            print(char,end = "")
removeconsonants('abc')


# In[ ]:





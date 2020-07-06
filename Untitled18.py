#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def isPalindrome(s): 
    return s == s[::-1] 
s = "noon"

x = isPalindrome(s) 
  
if x: 
    print("ispalindrome") 
else: 
    print("No")


# In[5]:


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


string1 = "I write code. I love to code."
words = string1.split()
print (" ".join(sorted(set(words), key=words.index)))


# In[18]:


def removeconsonants(x):
    for char in x:
        if char in 'aeiou':
            print(char,end = "")
removeconsonants('abc')


# In[ ]:





#!/usr/bin/env python
# coding: utf-8
1.What are the two values of the Boolean data type? How do you write them?
# boolean:
# 1-True
# 2-False
2. What are the three different types of Boolean operators?
# In[ ]:


==,!=,>,<,<=,>=


# In[3]:


1!=2


# In[6]:


1>=2

3. Make a list of each Boolean operator  truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ). True and True is True.

True and False is False.

False and True is False.

False and False is False.

True or True is True.

True or False is True.

False or True is True.

False or False is False.

not True is False.

not False is True.4. What are the values of the following expressions?
# In[7]:


print((5>4) and (3==5))
print(not(5>4))
print((5>4) or (3==5))
print(not(5>4) or (3==5))
print((True and True) and (True==False))
print((not(False))or(not(True)))

5. What are the six comparison operators? ==, !=, <, >, <=,>=6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.

== is the equal to operator that compares two values and evaluates to a Boolean, while = is the assignment operator that stores a value in a variable.
# In[9]:


if(2==3):
    print("True")
else:
    print("False")
c=1
print("c =",c)

7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print(&#39;eggs&#39;)
if spam &gt; 5:
print(&#39;bacon&#39;)
else:
print(&#39;ham&#39;)
print(&#39;spam&#39;)
print(&#39;spam&#39;)
# In[10]:


spam = 0
if spam == 10:
    print('eggs') #Block 1
if spam > 5:
    print('bacon') #Block 2
else:
    print('ham') #Block 3
    print('spam')
    print('spam')

8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.
# In[11]:


spam = int(input("Input a no."))
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")

9.If your programme is stuck in an endless loop, what keys you’ll press?

Ans . If program is stuck in endless loop we will press ctrl+c.10. How can you tell the difference between break and continue?
# In[13]:


for i in range(10):
    if(i==7):
        break
    print(i)
    
print('Breaked')
for i in range(10):
    if(i==7):
        continue
    print(i)
    

11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# In[14]:


for i in range(10):
    print(i)
#prints from 0 to the value given


# In[17]:


for i in range(0,10):
    print(i)
#prints from start value to end-1th value


# In[16]:


for i in range(0,10,1):
    print(i)
#prints from start value to end-1th value with the difference with each number according to the 3rd value passed

12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
# In[18]:


#For Loop
print("For Loop")
for i in range(1,11):
    print(i)
#While Loop
print("While Loop")
a =1
while a <= 10:
    print(a)
    a+=1

13. If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?
ans: spam.bacon
# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


TASK 1 (User login check)


# In[3]:


correct_username = "admin"
correct_password = "1234"
#input
username = input("Enter username:")
password = input("Enter password:")
if username == correct_username and password == correct_password:
    print("Login Successfull")
else:
    print("Invalid Credentials")


# In[ ]:


TASK 2(Pass/Fail Analyzer)


# In[4]:


marks = [45, 78, 90, 33, 60]
pass_count = 0
fail_count = 0

for mark in marks:
    if mark >= 50:
        pass_count += 1
    else:
        fail_count += 1
print("Total Students:", len(marks))
print("pass Students:", pass_count)
print("fail Students:", fail_count)


# In[ ]:


TASK 3(Simple Data Cleaner)


# In[5]:


names = [" Alice ", "bob", " CHARLIE "]
cleaned_names = []
#clean each name
for name in names:
    name = name.strip()  #removes extra spaces
    name = name.lower()  #converts to lowercase
    cleaned_names.append(name)
print("Cleaned Names:", cleaned_names)


# In[ ]:


TASK 4(Message Length Analyzer)


# In[8]:


messages = ["Hi", "Welcome to the platform", "OK"]
for message in messages:
    length = len(message)
    print("Message:", message)
    print("Length:", length)
    if length > 10:
        print("Status: Long Message")
    print()


# In[ ]:


TASK 5(Error Message Detector)


# In[9]:


logs = ["INFO", "ERROR", "WARNING", "ERROR"]
error_count = 0
for log in logs:
    if log == "ERROR":
        error_count += 1
    print("Total ERROR entries:", error_count)


# In[ ]:





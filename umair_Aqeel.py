#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Name: UMAiR AQEEL
Roll No: PIAIC80100
Quarter: 2
Instructor: Sir Qasim
Numpy Assignmentno.2


# In[1]:


import numpy as np


# In[2]:


def function1():
    x=np.arange(1,13).reshape((6,2))
    return x


# In[3]:


function1()


# In[4]:


def function2():
    x=np.arange(10,37,dtype=np.float64).reshape((3,3,3))
    return x


# In[5]:


function2()


# In[131]:


def function3():
    a=np.arange(1,(100*10+1)).reshape((100,10))
    x=a[(a%5==0) & (a%7==0)]
    print(x)
        


# In[132]:


function3()


# In[137]:


def function4():
    arr=np.arange(9).reshape(3,3)
    return arr[:,[1,0]]


# In[138]:


function4()


# In[145]:


def fucntion5():
    z=np.zeros([4,5])
    return z


# In[146]:


fucntion5()


# In[147]:


def function6():
    arr=np.zeros(10)
    arr[5]=10
    arr[8]=20
    return arr


# In[148]:


function6()


# In[158]:


def function7():
    x=np.arange(4,dtype=np.int64)
    return np.zeros_like(x)


# In[159]:


function7()


# In[181]:


def function8():
    x=np.arange(10,dtype=np.int32).reshape(2,5)
    x=np.zeros_like(x)
    return x+6 


# In[182]:


function8()


# In[215]:


def function9():
    x=np.arange(2,101) 
    y=x[x%2==0]
    return y


# In[216]:


function9()


# In[227]:


def function10():
    arr=np.array([[3,3,3],[4,4,4],[5,5,5]])
    brr=np.array([1,2,3])
    subt=arr-brr[:,None]
    return subt


# In[228]:


function10()


# In[229]:


def function11():
    arr=np.array([0,1,2,3,4,5,6,7,8,9])
    odd=arr[arr%2==1]
    arr[odd]=-1
    return arr


# In[230]:


function11()


# In[6]:


def function12():
    import numpy as np
    arr = np.array([1,2,3])
    ans = np.concatenate((np.repeat(arr,3),np.tile(arr,3)))
  
    return ans


# In[7]:


function12()


# In[13]:


def function13():
    import numpy as np
    arr = np.array([2, 6, 1, 9, 10, 3, 27])
    ans = arr[(arr>5) & (arr<10)]
    return ans


# In[14]:


function13()


# In[18]:


def function14():
    import numpy as np
    arr = np.arange(10, 34, 1).reshape(8,3)
    ans = np.array_split(arr,4)
    return ans


# In[19]:


function14()


# In[20]:


def function15():
    import numpy as np
    arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])
    ans = arr[np.argsort(arr[:, 1])]
  
    return ans


# In[21]:


function15()


# In[22]:


def function16():
    import numpy as np
    x = np.array([[1], [2], [3]])
    y = np.array([[2], [3], [4]])
    ans = np.dstack((x,y))
  
    return ans


# In[23]:


function16()


# In[24]:


def function17():
    # replace numbers with "YES" if it divided by 3 and 5
    # otherwise it will be replaced with "NO"
    # Hint: np.where
    import numpy as np
    arr = np.arange(1,10*10+1).reshape((10,10))
    return  np.where(((arr%3==0)&(arr%5==0)),"YES","NO")


# In[25]:


function17()


# In[28]:


def function18():
    # count values of "students" are exist in "piaic"
    import numpy as np
    piaic = np.arange(100)
    students = np.array([5,20,50,200,301,7001])
    x = np.count_nonzero(np.intersect1d(piaic,students))
    return x


# In[29]:


function18()


# In[31]:


def function19():
    import numpy as np
    X =   np.arange(1,26).reshape(5,5)# Write your code here
    W =   np.copy(X)   # Write your code here 
    W =   np.transpose(W)
    b =   5   # Write your code here
    output =    (X*W)+b# Write your code here
    return output


# In[32]:


function19()


# In[33]:


def function20():
    import numpy as np
    x = np.arange(1,11)
    def abc(x):
        return x*2+3-2
    return abc(x)


# In[35]:


function20()


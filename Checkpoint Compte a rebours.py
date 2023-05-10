#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Compte à rebours

import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
     
    print('Fire in the hole!')

t = input("Entrez la durée du compte à rebours en secondes: ")
 
countdown(int(t))


# In[ ]:





# In[ ]:





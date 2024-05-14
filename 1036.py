#!/usr/bin/env python
# coding: utf-8

# In[28]:


a , b, c = list(map(float, input().split()))

pr1 = (b**2)-(4*a*c)

if pr1>0 and a!=0:
    r1 = (-b + (pr1**0.5))/(2*a)
    r2 = (-b-(pr1**0.5))/(2*a)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')

else:
    print('mpossivel calcular')


# In[ ]:





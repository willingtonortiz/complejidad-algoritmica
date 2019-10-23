#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# In[7]:


import math
def diligencia(G, s, t):
    n = len(G)
    T = [math.inf]*n
    P = [None]*n
    
    def stuff(s, u):
        if u == s:
            T[s] = 0
        else:
            for v, w in G[u]:
                if P[v] == None:
                    stuff(s, v)
                if T[v] + w < T[u]:
                    T[u] = T[v] + w
                    P[u] = v
                    
    stuff(s, t)
    
    return T, P


# In[8]:


G = [[],
     [(0, 2)],
     [(0, 4)],
     [(0, 3)],
     [(1, 7), (2, 3), (3, 4)],
     [(1, 4), (2, 2), (3, 1)],
     [(1, 6), (2, 4), (3, 5)],
     [(4, 1), (5, 6), (6, 3)],
     [(4, 4), (5, 3), (6, 3)],
     [(7, 3), (8, 4)]]


# In[9]:


diligencia(G, 0, 9)


# In[ ]:





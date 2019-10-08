#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('conda install -y python-graphviz')


# In[4]:


from graphviz import Digraph, Source


# In[5]:


class Dottable:
    def Dot(self):
        dot = Digraph()
        
        for i in range(self.N):
            dot.node(str(i))
            
        for i in range(self.N):
            if i != self.sets[i]:
                dot.edge(str(i), str(self.sets[i]))
                
        dot.graph_attr['rankdir'] = 'BT'
        return dot


# In[6]:


class DisjointSetQF(Dottable):
    def __init__(self, n):
        self.N = n
        self.sets = [i for i in range(n)]
        
    def Find(self, a):
        return self.sets[a]
    
    def Union(self, a, b):
        pa = self.Find(a)
        pb = self.Find(b)
        for i in range(self.N):
            if self.sets[i] == pa:
                self.sets[i] = pb


# In[20]:


ds = DisjointSetQF(10)
ds.Dot()


# In[21]:


ds.Union(3, 4)
ds.Dot()


# In[22]:


ds.Union(4, 9)
ds.Dot()


# In[23]:


ds.Union(8, 0)
ds.Dot()


# In[24]:


ds.Union(2, 3)
ds.Dot()


# In[25]:


ds.Union(5, 6)
ds.Dot()


# In[26]:


ds.Union(5, 9)
ds.Dot()


# In[27]:


ds.Union(7, 3)
ds.Dot()


# In[28]:


ds.Union(4, 8)
ds.Dot()


# In[29]:


ds.Union(6, 1)
ds.Dot()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[3]:


from graphviz import Digraph, Source


# In[4]:


class Dottable:
    def Dot(self):
        dot = Digraph()
        
        for i in range(self.N):
            dot.node(str(i))
            
        for i in range(self.N):
            if self.sets[i] >= 0:
                dot.edge(str(i), str(self.sets[i]))
                
        dot.graph_attr['rankdir'] = 'BT'
        return dot


# In[5]:


class DisjointSetQU(Dottable):
    def __init__(self, n):
        self.N = n
        self.sets = [-1 for _ in range(n)]
        
    def Find(self, a):
        while self.sets[a] >= 0:
            a = self.sets[a]
        return a
    
    def Union(self, a, b):
        pa = self.Find(a)
        pb = self.Find(b)
        if self.sets[pa] < self.sets[pb]:
            self.sets[pb] = pa
        elif self.sets[pb] < self.sets[pa]:
            self.sets[pa] = pb
        else:
            self.sets[pb] -= 1
            self.sets[pa] = pb


# In[6]:


ds = DisjointSetQU(10)
ds.Dot()


# In[7]:


ds.Union(3, 4)
ds.Dot()


# In[8]:


ds.Union(4, 9)
ds.Dot()


# In[9]:


ds.Union(8, 0)
ds.Dot()


# In[10]:


ds.Union(2, 3)
ds.Dot()


# In[11]:


ds.Union(5, 6)
ds.Dot()


# In[12]:


ds.Union(5, 9)
ds.Dot()


# In[13]:


ds.Union(7, 3)
ds.Dot()


# In[14]:


ds.Union(4, 8)
ds.Dot()


# In[15]:


ds.Union(6, 1)
ds.Dot()


# In[ ]:





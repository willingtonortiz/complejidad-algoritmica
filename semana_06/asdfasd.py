#!/usr/bin/env python
# coding: utf-8

# # Kosaraju (strongly connected componentes)

# In[5]:


import heapq as hq


# In[19]:


def kosaraju(G):
    n = len(G)
    Grev = [[] for i in range(n)]
    
    """ 1 """ 
    for u in range(n):
        for v in G[u]:
            Grev[v].append(u)
            
    """ 2 """
    d = [None]*n
    f = []
    cont = [0]
     
    def dfs(u):
        if d[u] == None:
            cont[0] += 1
            d[u] = cont[0]
            for v in Grev[u]:
                if d[v] == None:
                    dfs(v)
                    
            cont[0] += 1
            hq.heappush(f, (-cont[0], u))
            
    for u in range(n):
        dfs(u)
    
    """ 3 """
    visited = [False]*n
    def dfs2(u, res):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs2(v, res)
        res.append(u)
    
    scc = []
    while len(f) > 0:
        _, u = hq.heappop(f)
        if not visited[u]:
            cc = []
            dfs2(u, cc)
            scc.append(cc)
            
    return scc


# In[20]:


G = [[3], [7], [5], [6], [1], [8], [0], [4, 5], [2, 6]]


# In[21]:


kosaraju(G)


# In[ ]:





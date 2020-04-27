"""
Created on Tue Apr 28 06:26:33 2020

@author: EthanWu
"""
%reset -f
import pandas as pd
from collections import deque
import numpy as np

c1 = [7,7,7,3,3,8,2,6,6,4,4,1,1]
c2 = [3,6,4,8,2,0,0,4,1,1,5,5,2]
 
data_array = np.vstack((c1,c2)).T
del c1 ,c2

Adj_List = [[] for i in  range(data_array.max()+1)]#無向圖  
Adj_DList = [[] for i in  range(data_array.max()+1)]#有向圖
Adj_RDList = [[] for i in  range(data_array.max()+1)]#反向圖

#Prepare tbe Graph data
for i,j in data_array:
    Adj_List[i].append(j)
    Adj_List[j].append(i)
    Adj_DList[i].append(j)
    Adj_RDList[j].append(i)

#Initial Area
visit_time = np.zeros(data_array.max()+1) # 紀錄in的時間點
visit_out = np.zeros(data_array.max()+1)
visit_point = [] # 紀錄遍歷順序
parent = np.zeros(data_array.max()+1) #父節點
t=0

#Depth-First Search Main Function
def DFS_func(x,Adj): 
   global t
   visit_point.append(x)
   t+=1;visit_time[x]=t
   for y in Adj[x]:
       if visit_time[y]==0:
           DFS_func(y,Adj)
           parent[y] = x
   t+=1;visit_out[x]=t   
   return

DFS_func(7,Adj_DList)
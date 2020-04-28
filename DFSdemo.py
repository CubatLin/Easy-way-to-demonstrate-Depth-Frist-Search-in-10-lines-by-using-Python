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

#Prepare Graph data
for i,j in data_array:
    Adj_List[i].append(j)
    Adj_List[j].append(i)
    Adj_DList[i].append(j)
    Adj_RDList[j].append(i)

#--Type1--#
#Initial 
visit_time = np.zeros(data_array.max()+1) # 紀錄in的時間點
visit_out = np.zeros(data_array.max()+1) # 紀錄out的時間點
visit_point = [] # 紀錄遍歷順序
parent = np.zeros(data_array.max()+1) #父節點
t=0

#Depth-First Search Main Function Type1
def DFS_func_type1(x,Adj): 
   global t
   visit_point.append(x)
   t+=1;visit_time[x]=t
   for y in Adj[x]:
       if visit_time[y]==0:
           DFS_func_type1(y,Adj)
           parent[y] = x
   t+=1;visit_out[x]=t   
   return

DFS_func_type1(7,Adj_DList)

#--Type2--#
#Initial 
visit_time = np.zeros(data_array.max()+1) # 紀錄in的時間點
visit_out = np.zeros(data_array.max()+1) # 紀錄out的時間點
visit_point = [] # 紀錄遍歷順序
parent = np.zeros(data_array.max()+1) #父節點
t=0

#Depth-First Search Main Function 
def DFS_func_type2(x,Adj):
    global t
    if Adj[x]==[]:
        visit_point.append(x)
        t+=1;visit_time[x]=t;print(t,x)
        t+=1;visit_out[x]=t;print(t,x)
        return 
    visit_point.append(x)
    t+=1;visit_time[x]=t;print(t,x)
    for y in Adj[x]:
        if visit_time[y]==0:
            DFS_func_type2(y,Adj)
            parent[y]=x
    t+=1;visit_out[x]=t;print(t,x)
        
DFS_func_type2(7,Adj_DList)

#----Additional----#
def DFS_func_Additional(x,Adj):
    global t
    if Adj[x]==[]:
        visit_point.append(x)
        t+=1;visit_time[x]=t;print('Time:',t,'Point:',x)
        t+=1;visit_out[x]=t;print('Time:',t,'Point:',x)
        return 
    visit_point.append(x)
    t+=1;visit_time[x]=t;print('Time:',t,'Point:',x)
    for y in Adj[x]:
        if visit_time[y]==0:
            DFS_func_Additional(y,Adj)
            parent[y]=x
        t+=1;visit_out[x]=t;print('Time:',t,'Point:',x) #What happened if I change this line?
        
DFS_func_Additional(7,Adj_DList)
# =============================================================================
# DFS_func_Additional's process
# Time: 1 Point: 7
# Time: 2 Point: 3
# Time: 3 Point: 8
# Time: 4 Point: 0
# Time: 5 Point: 0
# Time: 6 Point: 8
# Time: 7 Point: 3
# Time: 8 Point: 2
# Time: 9 Point: 2
# Time: 10 Point: 3
# Time: 11 Point: 7
# Time: 12 Point: 6
# Time: 13 Point: 4
# Time: 14 Point: 1
# Time: 15 Point: 5
# Time: 16 Point: 5
# Time: 17 Point: 1
# Time: 18 Point: 1
# Time: 19 Point: 4
# Time: 20 Point: 4
# Time: 21 Point: 6
# Time: 22 Point: 6
# Time: 23 Point: 7
# Time: 24 Point: 7
# =============================================================================

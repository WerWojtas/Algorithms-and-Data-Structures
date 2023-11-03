# Weronika Wojtas
"""Zastosowanie algorytmu dijkstry od wierzchołka s do wszystkich, a następnie od wierzchołka t do wszystkich z uwzględnieniem podwójnej wagi krawędzi i dodatkowego kosztu r. Złożoność obliczeniowa O((V+E)logV)"""

from queue import PriorityQueue

def gold(G,V,s,t,r):

  result=10**10
  n=len(G)
  distances1=Dijkstra(G,s,n)
  distances2=Dijkstra2(G,t,n,r)

  for i in range(len(G)):
    sum=distances1[i]+distances2[i]-V[i]
    if result>sum:
      result=sum


  return result


def Dijkstra(G,start,n):
  d=[10**10]*n
  s=[False]*n
  Q=PriorityQueue()
  d[start]=0
  Q.put((d[start],start))
  while not Q.empty():
    dist,v=Q.get()
    for j in range(len(G[v])):
      neigh=G[v][j][0]
      cost=G[v][j][1]
      if s[neigh]==False and d[neigh]>dist+cost:
          d[neigh]=dist+cost
          Q.put((d[neigh],neigh))
      s[v]=True
  return d

def Dijkstra2(G,start,n,r):
  d=[10**10]*n
  s=[False]*n
  Q=PriorityQueue()
  d[start]=0
  Q.put((d[start],start))
  while not Q.empty():
    dist,v=Q.get()
    for j in range(len(G[v])):
      neigh=G[v][j][0]
      cost=G[v][j][1]*2+r
      if s[neigh]==False and d[neigh]>dist+cost:
          d[neigh]=dist+cost
          Q.put((d[neigh],neigh))
      s[v]=True


  return d
      
      



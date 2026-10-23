import numpy as np
import time
import random
n=10
m=10
grid = np.random.randint(0,2,(n,m))
def gen_grid(n,m,p):
  newgrid=np.random.random((n,m))
  newgrid =(newgrid<p).astype(int)
  return newgrid
grid=gen_grid(n,m,0.5)
i,j=0,0
nbrs=grid[max(0,i-1):i+2,max(0,j-1):j+2].sum()- grid[i,j]
def step(gridn):
  ngrid=np.zeros_like(gridn)
  for i in range(gridn.shape[0]):
    for j in range(gridn.shape[1]):
      nnbrs=gridn[max(0,i-1):i+2,max(0,j-1):j+2].sum()-ngrid[i,j]
      if gridn[i,j]==0 and nnbrs<2:
        if random.randint(-50*max(nnbrs,1),1)>0:
          ngrid[i,j]=1
          if(random.randint(0,1)>0):
            ngrid[i,j]=2
      if gridn[i,j]==2:
        if i+1<n and ngrid[i+1,j]==0 and ngrid[i,j]==2:
            ngrid[i+1,j]=2;
        if i+1<n and ngrid[i+1,j]==1:
            ngrid[i,j]=1
        elif i-1>=0 and ngrid[i-1,j]==0 and ngrid[i,j]==2:
          ngrid[i-1,j]=2;
        if i-1>0 and ngrid[i-1,j]==1:
            ngrid[i,j]=1
        if j+1<m and ngrid[i,j+1]==0 and ngrid[i,j]==2:
            ngrid[i,j+1]=2;
        if j+1<n and ngrid[i,j+1]==1:
            ngrid[i,j]=1
        elif j-1>=0 and ngrid[i,j-1]==0 and ngrid[i,j]==2:
          grid[i,j-1]=2;
        if j-1>0 and ngrid[i,j-1]==1:
            ngrid[i,j]=1
      if gridn[i,j]==0 and nnbrs==3:
        ngrid[i,j]=1
      if gridn[i,j]==1 and nnbrs in (2,3):
        ngrid[i,j]=1
  return ngrid
def printgrid(gridik):
  tmpgrid=gridik.astype(str)
  tmpgrid[tmpgrid=='0']='⬛'
  tmpgrid[tmpgrid=='1']='🟩'
  tmpgrid[tmpgrid=='2']='🟦'
  s='\n'.join([''.join(tmpgrid[i]) for i in range(tmpgrid.shape[0])])
  print(s)
  return None
#from IPython.core.display import clear_output
np.random.seed(0)
n,m=map(int, input().split())
p=float(input())
grid=gen_grid(n,m,p)
printgrid(grid)
#clear_output(wait=True)
while True:
  grid=step(grid)
  #clear_output(wait=True)
  printgrid(grid)
  time.sleep(0.2)

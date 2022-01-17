#!/usr/bin/env python3

import shutil
import sys
import numpy as np
from scipy import ndimage


# FILE HANDLING
# ----------------------------------------
if len(sys.argv) != 2:
    print("Invalid input")
    sys.exit(1)

fname = sys.argv[1]

f = open(fname, 'r')
ln = f.readlines()
C=[]
O=[]
H=[]
def commeth(C, O, H):
    e = (C[x][y]+O[x][y]+H[x][y])/(33)
    return e

t=[]
num = len(ln)
num -=2

for i in range(0, num -1 , 1):
    if ln[i][13] == 'C':  # Check if atom is Oxygen(Donor)
        if ln[i+1][13] == 'O' :
            C.append([float(ln[i][30:38])*(15), float(ln[i][38:46])*15, float(ln[i][46:54])*15])
            O.append([float(ln[i+1][30:38])*16, float(ln[i+1][38:46])*16, float(ln[i+1][46:54])*16])
            H.append([float(ln[i+2][30:38]), float(ln[i+2][38:46]), float(ln[i+2][46:54])])

for x in range(len(C)):
    t.append([])
    for y in range(len(C[x])):
        t[x].append(commeth(C, O, H))

b=[]
B=[]
def com(B):
    d = (B[x][y]+B[x+1][y]+B[x+2][y]+B[x+3][y]+B[x+4][y]+B[x+5][y])/(6)
    return d


num = len(ln)
num -=2

for i in range(0, num -1 , 1):
    if ln[i][13] == 'C' and ln[i+1][13] == 'C':  # Check if atom is Oxygen(Donor)
        #if ln[i+1][13] == 'O' :
          #  continue
       # else :
            B.append([float(ln[i][30:38]), float(ln[i][38:46]), float(ln[i][46:54])])

B.append([float(ln[num-1][30:38]), float(ln[num-1][38:46]), float(ln[num-1][46:54])])
for x in range(0,len(B)-5,6):
    b.append([])
    for y in range(0,len(B[x])):
        b[int(x/6)].append(com(B))




f.close()

def dist(A, B):
    """A and B are 2 numpy array representing the location of 2 atoms.
    This function returns the distance between A and B"""
    temp = np.subtract(A,B)
    c = np.sqrt(temp[0]*temp[0] + temp[1]*temp[1] + temp[2]*temp[2])
    return c
m=[]
T=np.array(t)
Z=np.array(b)
dist_cut = 3.5

for i in T:
    for j in Z:
        m.append(dist(i,j))


def scanner(index,threshold):
    count = 0
    for i in Z:
        if dist(T[index],i) < threshold:
            count+=1

    return count


j = 0
for i in range(0,len(T)):
          j+=scanner(i,10.0)

n= j/len(T)
#print(int(n))
print(n)

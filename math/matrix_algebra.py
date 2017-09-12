# Matrix Algebra

import numpy as np

A = np.array([[1, 2, 3], [2, 7, 4]], np.float)
B = np.array([[1, -1], [0, 1]], np.float)
C = np.array([[5, -1], [9, 1], [6, 0]], np.float)
D = np.array([[3, -2, -1], [1, 2, 3]], np.float)
u = np.array([[6, 2, -3, 5]], np.float)
v = np.array([[3, 5, -1, 4]], np.float)
w = np.array([[1], [8], [0], [5]], np.float)

print(A.shape)
print(B.shape)
print(C.shape)
print(D.shape)
print(u.shape)
print(w.shape)

#1.1:  (2, 3)
#1.2:  (2, 2)
#1.3:  (3, 2)
#1.4:  (2, 3)
#1.5:  (1, 4)
#1.6:  (4, 1)

print(u+v)
print(u-v)
alpha=2.0
print(alpha*u)
print(np.dot(u,v.T))
print(np.linalg.norm(u))

#2.1:  [[ 9.  7. -4.  9.]]
#2.2:  [[ 3. -3. -2.  1.]]
#2.3:  [[ 12.   4.  -6.  10.]]
#2.4:  [[ 51.]]
#2.5:  8.60232526704

#print(A + C)
print(A - C.T)
print(C.T + 3.0*D)
print(np.dot(B,A))
#print(np.dot(B,A.T))

#3.1:  ValueError: operands could not be broadcast together with shapes (2,3) (3,2)
#3.2:  [[-4. -7. -3.]
#       [ 3.  6.  4.]]
#3.3:  [[ 14.   3.   3.]
#       [  2.   7.   9.]]
#3.4:  [[-1. -5. -1.]
#       [ 2.  7.  4.]]
#3.5:  ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)

#print(np.dot(B,C))
print(np.dot(C,B))
print(  np.dot((np.dot(np.dot(B,B),B)),B)    )
print(np.dot(A,A.T))
print(np.dot(D.T,D))

#3.6:   ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)
#3.7:   [[ 5. -6.]
#        [ 9. -8.]
#        [ 6. -6.]]
#3.8:   [[ 1. -4.]
#        [ 0.  1.]]
#3.9:   [[ 14.  28.]
#        [ 28.  69.]]
#3.10:  [[ 10.  -4.   0.]
#        [ -4.   8.   8.]
#        [  0.   8.  10.]]




import numpy as np

a = np.array([[1,1], [2,3], [4,4], [8,1]])
b = np.array([[0.1,0.1], [1.2,3.3], [-3,-6]])
#b1 = np.array([[[0.1],[0.1]], [[1.2],[3.3]], [[-3],[-6]]])
b_x = b.T[0].reshape((1,len(b)))
b_y = b.T[1].reshape((1,len(b)))
a_x = a.T[0].reshape((1,len(a)))
a_y = a.T[1].reshape((1,len(a)))
print(b_x, b_y,len(b),len(b_x),len(a))

center = np.array([np.sum(b_x, axis=1), np.sum(b_y, axis=1)]) / len(b)
print(center[0][0])
print(np.argmin((b_x - center[0])))
print(b_x - center[0])

##mat_b_x = np.zeros((len(b),len(a)),dtype=b_x.dtype) + b_x.T
##mat_b_y = np.zeros((len(b),len(a)),dtype=b_x.dtype) + b_y.T
####print(mat_b_x)
####print(a_x)
####print(mat_b_x - a_x)
##
##diff_x = mat_b_x - a_x
##diff_y = mat_b_y - a_y
####print(diff_x)
####print(diff_x**2)
##
##square_diff_x = diff_x**2
##square_diff_y = diff_y**2
##
##sum1 = square_diff_x + square_diff_y
####print(square_diff_x)
####print(square_diff_y)
####print(sum1)
##
##sqrt1 = np.sqrt(sum1) # = distance
##print(sqrt1)
##
##distance = np.sqrt( (mat_b_x - a_x)**2 + (mat_b_y - a_y)**2 )
##print(distance)


# GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOD
##mat_b_x = np.zeros((len(b_x),len(b_x)),dtype=b_x.dtype)
##mat_b_y = np.zeros((len(b_y),len(b_y)),dtype=b_y.dtype)
##for i in range(len(b_x)):
##    mat_b_x[i] = np.roll(b_x,i)
##for i in range(len(b_y)):
##    mat_b_y[i] = np.roll(b_y,i)



##mat_b_x = np.zeros((len(b_x),len(b_x)),dtype=b_x.dtype)
##print(mat_b_x, len(mat_b_x))
##for i in range(len(b_x)):
##    mat_b_x[i] = np.roll(b_x,i)
##print(mat_b_x)


##mat_b = np.zeros((3,3),dtype=b_x.dtype) + b_x
##print(mat_b.T)
##print(np.roll(mat_b.T,2))

##print("vector a : \n", a)
##print("vector b : \n", b)
##print("------------------")
##print("Orginal : \n", b)
##print("shifted : \n", np.roll(b,1, axis=0))
##
##print("------------------")
###mat_b = np.broadcast_to(b.T,(3,3))
###print(mat_b)
##m=3
##mat_b = np.repeat(b1, 2, axis=0) #np.zeros((3,4),dtype=b.dtype) + b
##print("matrix : \n",mat_b)
##print(mat_b[2])
##
### roll mat_b
### diff = mat_b - a
### (mat_b)**2
##

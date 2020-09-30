# Implementation of Gauss-Seidel Method in Python 
# Erin Sam Joe | Undergrad NITK | Mechanical Engg. Major | Electrical & Electronics Engg. Minor 

import numpy as np 
import math 



dimensions = int(input("\nEnter the dimension of the unknowns' vector: "))

print("\nEnter the entries of the coefficient matrix in a single line (separated by spaces):")
entries = list(map(float, input().split()))
A = np.array(entries).reshape(n,n)

print("\nEnter the entries for the constant term in a single line, separated by spaces:")
entries = list(map(float, input().split()))
b = np.array(entries)

# Initialising the unkowns' vector to zero 
x = np.zeros(n)
x_update = np.zeros(n)

# Displaying coefficient matrix and constants' vector 
print("\nCoefficient Matrix:", A, "Constants' Vector:", b)



# Obtaing error tolerance and the iteration count from the user 
tolerance = float(input("Enter the error tolerance for Jacobi Method: "))
max_iter = int(input("Enter the maximum number of iteration for Jacobi Method: "))



# Gauss-Seidel METHOD
for k in range(max_iter):
	for i in range(n):
		x_update[i] = (1/A[i,i]) * ( b[i] - np.dot(A[i, :i-1], x_update[:i-1]) - np.dot(A[i, i+1:], x[i+1,]) )

	# Tolerance Check 
	if ( (max(x_update - x))/max(x_update) <= tolerance ):
		x = x_update
		break

	# Updation Step
	x = x_update


print("\nThe final value of the unknowns' vector obtained given the maximum count on the number of iteration and error tolerance: ")
print(x)



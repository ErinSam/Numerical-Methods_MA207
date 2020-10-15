
def bisection_method():

	tolerance = float(input("Enter the error tolerance for the algorithm: "))
	iteration_limit = float(input("Enter the iteration limit for the algorithm: "))

	bisection_limit_1 = float(input("Enter the first endpoint for the interval: "))
	bisection_limit_2 = float(input("Enter the second endpoint for the interval: "))

	if ( f(bisection_limit_1) * f(bisection_limit_2) > 0):
		print("\nInappropriate endpoints provided for bisection method. Ending program.")
		return

	count = 0			

	approximate_solution = bisection_method_iteration_step(bisection_limit_1, bisection_limit_2, tolerance, count, iteration_limit)
	if ( approximate_solution != None ):
		print("\n\nThe approximate solution for the zero obtained through our bisection algorithm is ")
		print(approximate_solution)



def bisection_method_iteration_step(bisection_limit_1, bisection_limit_2, tolerance, count, iteration_limit):
	bisection_point = ( bisection_limit_1 + bisection_limit_2 ) / 2
	# print(bisection_point)

	count += 1 
	if ( count > iteration_limit ):
		print("\nIteration limit has been exceeded. Solution unable to converge.")
		return None 

	if ( (abs( bisection_limit_2 - bisection_limit_1 ) / 2 <= tolerance) | (f(bisection_point) == 0) ):
		return bisection_point

	if ( f(bisection_limit_1)*f(bisection_point) < 0 ):
		return bisection_method_iteration_step(bisection_limit_1, bisection_point, tolerance, count, iteration_limit)
	else:
		return bisection_method_iteration_step(bisection_point, bisection_limit_2, tolerance, count, iteration_limit)



def f(x):
	# User modifies this part to fit the function that they need to apply bisection method to
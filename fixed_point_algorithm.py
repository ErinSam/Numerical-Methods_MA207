
def fixed_point_method():
	start_step_point = float(input("Enter the initial approximation: "))

	tolerance = float(input("Enter the error tolerance for the algorithm: "))
	iteration_limit = float(input("Enter the iteration limit for the algorithm: "))

	count = 0

	approximate_solution = fixed_point_iteration_step(start_step_point, tolerance, count, iteration_limit)
	if ( approximate_solution != None ):
		print("\n\nThe approximate solution for the zero obtained through our bisection algorithm is ")
		print(approximate_solution)


def fixed_point_iteration_step(approximation, tolerance, count, iteration_limit):
	next_approximation = g(approximation)

	# Ensures that algorithm does not exceed the iteration limit 
	count += 1 
	if ( count > iteration_limit ):
		print("\nIteration limit has been exceeded. Solution unable to converge.")
		return None

	# Checks whether the approximate solutions has been obtained 
	# If not, the recursion continues
	if ( (abs( next_approximation - approximation ) <= tolerance) | (next_approximation == g(next_approximation)) ):
		return next_approximation 
	else: 
		return fixed_point_iteration_step(next_approximation, tolerance, count, iteration_limit)


def g(x):
	# User modifies this part to fit the function that they need to apply fixed point iteration method to 

fixed_point_method()



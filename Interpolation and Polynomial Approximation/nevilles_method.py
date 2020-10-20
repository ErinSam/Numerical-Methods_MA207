"""
    Python script that reads values from an excel file containing the 
    data points and their corresponding values of a function and 
    obtains all the possible Lagrange Polynomials available to it 
    
    This is Neville's Method. 

    Faires J. D., Numerical Analysis
"""

import numpy as np 
import pandas as pd 


def nevilles_method(x):
    
    # Reading the contents of the xls file 
    data = pd.read_excel("data_points_and_corresponding_values.xlsx")
    
    # Creating the necessary (Numpy) arrays to handle the data 
    data_point = np.array(data['data_point'].tolist())
    lagrange_approximation = np.zeros((data.shape[0], data.shape[0]))
    
    # Initialising the first column of the lagrange approximations matrix 
    lagrange_approximation[:,0] = np.array(data['value_at_data_point'].tolist())
    
    # Neville's Method 
    for i in range(1, data.shape[0]):
        for j in range(1, i):
            lagrange_approximation[i,j] = ( (x - data_point[i]) * lagrange_approximation[i-1,j-1] 
                                            - (x - data_point[i-j]) * lagrange_approximation[i,j-1] )
                                            / (data_point[i-j] - data_point[i]) 

    # Writing the values to the xls file
    # ADD


###################################################################################################
###################################################################################################

num = float(input("\nPlease enter the point at which you would like the approximations to be obtained at: "))
nevilles_method(num)

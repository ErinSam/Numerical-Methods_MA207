""" 
    Python script that implements the Runge-Kutta Method for with fourth order local 
    truncation error.  
"""

# Erin Sam Joe | NITK '23 | Mechanical Engg. Major | Electronics & Electrical Engg. Minor


import numpy as np 
import math as m 



def runge_kutta_order_4(a, b, N, initial_condition, f)
    """
        Function that approximates the solution of the IVP
            y' = f(t,y),    a <= t <= b,     y(a) = initial_condition
        at (N+1) equally spaced numbers in the interval [a,b]

        Args: 
            a: float; endpoint start
            b: float; endpoint end
            N: int; number of data points to approximate for 
            initial_condition: float; the initial conditon for IVP 
            f: function; function f=f(t,y) in the IVP

        Return:
            data_pts: ndarray(N+1, 2); 2D array containing the approximations at the datapoints 
    """

    # Obtaining the step size
    step_size = (b-a)/N
 
    # Creating the array 
    data_pts = np.zeros((2, N+1))
    data_pts[0,0], data_pts[0,1] = a, initial_condition

    # Runge-Kutta Method
    for i, data_pt in enumerate(data_pts[1:,]):
        k1 = step_size * f(data_pts[i-1,0], data_pts[i-1,1])
        k2 = step_size * f(data_pts[i-1,0] + step_size/2, data_pts[i-1,1] + k1/2)
        k3 = step_size * f(data_pts[i-1,0] + step_size/2, data_pts[i-1,1] + k2/2) 
        k4 = step_size * f(data_pts[i-1,0] + step_size, data_pts[i-1,1] + k3) 
        
        data_pts[i,0] = a + i * step_size
        data_pts[i,1] = data_pts[i-1,1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return data_pts

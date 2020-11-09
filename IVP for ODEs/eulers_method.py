"""
    Python script that implements Euler's Method
"""

# Erin Sam Joe | NITK '23 | Mechanical Engg. Major | Electrical & Electronics Engg. Minor


import numpy as np 



def eulers_method(a, b, N, alpha, f):
    """ EULER'S METHOD
        
        Function that uses Euler's Method to solve the following IVP:
            y' = f(t, y), 
                a <= t <= b
                y(a) = alpha

        Args: 
            a: float; part of the bounds [a,b]
            b: float; part of the bounds [a,b]
            N: int; number of mesh points
            alpha: float; initial condition
            f: function; f that is present in the IVP must be passed 

        Return: 
            data_pts: ndarray(2,N+1); values at the mesh-points using Euler's Method 
    """

    # Obtaining the step size
    step_size = (b-a)/N

    # Initializing the ndarray for the values at the mesh points
    data_pts = np.zeros((2,N+1))
    data_pts[0,0], data_pts[0,1] = alpha, a

    # Loop to obtain the values at the mesh points
    for i, data_pt in enumerate(data_pts[,1:].T):
        data_pts[0,i] = data_pts[0,i-1] + step_size * f(data_pts[1,-1], data_pts[0,i-1])
        data_pts[1,i] = a + i * step_size

    return data_pts
        

### module to calculate the hypotenuse of a right angle triangle. need numpy for square root. 
import numpy as np

## function 1 to calculate the square of a variable.
# Inputs: a
def square(a, b):
    """Calculate square of 2 values
    
    Args:
        a = opposite side of right angle triangle 
        b = adjacent side of right angle triangle
    
    Returns:
        float, float: the squared inputs
        """
    a2 = a**2
    b2 = b**2
    return(a2, b2)
# Outputs: a**2

## function 2 that calculates  square root of a**2 + b**2 using function 1. 
# Inputs: a and b
def hypot(a,b):
    c2 = a + b
    c = np.sqrt(c2)
    return(c)
# outputs: c

def pythag(a,b):
    a2, b2 = square(a,b)
    hypotenuse = hypot(a2,b2)
    return hypotenuse

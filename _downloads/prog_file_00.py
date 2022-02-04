# Example program for importing
# *not* using __name__

import numpy as np


def func01_max(x, y):
    '''func01_max(x, y)

    This program takes two inputs and compares them to find
    the maximum.  

    The maximum value is output; if they are equal, 0 is returned.'''
    
    if x > y:
        print("first value is greater")
        return x
    elif y > x:
        print("second value is greater")
        return y
    else:
        print("Equality!")
        return 0

# ----------------- end of definitions -------------------------------

out1 = func01_max(5, 55)
print("In first comparison, the winner is:", out1)

out2 = func01_max("a", "A")
print("comparing small/large letters, the winner is:", out2)

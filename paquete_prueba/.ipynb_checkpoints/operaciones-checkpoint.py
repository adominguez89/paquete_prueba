def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplica(a,b):
    return a*b

def divide(a,b):
    if b!=0:
        return a/b
    else:
        import numpy as np
        return np.nan
    
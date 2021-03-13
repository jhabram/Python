# -*- coding: utf-8 -*-

""" ---- Recursive Euklides Algorithm ---- """


def euklides_rec(x,y):
    
    """
    Returns GCD(x,y) - The greatest common divisor
    of two integer numbers using Euklides algorithm.
    
    Input
    -----
    x:int
    y:int
    
    Return
    ------
    GCD(x,y):int
    
    """
   
    r = x % y # rest of division x,y
        
    if r == 0:
        return y # GCD(x,y)
    else:
        return euklides_rec(y, r)

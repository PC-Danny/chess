import numpy as np

def sqdist(vector):
    return sum(x*x for x in vector)

def isPosition(pos):
    """
    Deze functie bekijkt of de positie überhaupt een positie is op het schaakboord.
    """
    if  pos[0] > 8  or pos[0] < 1 \
        or  pos[1] > 8 or pos[1] < 1:
        raise Exception()
    else:
        pass
    

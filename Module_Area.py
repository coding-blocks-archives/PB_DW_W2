"This module provides an interface for area of 2D shapes like circle , square and rectangle"""
import math

pi = math.pi

def circle(r):
    """input: radius
    output: pi*r**2"""
    return pi*r**2

def square(side):
    return side**2

def rectangle(l , b):
    return l*b
if __name__ == '__main__':
    import sys
    shape = sys.argv[1]
    if shape == 'circle':
        print(circle(int(sys.argv[2])))
    elif shape == 'square':
        print(square(int(sys.argv[2])))

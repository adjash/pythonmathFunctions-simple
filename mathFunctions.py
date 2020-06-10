import numpy as np
import pandas as pd 

"""Global Pi Variable"""
pi = 22/7

def is_palindrome(s):
    return s == s[::-1]

def addition(val1, *values):
    total = val1
    for num in values:
        total = total + num
    return total

def findSmallestValue(val1, *values):
    smallest = val1
    for num in values:
        if smallest > num:
            smallest = num
        else:
            smallest = smallest
        return smallest

def degreeToRadian(degree):
   degree = degree * pi/ 180
   return degree

def trapezoidArea(topWidth, baseWidth, height):
    """Trapezoid Area: a = topBase + baseWidth, /2, *height"""
    area = ((topWidth + baseWidth) /2) * height
    return area
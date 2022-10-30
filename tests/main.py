import matplotlib.pyplot as plt
import timeit

def _min(a):
    m=min(a)
    return m

def _max(a):
    m=max(a)
    return m

def _sum(a):
    m=sum(a)
    return m

def _mult(a):
    m=math.prod(a)
    return m


import math


f = open("input.txt", "r")
lines = f.read().split(' ')
nums = list(map(int, lines))
print (*nums, sep=" ")
print (_min(nums))
print (_max(nums))
print (_sum(nums))
print (_mult(nums))


'''
This is a python code to calculate equivalent width of stokes lines.
Created by: Samriddhi
Created on: 06 Apr, 2019
Created at : Bangalore
'''

import numpy as np

# function to calculate equivalent width
def eqwidth(x,y,N):
  sum = 0.0
  for j = 0 in range(1, N):
    sum = sum + (x[j-1]-x[j])*(1.0 - y[j-1]) + (1.0 - y[j])
    sum = 0.5 * abs(sum)
    return sum
  

wla = 6172.34 # lower wavelength
wlb = 6174.34 # higher wavelength
wld = 0.02    # wavelength difference

x = np.arange(wl, wlb, wld)
y = loadtxt('datafile.csv') # load data file
N = len(x)
width = eqwidth(x,y,N)
print(width)

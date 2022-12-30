#7x^{4}+3x^{2}-10x
# domain: [-100, 100]
# print out, range

# 1. input your polynomial degree
# 2. input your coefficents

import matplotlib.pyplot as plt
import numpy as np

xlist = []
ylist = []

def polynomial_func():
  for x in range(-10, 11):
    global xlist
    global ylist
    
    print(x)
    xlist.append(x)

    result = 7*(x**3) + 3*(x**2) - 10*x
    print("Result: ", result)
    ylist.append(result)

polynomial_func()

print("Y-list: ", ylist)


xpoints = np.array(xlist)
ypoints = np.array(ylist)

plt.plot(xpoints, ypoints, ':Dc')
plt.show()
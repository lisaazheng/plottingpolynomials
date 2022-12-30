#7x^{4}+3x^{2}-10x
# domain: [-100, 100]
# print out, range

# 1. input your polynomial degree
# 2. input your coefficents

import matplotlib.pyplot as plt
import numpy as np

coeff1 = input("input highest coefficient")
coeff2 = input("input second coefficient")
coeff3 = input("input lowest coefficient")

xlist = []
ylist = []

def polynomial_func():
  for x in range(-10, 11):
    global xlist
    global ylist
    
    print(x)
    xlist.append(x)

    result = (coeff1)*(x**3) + (coeff2)*(x**2) + (coeff3)*x
    print("Result: ", result)
    ylist.append(result)

polynomial_func()

print("Y-list: ", ylist)


xpoints = np.array(xlist)
ypoints = np.array(ylist)

plt.plot(xpoints, ypoints, ':Dc')
plt.show()

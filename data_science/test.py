# from sympy import *
# x = symbols('x')
# f = 2*x + 1
# plot(f)


# from sympy import *
# from sympy.plotting import plot3d
# x, y = symbols('x y')
# f = x + y
# plot3d(f)

# x = [1, 4, 6, 2]
# n = len(x)
# summation = sum(10*x[i] for i in range(0,n))
# print(summation)


import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

x = full_health_data["Average_Pulse"]
y = full_health_data ["Calorie_Burnage"]

slope, intercept, r, p, std_err = stats.linregress(x, y)
print(slope, intercept, r, p, std_err)

def myfunc(x):
 return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, slope * x + intercept)
plt.ylim(ymin=0, ymax=2000)
plt.xlim(xmin=0, xmax=200)
plt.xlabel("Average_Pulse")
plt.ylabel ("Calorie_Burnage")
plt.show()
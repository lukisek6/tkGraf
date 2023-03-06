import scipy.interpolate as inp
import pylab as lab

#x= [0, 0.3, 0.5, 0.8, 1,  2,  3 ]
#y= [0, 0.1, 0.5, 1,   3, 10, 30]

x= "0 0.3 0.5 0.8 1  2  3".split()
y= "0 0.1 0.5 1   3 10 30".split()

bagr = []
for cislo in x:
    bagr.append(float(cislo))
x = bagr

x = list(map(float, x))
y = list(map(float, y))

lab.plot(x, y, 'o',color='red')

spl = inp.CubicSpline(x, y)
newX = lab.linspace(0, 3, 200)
newY = spl(newX)
lab.plot(newX, newY,':', label='CubicSpline')

spl = inp.UnivariateSpline(x, y, s=2)
newY = spl(newX)
lab.plot(newX, newY,':', label='make_interp_spline')

lab.grid()
lab.legend()
lab.show()
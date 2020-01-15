import matplotlib.pyplot as plt
from consts import *
from math import *


def r(x, y):
    return sqrt(x**2 + y**2)


def f(x, y):
    r1 = r(x, y)
    r2 = r(l - x, y)
    try:
        res = y * (q1 * r2**3 + q2 * r1**3) / (q1 * x * r2**3 - q2 * (l-x) * r1**3)
    except ZeroDivisionError:
        res = 0
    return res


fig = plt.figure()
plt.xlim(-l*0.6, l*1.6)
plt.ylim(-l*sin(pi/3), l*sin(pi/3))

for ang in range(5):
    angle = pi/20 + pi/10*ang
    x0 = y0 = X0 = Y0 = 0
    x = x0 + ro * cos(angle)
    y = y0 + ro * sin(angle)
    start = plt.plot([x0, x], [y0, y], c='b', ls='--')
    start1 = plt.plot([x0, x], [-y0, -y], c='b', ls='--')
    x0 = x
    y0 = y

    X = X0 - ro * cos(angle)
    Y = Y0 - ro * sin(angle)
    start2 = plt.plot([X0, X], [Y0, Y], c='b', ls='--')
    start3 = plt.plot([X0, X], [-Y0, -Y], c='b', ls='--')
    X0 = X
    Y0 = Y

    while r(x0, y0) + r(l - x, y) < 2*l:
        d = f(x0, y0)
        x = x0 + h
        y = y0 + h * d
        y = y0 + h / 2 * (f(x0, y0) + f(x, y))
        point = plt.plot([x0, x], [y0, y], c='g', ls="--")
        point1 = plt.plot([x0, x], [-y0, -y], c='g', ls='--')
        x0 = x
        y0 = y
    while r(X0, Y0) + r(l - X, Y) < 2*l and f(X0, Y0) > 0:
        D = f(X0, Y0)

        X = X0 - h
        Y = Y0 - h * D
        point2 = plt.plot([X0, X], [Y0, Y], c='r', ls='--')
        point3 = plt.plot([X0, X], [-Y0, -Y], c='r', ls='--')
        X0 = X
        Y0 = Y

if q2 > 0:
    for ang in range(5):
        angle = pi / 20 + pi / 10 * ang
        y0 = Y0 = 0
        x0 = X0 = l

        x = x0 + ro * cos(angle)
        y = y0 + ro * sin(angle)
        start = plt.plot([x0, x], [y0, y], c='b', ls='--')
        start1 = plt.plot([x0, x], [-y0, -y], c='b', ls='--')
        x0 = x
        y0 = y

        X = X0 - ro * cos(angle)
        Y = Y0 - ro * sin(angle)
        start2 = plt.plot([X0, X], [Y0, Y], c='b', ls='--')
        start3 = plt.plot([X0, X], [-Y0, -Y], c='b', ls='--')
        X0 = X
        Y0 = Y

        while r(x0, y0) + r(l - x, y) < 2 * l:
            d = f(x0, y0)
            x = x0 + h
            y = y0 + h * d
            y = y0 + h / 2 * (f(x0, y0) + f(x, y))
            point = plt.plot([x0, x], [y0, y], c='g', ls="--")
            point1 = plt.plot([x0, x], [-y0, -y], c='g', ls='--')
            x0 = x
            y0 = y
        while r(X0, Y0) + r(l - X, Y) < 2 * l and f(X0, Y0) > 0:
            D = f(X0, Y0)

            X = X0 - h
            Y = Y0 - h * D
            point2 = plt.plot([X0, X], [Y0, Y], c='r', ls='--')
            point3 = plt.plot([X0, X], [-Y0, -Y], c='r', ls='--')
            X0 = X
            Y0 = Y

z1 = plt.scatter(0, 0, c='b')
z2 = plt.scatter(l, 0, c='b')

plt.show()

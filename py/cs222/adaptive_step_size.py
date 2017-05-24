# QUIZ
#
# Implement adaptive step size in the
# below function.

import math
import numpy
import matplotlib.pyplot

total_time = 12500.  # s == 3.472 hours
# total_time = 60 * 60 * 24 * 2
g = 9.81  # m / s2
earth_mass = 5.97e24  # kg
gravitational_constant = 6.67e-11  # N m2 / kg2


def acceleration(spaceship_position):
    vector_to_earth = - spaceship_position  # earth located at origin
    return gravitational_constant * earth_mass / numpy.linalg.norm(
        vector_to_earth) ** 3 * vector_to_earth


def orbit():
    x = numpy.zeros(2)  # m
    v = numpy.zeros(2)  # m / s
    x[0] = 15e6
    x[1] = 1e6
    v[0] = 2e3
    v[1] = 4e3
    # v[:] = 3e3, 6e3
    matplotlib.pyplot.scatter(x[0], x[1], s=7)

    current_time = 0.  # s
    h = 100.  # s
    h_new = h  # s, will store the adaptive step size of the next step
    tolerance = 5e5  # m

    steps, h_min, h_max = 0, h, h

    while current_time < total_time:
        steps, h_min, h_max = steps + 1, min(h_min, h), max(h_max, h)

        acceleration0 = acceleration(x)
        xE = x + h * v
        vE = v + h * acceleration0
        xH = x + h * 0.5 * (v + vE)
        vH = v + h * 0.5 * (acceleration0 + acceleration(xE))
        x = xH
        v = vH

        error = numpy.linalg.norm(xH - xE) \
                + total_time * numpy.linalg.norm(vH - vE)
        h_new = h * math.sqrt(tolerance / (error + 1e-50))  # safe divided by 0
        h_new = min(1800., max(0.1, h_new))  # min is 0.1, max is 1800
        # print(h_new)

        matplotlib.pyplot.scatter(x[0], x[1], s=1)
        current_time += h
        h = h_new
    print(steps, h_min, h_max)

    matplotlib.pyplot.axis('equal')
    matplotlib.pyplot.scatter(0., 0.)
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    matplotlib.pyplot.show()
    return x, v


x, v = orbit()

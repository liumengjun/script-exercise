# PROBLEM 3
#
# Modify the below functions acceleration and
# ship_trajectory to plot the trajectory of a
# spacecraft with the given initial position
# and velocity. Use the Forward Euler Method
# to accomplish this.

import numpy
import matplotlib.pyplot

h = 1.0  # s
EARTH_MASS = 5.97e24  # kg
GRAVITATIONAL_CONSTANT = 6.67e-11  # N * m^2 / kg^2
MOON_DISTANCE = 384e6  # m

_earth_gravitational = GRAVITATIONAL_CONSTANT * EARTH_MASS


def acceleration(spaceship_position):
    vector_to_earth = - spaceship_position
    norm = numpy.linalg.norm(vector_to_earth)
    # unit = vector_to_earth / norm
    # return unit * GRAVITATIONAL_CONSTANT * EARTH_MASS / (norm ** 2)
    return vector_to_earth * _earth_gravitational / (norm ** 3)


def ship_trajectory():
    # num_steps = 13000  # about 3.6 hours
    num_steps = 60 * 60 * 24 * 10
    x = numpy.zeros([num_steps + 1, 2])  # m
    v = numpy.zeros([num_steps + 1, 2])  # m / s

    x[0] = 15e6, 1e6
    # v[0] = 2e3, 4e3  # |v[0]| = 4.472 km / s
    v[0] = 3.14e3, 6.41e3  # or 3.192e3, 6.384e3

    for step in range(num_steps):
        x[step + 1] = x[step] + h * v[step]
        v[step + 1] = v[step] + h * acceleration(x[step])

    return x, v


def moon_orbit():
    num_steps = 50
    x = numpy.zeros([num_steps + 1, 2])

    two_pi = 2. * numpy.pi
    for i in range(num_steps + 1):
        rad = two_pi * i / num_steps
        x[i, 0] = MOON_DISTANCE * numpy.cos(rad)
        x[i, 1] = MOON_DISTANCE * numpy.sin(rad)

    return x


mo = moon_orbit()

x, v = ship_trajectory()


def plot_me():
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])  # ship trajectory
    matplotlib.pyplot.plot(x[:500, 0], x[:500, 1])  # first few minutes of ship
    matplotlib.pyplot.plot(mo[:, 0], mo[:, 1])  # moon orbit
    matplotlib.pyplot.scatter(0, 0)
    matplotlib.pyplot.axis('equal')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    matplotlib.pyplot.show()


plot_me()

# QUIZ
#
# Fill in the total_energy function
# below to compute the total energy
# at each time step and store it in
# the array energy.

import numpy
import matplotlib.pyplot

h = 5.0  # s
earth_mass = 5.97e24  # kg
spacecraft_mass = 30000.  # kg
gravitational_constant = 6.67e-11  # N m2 / kg2


def acceleration(spaceship_position):
    vector_to_earth = - spaceship_position  # earth located at origin
    return gravitational_constant * earth_mass / numpy.linalg.norm(
        vector_to_earth) ** 3 * vector_to_earth


def total_energy():
    num_steps = 6000
    x = numpy.zeros([num_steps + 1, 2])  # m
    v = numpy.zeros([num_steps + 1, 2])  # m / s
    energy = numpy.zeros(num_steps + 1)  # J = kg m2 / s2
    distance = numpy.zeros(num_steps + 1)

    x[0, 0] = 15e6
    x[0, 1] = 1e6
    v[0, 0] = 2e3
    v[0, 1] = 4e3
    distance[0] = numpy.linalg.norm(x[0])
    energy[0] = 0.5 * spacecraft_mass * numpy.linalg.norm(v[0]) ** 2 \
                - gravitational_constant * earth_mass * spacecraft_mass \
                  / numpy.linalg.norm(x[0])

    for step in range(num_steps):
        ###Forward Euler Method
        # x[step + 1] = x[step] + h * v[step]
        # v[step + 1] = v[step] + h * acceleration(x[step])
        ###End Forward Euler Method

        ###Symplectic Euler Method
        # x[step + 1] = x[step] + h * v[step]
        # v[step + 1] = v[step] + h * acceleration(x[step + 1])
        ###End Symplectic Euler Method

        ###Heun's Method
        # init_acceleration = acceleration(x[step])
        # xE = x[step] + h * (v[step])
        # vE = v[step] + h * init_acceleration
        # x[step + 1] = x[step] + h * 0.5 * (v[step] + vE)
        # v[step + 1] = v[step] + h * 0.5 * (init_acceleration + acceleration(xE))
        ###End Heun's Method

        ###Heun's Method variant
        init_acceleration = acceleration(x[step])
        vE = v[step] + h * init_acceleration
        x[step + 1] = x[step] + h * 0.5 * (v[step] + vE)
        v[step + 1] = v[step] + h * 0.5 * (
            init_acceleration + acceleration(x[step + 1]))
        ###End Heun's Method variant

        distance[step + 1] = numpy.linalg.norm(x[step + 1])

        e_kinetic = 0.5 * spacecraft_mass * numpy.linalg.norm(v[step + 1]) ** 2
        e_potential = gravitational_constant * earth_mass * spacecraft_mass \
                      / numpy.linalg.norm(x[step + 1])
        energy[step + 1] = e_kinetic - e_potential

    return x, energy, distance


x, energy, distance = total_energy()


def plot_me():
    axes_positions = matplotlib.pyplot.subplot(311)
    matplotlib.pyplot.scatter(*x[0], s=4)
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    matplotlib.pyplot.scatter(0, 0)
    matplotlib.pyplot.axis('equal')
    axes_positions.set_xlabel('Longitudinal position in m')
    axes_positions.set_ylabel('Lateral position in m')
    axes_distance = matplotlib.pyplot.subplot(312)
    matplotlib.pyplot.plot(distance)
    axes_distance.set_xlabel('Step number')
    axes_distance.set_ylabel('Distance to Earth in m')
    axes_energy = matplotlib.pyplot.subplot(313)
    matplotlib.pyplot.plot(energy)
    axes_energy.set_xlabel('Step number')
    axes_energy.set_ylabel('Energy in J')  # 1 Joule = 1 N m = 1 kg m2 / s2
    matplotlib.pyplot.show()


plot_me()

# PROBLEM 2
#
# Figure out what value of the boost velocity will allow the spaceship to
# return safely to earth. In order to do this, you will
# have to fill in the moon_position, acceleration,
# and apply_boost functions. Further details are below.
# NOTE: 地球在坐标系原点
#


import math
import numpy
import matplotlib.pyplot
import matplotlib.lines
import matplotlib.patches

earth_mass = 5.97e24  # kg
earth_radius = 6.378e6  # m (at equator)
gravitational_constant = 6.67e-11  # m3 / kg s2
moon_mass = 7.35e22  # kg
moon_radius = 1.74e6  # m
moon_distance = 400.5e6  # m (actually, not at all a constant)
moon_period = 27.3 * 24.0 * 3600.  # s
moon_initial_angle = math.pi / 180. * -61.  # radian

total_duration = 12. * 24. * 3600.  # s
marker_time = 0.5 * 3600.  # s
tolerance = 100000.  # m


def moon_position(time):
    moon_angle = moon_initial_angle + 2.0 * math.pi * time / moon_period
    position = numpy.zeros(2)
    position[0] = moon_distance * math.cos(moon_angle)
    position[1] = moon_distance * math.sin(moon_angle)
    return position


def acceleration(time, position):
    moon_pos = moon_position(time)
    vector_from_moon = position - moon_pos
    # vector_from_earth = position
    return -gravitational_constant * (earth_mass / numpy.linalg.norm(
        position) ** 3 * position + moon_mass / numpy.linalg.norm(
        vector_from_moon) ** 3 * vector_from_moon)


axes = matplotlib.pyplot.gca()
axes.set_xlabel('Longitudinal position in m')
axes.set_ylabel('Lateral position in m')


# Task Final: What is the appropriate boost to apply?
# Try -10 m/s, 0 m/s, 10 m/s, 50 m/s and 100 m/s and leave the correct amount in as you submit the solution.

def apply_boost():
    # Do not worry about the arrays position_list, velocity_list, and times_list.
    # They are simply used for plotting and evaluating your code, so none of the
    # code that you add should involve them.

    boost = 10.  # m/s Change this to the correct value from the list above after everything else is done.
    position_list = [numpy.array([-6.701e6, 0.])]  # m
    velocity_list = [numpy.array([0., -10.818e3])]  # m / s
    times_list = [0]
    position = position_list[0]
    velocity = velocity_list[0]
    current_time = 0.
    h = 0.1  # s, set as initial step size right now but will store current step size
    h_new = h  # s, will store the adaptive step size of the next step
    mcc2_burn_done = False
    dps1_burn_done = False
    dec_done = False

    while current_time < total_duration:
        # Task 3: Include a retrograde rocket burn at 101104 seconds that reduces the velocity by 7.04 m/s
        # and include a rocket burn that increases the velocity at 212100 seconds by the amount given in the variable called boost.
        # Both velocity changes should happen in the direction of the rocket's motion at the time they occur.

        if not mcc2_burn_done and current_time >= 101104.:
            velocity -= 7.04 * velocity / numpy.linalg.norm(velocity)
            matplotlib.pyplot.scatter(*position, s=16, c='c')
            mcc2_burn_done = True

        if not dps1_burn_done and current_time >= 212100.:
            velocity += boost * velocity / numpy.linalg.norm(velocity)
            matplotlib.pyplot.scatter(*position, s=16, c='m')
            dps1_burn_done = True

        if not dec_done and current_time >= 696362.:
            # 减速回地球
            velocity -= 800 * velocity / numpy.linalg.norm(velocity)
            matplotlib.pyplot.scatter(*position, s=16, c='k')
            dec_done = True

        # Task 4: Implement Heun's method with adaptive step size. Note that the time is advanced at the end of this while loop.
        acceleration0 = acceleration(current_time, position)
        positionE = position + h * velocity
        velocityE = velocity + h * acceleration0
        positionH = position + h * 0.5 * (velocity + velocityE)
        velocityH = velocity + h * 0.5 * (
            acceleration0 + acceleration(current_time + h, positionE))
        position = positionH
        velocity = velocityH

        error = numpy.linalg.norm(positionH - positionE) \
                + total_duration * numpy.linalg.norm(velocityH - velocityE)
        h_new = h * math.sqrt(tolerance / (error + 1e-50))  # safe divided by 0
        # restrict step size to reasonable range
        h_new = min(0.5 * marker_time, max(0.1, h_new))

        current_time += h
        h = h_new
        position_list.append(position.copy())
        velocity_list.append(velocity.copy())
        times_list.append(current_time)

    return position_list, velocity_list, times_list, boost


position, velocity, current_time, boost = apply_boost()


def plot_path(position_list, times_list):
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    previous_marker_number = -1;
    for position, current_time in zip(position_list, times_list):
        if current_time >= marker_time * previous_marker_number:
            previous_marker_number += 1
            # ship trajectory
            matplotlib.pyplot.scatter(position[0], position[1], s=2.,
                                      facecolor='r', edgecolor='none')
            moon_pos = moon_position(current_time)
            if numpy.linalg.norm(position - moon_pos) < 30. * moon_radius:
                # close to moon
                axes.add_line(
                    matplotlib.lines.Line2D([position[0], moon_pos[0]],
                                            [position[1], moon_pos[1]],
                                            alpha=0.1, c='g'))
    # the earth
    axes.add_patch(matplotlib.patches.CirclePolygon((0., 0.), earth_radius,
                                                    facecolor='none',
                                                    edgecolor='b'))
    # moon orbit
    for i in range(int(total_duration / marker_time)):
        moon_pos = moon_position(i * marker_time)
        axes.add_patch(matplotlib.patches.CirclePolygon(moon_pos, moon_radius,
                                                        facecolor='none',
                                                        edgecolor='y',
                                                        alpha=0.7))

    matplotlib.pyplot.axis('equal')
    matplotlib.pyplot.show()


plot_path(position, current_time)

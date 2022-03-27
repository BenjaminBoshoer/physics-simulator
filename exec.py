import time


class Object:
    def __init__(self, weight=0):
        self.mass = weight
        self.acc = self.acc_x = self.acc_y = 0
        self.vel = self.vel_x = self.vel_y = 0
        self.location = self.startingLocation = [0, 0]
        self.x_axis_forces = list()
        self.y_axis_forces = list()
        self.y_axis_forces.append("-mg")
        self.movement_start_time = 0
        self.is_in_motion = 0

    def add_force(self, variables, axis):
        if axis == 'x' or axis == 'X':
            self.x_axis_forces.append(variables)

        if axis == 'y' or axis == 'Y':
            self.y_axis_forces.append(variables)

    def get_forces(self, axis):
        if axis == 'x' or axis == 'X':
            return self.x_axis_forces
        else:
            return self.y_axis_forces

    def start_moving(self):
        self.movement_start_time = time.time()
        self.is_in_motion = 1

    def stop_moving(self):
        self.is_in_motion = 0

    def get_acc(self):
        if self.is_in_motion == 1:
            pass

        else:
            return 0

    # This function returns the equation for a given axis. Example "F - mg = ma"
    def get_equation(self, axis):
        if axis == 'x':
            left = "+".join(self.x_axis_forces)

        elif axis == 'y':
            left = "+".join(self.y_axis_forces)

        index = left.find("+-")
        if index != -1:
            left = left[0:index] + left[index + 1:]

        if self.is_in_motion == 1:
            return left + f" = {self.mass}a"

        else:
            return left + f" = 0"


class FloorObj(object):
    def __init__(self, width, height, color=(0, 0, 0), pos_y=0):
        self.width = width
        self.height = height
        self.color = color
        self.pos_x = 0
        self.pos_y = pos_y

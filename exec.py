
class object:
    def __init__(self, weight=0):
        self.mass = weight
        self.acc = self.acc_x = self.acc_y = 0
        self.vel = self.vel_x = self.vel_y = 0
        self.location = self.startingLocation = [0,0]
        self.x_axis_forces = list()
        self.y_axis_forces = list()
        self.y_axis_forces.append("-mg")


    def add_force(self, variables, axis):
        if(axis == 'x' or axis == 'X'):
            x_axis_forces.append(variables)

        if(axis == 'y' or axis == 'Y'):
            y_axis_forces.append(variables)


    def get_forces(self, axis):
        if(axis == 'x' or axis == 'X'):
            return x_axis_forces
        else:
            return y_axis_forces



class floor_obj(object):
    def __init__(self, width, height, color=(0,0,0), pos_y = 0):
        self.width = width
        self.height = height
        self.color = color
        self.pos_x = 0
        self.pos_y = pos_y

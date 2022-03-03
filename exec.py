
import time

class object:
    def __init__(self, weight=0):
        self.mass = weight
        self.acc = self.acc_x = self.acc_y = 0
        self.vel = self.vel_x = self.vel_y = 0
        self.location = self.startingLocation = [0,0]
        self.x_axis_forces = list()
        self.y_axis_forces = list()
        self.y_axis_forces.append("-mg")
        self.movement_start_time = 0
        self.is_in_motion = 0


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


    def start_moving(self):
        self.movement_start_time = time.time()
        self.is_in_motion = 1


    def stop_moving(self):
        self.is_in_motion = 0


    def get_acc():
        if(self.is_in_motion == 1):
            pass




        else:
            return 0

    # This function retruns the equation for a given axis. Example "F - mg = ma"
    def get_equation(self, axis):

        if(axis == 'x'):
            left = "+".join(self.x_axis_forces)

        elif(axis == 'y'):
            left = "+".join(self.y_axis_forces)

        indx = left.find("+-")
        if(indx != -1):
            left = left[0:indx] + left[indx+1:]

        if(self.is_in_motion == 1):
            return left + f" = {self.mass}a"

        else:
            return left + f" = 0"



class floor_obj(object):
    def __init__(self, width, height, color=(0,0,0), pos_y = 0):
        self.width = width
        self.height = height
        self.color = color
        self.pos_x = 0
        self.pos_y = pos_y

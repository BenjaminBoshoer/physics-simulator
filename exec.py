
class object:
    def __init__(self, weight=0):
        self.mass = weight
        self.acc = self.acc_x = self.acc_y = 0
        self.vel = self.vel_x = self.vel_y = 0
        self.location = self.startingLocation = [0,0]


class floor_obj(object):
    def __init__(self, width, height, color=(0,0,0), pos_y = 0):
        self.width = width
        self.height = height
        self.color = color
        self.pos_x = 0
        self.pos_y = pos_y

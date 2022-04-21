from sympy import symbols,  Eq
from sympy.solvers import solve
import numpy as np

class Object():
    def __init__(self, sign):
        self.mass = symbols(sign)
        self.acc_x = self.acc_y = None
        self.location = None
        self.forces_x = np.array([], dtype = 'S4')
        self.forces_y = np.array([], dtype = 'S4')
        self.forces_y = np.append(self.forces_y, symbols('g'))
        self.equation_x = Eq(0,0)
        self.equation_y = Eq(0,0)
        self.is_in_motion = None


    def add_force(self, force, axis):
        if axis is 'x' or 'X':
            self.forces_x = np.append(self.forces_x, symbols(force))

        elif axis is 'y' or 'Y':
            self.forces_y = np.append(self.forces_y, symbols(force))
            self.equation_y = Eq(self.equation_y + self.forces_y, 0)



    def start_moving(self):
        self.is_in_motion = 1


    def get_equation(self, axis):
        for i in self.forces_y:
            self.equation_y = Eq(self.equation_y + self.forces_y, 0)


def get_equation2(str1):
    if '=' not in str1:
        return None

    right = str1.split("=")
    left = right[0]
    right = right[1]

def main():
    object1 = Object('m1')
    eq1 = Eq(object1.mass * object1.forces_y[0] + object1.mass, symbols('a'))
    print(eq1)
    print(solve(eq1, object1.mass))
    print()

    print("Enter an equation")
    str1 = input()

    print(get_equation2(str1))

if __name__ == "__main__":
    main()

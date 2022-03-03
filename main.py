from exec import *


G_constant = 9.8
WIN_HEIGHT, WIN_WIDTH = 500, 700


def main():

    obj_arr = list()
    obj1 = object("m")
    floor = floor_obj(WIN_WIDTH, WIN_HEIGHT * 0.1, (0, 0, 0), WIN_HEIGHT - WIN_HEIGHT*0.1)

    obj_arr.append(obj1)
    obj1.start_moving()

    print(f"the mass is {obj1.mass}, and the forces on this object are: ")
    print(f"And it's equation is {obj1.get_equation('y')}")


    # currently, the values looks funny.
    # but it will sort itself once the pygame window ajd the 60 FPS will be implied
    start_time = time.time()
    """while True:
        current_time = time.time()
        print("time: %f" % current_time)"""


def update_location(current_time, obj_arr):

    for obj in obj_arr:
        acc = obj.get_acc()


if __name__ == "__main__":
    main()

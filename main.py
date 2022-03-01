from exec import *
import time


WIN_HEIGHT, WIN_WIDTH = 500, 700


def main():

    obj1 = object(12)
    floor = floor_obj(WIN_WIDTH, WIN_HEIGHT * 0.1, (0, 0, 0), WIN_HEIGHT - WIN_HEIGHT*0.1)

    print(f"the mass is {obj1.mass}")
    # currently, the values looks funny.
    # but it will sort itself once the pygame window ajd the 60 FPS will be implied
    start_time = time.time()
    while True:
        current_time = time.time()
        print("time: %f" % current_time)


if __name__ == "__main__":
    main()

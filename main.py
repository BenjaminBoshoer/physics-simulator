from exec import *


WIN_HEIGHT, WIN_WIDTH = 500, 700


def main():

    obj1 = object(12)
    floor = floor_obj(WIN_WIDTH, WIN_HEIGHT * 0.1, (0, 0, 0), WIN_HEIGHT - WIN_HEIGHT*0.1)

    print(f"the mass is {obj1.mass}")
    print("check")



if __name__ == "__main__":
    main()

from turtle import *
import random
import os

SPEED = int(os.getenv('SPEED', -1))
WIDTH = int(os.getenv('WIDTH', 3))
COLORS = os.getenv('COLORS', 'sky blue,navy,steel blue,cyan').split(',')

def main():
    colors = COLORS.copy()
    for i in range(0, 204, 2):
        color(colors.pop(0) if colors else COLORS[0])
        circle(10+i, 100, 2)

if __name__ == '__main__':
    speed(SPEED)
    width(WIDTH)
    ht()
    main()
    mainloop()


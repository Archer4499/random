import math
import sys


def start_draw():
    sys.stdout.write("\x1b[?25l")
    sys.stdout.write("\x1b[2J")
    sys.stdout.flush()


def end_draw(y, radius):
    sys.stdout.write("\x1b[{}H".format(y+radius+1))
    sys.stdout.write("\x1b[?25h")
    sys.stdout.flush()


def draw_point(x, y, char="*"):
    sys.stdout.write("\x1b[{};{}H".format(y, x))
    sys.stdout.flush()
    sys.stdout.write(char)
    sys.stdout.flush()


def draw_circle1(x, y, radius):
    increment = 1/(radius*10)
    rad = 0
    while rad < math.pi/2:
        draw_point(2*x+int(2*radius*math.cos(rad)), y+int(radius*math.sin(rad)))
        draw_point(2*x+int(2*radius*math.cos(rad)), y-int(radius*math.sin(rad)))
        draw_point(2*x-int(2*radius*math.cos(rad)), y+int(radius*math.sin(rad)))
        draw_point(2*x-int(2*radius*math.cos(rad)), y-int(radius*math.sin(rad)))
        rad += increment


def draw_circle2(x, y, radius):
    increment = 1/(radius*2)
    i = 0

    while i < radius:
        j = int(math.sqrt(radius ** 2 - i ** 2))
        draw_point(int(2*(x + i)), y + j)
        draw_point(int(2*(x + i)), y - j)
        draw_point(int(2*(x - i)), y + j)
        draw_point(int(2*(x - i)), y - j)
        i += increment


def draw_circle3(centre_x, centre_y, radius):
    # increment = 1/(radius*2)
    increment = 1/2
    y = 0
    x = radius

    chars = ["╮", "╯", "╰", "╭"]
    chars = ["╲", "╱", "╲", "╱"]
    chars = ["▖", "▘", "▝", "▗"]

    while y < x:
        draw_point(2 * centre_x + int(2*x), centre_y - int(y), chars[0])
        draw_point(2 * centre_x + int(2*x), centre_y + int(y), chars[1])
        draw_point(2 * centre_x - int(2*x), centre_y + int(y), chars[2])
        draw_point(2 * centre_x - int(2*x), centre_y - int(y), chars[3])

        draw_point(2 * centre_x + int(2*y), centre_y - int(x), chars[0])
        draw_point(2 * centre_x + int(2*y), centre_y + int(x), chars[1])
        draw_point(2 * centre_x - int(2*y), centre_y + int(x), chars[2])
        draw_point(2 * centre_x - int(2*y), centre_y - int(x), chars[3])
        y += increment
        x = math.sqrt(radius ** 2 - y ** 2)


def draw_circle4(centre_x, centre_y, radius):
    y = 0
    x = radius

    chars = ["╲", "╱", "╲", "╱"]
    chars = ["▖", "▘", "▝", "▗"]
    chars = ["╮", "╯", "╰", "╭"]

    while y < x:
        draw_point(centre_x + x, centre_y - y, chars[0])
        draw_point(centre_x + x, centre_y + y, chars[1])
        draw_point(centre_x - x, centre_y + y, chars[2])
        draw_point(centre_x - x, centre_y - y, chars[3])

        draw_point(centre_x + y, centre_y - x, chars[0])
        draw_point(centre_x + y, centre_y + x, chars[1])
        draw_point(centre_x - y, centre_y + x, chars[2])
        draw_point(centre_x - y, centre_y - x, chars[3])
        y += 1
        x = int(math.sqrt(radius ** 2 - y ** 2))


if __name__ == '__main__':
    x = 20
    y = 16
    radius = 15
    start_draw()
    draw_circle2(x, y, radius)
    end_draw(y, radius)
import turtle
import argparse


def draw_koch_segment(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        draw_koch_segment(t, length, level - 1)
        t.left(60)
        draw_koch_segment(t, length, level - 1)
        t.right(120)
        draw_koch_segment(t, length, level - 1)
        t.left(60)
        draw_koch_segment(t, length, level - 1)


def draw_koch_snowflake(t, length, level):
    for _ in range(3):
        draw_koch_segment(t, length, level)
        t.right(120)


def main():
    parser = argparse.ArgumentParser(description="Draw a Koch snowflake with specified recursion level.")
    parser.add_argument("level", type=int, help="Recursion level for the Koch snowflake")
    args = parser.parse_args()

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    t = turtle.Turtle()
    t.speed(0)

    length = 300  # Length of one side of the snowflake
    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()

    draw_koch_snowflake(t, length, args.level)

    turtle.done()


if __name__ == "__main__":
    main()
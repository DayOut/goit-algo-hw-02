import turtle
import math

def draw_tree(t, branch_length, level, angle):
    if level == 0:
        return

    t.forward(branch_length)
    t.left(angle)
    draw_tree(t, branch_length * math.cos(math.radians(angle)), level - 1, angle)
    t.right(2 * angle)
    draw_tree(t, branch_length * math.cos(math.radians(angle)), level - 1, angle)
    t.left(angle)
    t.backward(branch_length)


def main():
    # Введення рівня рекурсії
    level = int(input("Введіть рівень рекурсії: "))

    # Налаштування Turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)

    # Малювання дерева Піфагора
    draw_tree(t, 100, level, 45)
    screen.mainloop()


if __name__ == "__main__":
    main()
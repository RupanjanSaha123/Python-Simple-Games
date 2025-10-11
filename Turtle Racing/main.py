import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown', 'cyan', 'magenta']

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title('Turtle Racing')

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Invalid input. Please enter a number between 2 and 10.')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Number out of range. Please enter a number between 2 and 10.')

def race(colors):
    turtles = create_turtle(colors)
    while True:
        for racer in turtles:
            step = random.randrange(1, 20)
            racer.forward(step)

            x,y = racer.position()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtle(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')


racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f'The winner is the {winner} turtle!')

time.sleep(5)
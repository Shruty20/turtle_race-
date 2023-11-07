from turtle import Turtle, Screen
import random
import time

def start_race():
    global is_race_on
    is_race_on = True

def restart_game():
    for turtle in all_turtles:
        turtle.goto(-220, y_positions[all_turtles.index(turtle)])
        turtle.clear()

    finish_line.clear()
    start_race()

is_race_on = False
screen = Screen()
screen.title('TURTLE RACE GAME')

#setup the screen and ask user to paly game
screen.setup(width=500, height=400)
user_reply = screen.textinput(title="TURTLE RACE GAME",prompt="Type yes to start the game? ")
if user_reply.lower() == "yes":
    start_race()

else:
    exit()
colors = ["red", "green", "blue", "purple", "orange", "yellow"]
y_positions = [-20, 10, 40, 70, 100, 130]
all_turtles = []


#create 6 turtles

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-220, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Create the finish line
finish_line = Turtle()
finish_line.penup()
finish_line.goto(230, -200)  # Adjust the coordinates as needed
finish_line.pendown()
finish_line.goto(230, 200)  # This draws a vertical line on the right side
finish_line.hideturtle()

# Countdown before the race
for count in range(3, 0, -1):
    screen.title(f'TURTLE RACE GAME - Starting in {count}')
    time.sleep(1)
    screen.title('TURTLE RACE GAME')

start_time = time.time()
while True:
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 220:
                is_race_on = False
                winning_color = turtle.pencolor()
                winning_time = (time.time() - start_time)
                print(f"The {winning_color} turtle is the winner! Time: {winning_time:.2f} seconds")
            # make each turtle move with different speed

            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

    user_restart = screen.textinput(title="TURTLE RACE GAME",prompt="Type 'yes' to play again or 'exit' to quit: ")
    if user_restart.lower() == "yes":
        restart_game()
    else:
        exit()
screen.exitonclick()


#


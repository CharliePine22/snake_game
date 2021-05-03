import turtle
from turtle import *
from snake import Snake, Parts, Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)


# Call the snake class from the snake.py file
snake = Snake()

# Call the Parts class from the snake.py file
dot = Parts(screen)
dot.dot.goto(dot.generate_dot_cor())
dot.dot.speed('fastest')


# Set initial coordinates
coors = dot.generate_dot_cor()

# Set loop flag
game_on = True

# Allows user to rotate snake head depending on the button pressed
screen.onkey(snake.up, 'Up')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.listen()

# Creates the text to keep score by calling the Scoreboard class from snake.py
score = Scoreboard()


while game_on:
    # Update the screen every loop to move snake forward
    screen.update()
    time.sleep(0.05)

    # Method from snake class that continuously moves the snake
    snake.move()

    if snake.snake_head.distance(dot.dot.pos()) < 15:  # If the snake is within 15 paces of the target
        snake.add_part()  # Increase the length of the snake
        new_coors = dot.generate_dot_cor()  # Generate new coor
        score.add_point() # Add a point to the score
        score.update_score() # Update the scoreboard
        dot.dot.goto(new_coors) # Send dot to new coor

    elif snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() <= -280:
        # If the snake head goes past the boundaries, game over.
        score.save_score()
        score.game_over()
        game_on = False

    for part in snake.snake_body:
        if part == snake.snake_head:
            pass

        elif snake.snake_head.distance(part) < 5:
            score.save_score()
            score.game_over()
            game_on = False

screen.exitonclick()

from turtle import *
from random import *


# noinspection PyShadowingNames
class Snake:
    """Class that creates the initial snake object"""

    def __init__(self):

        # Make starting point of snake game
        self.start_positions = [(0, 0), (-20, 0), (-40, 0)]

        # Used to store created parts, the snakes body
        self.snake_body = []

        for position in self.start_positions:
            # Create 3 white squares
            t = Turtle('square')
            t.penup()
            t.speed('fastest')
            t.color('white')
            # Send them to the starting spot
            t.goto(position)
            # Add to snake body
            self.snake_body.append(t)
            # Declare first part as head for ease of use
        self.snake_head = self.snake_body[0]

    def move(self):
        """Function used to move all the snake body parts forward"""
        for part in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[part].showturtle() # Show any parts that are hidden
            # Loop through parts backwards to get them to move at same time
            new_x = self.snake_body[part - 1].xcor()
            new_y = self.snake_body[part - 1].ycor()
            self.snake_body[part].goto(new_x, new_y)
        self.snake_head.fd(10)

    def up(self):
        """Sets snake positioning north"""
        self.snake_head.seth(90)


    def down(self):
        """Sets snake positioning south"""
        self.snake_head.seth(270)

    def left(self):
        """Sets snake positioning west"""
        self.snake_head.seth(180)

    def right(self):
        """Sets snake positioning east"""
        self.snake_head.seth(0)


    def add_part(self):
        """Function to add a new part"""
        t = Turtle('square')
        t.penup()
        t.speed('fastest')
        t.color('white')
        t.hideturtle() # Hide the turtle before being appended or else itll appear on screen
        self.snake_body.append(t)


class Parts:
    """Class to create dots to add to the snakes length"""

    def __init__(self, screen):
        self.screen = screen
        self.dot = Turtle('circle')
        self.dot.penup()
        self.dot.color('blue')
        self.dot.shapesize(.5,.5)
        self.dot.speed('fastest')

    def generate_dot_cor(self):
        x = randrange(-270, 270, 10)
        y = randrange(-270, 270, 10)
        return x,y



class Scoreboard(Turtle):
    """Class for holding all the scores"""
    
    def __init__(self):
        
        self.score = 0
        with open('scores.txt', 'r') as f:
            hs = f.read()
            self.high_score = int(hs)


        Turtle.__init__(self)

        self.goto(0, 275)
        self.color('white')
        self.hideturtle()
        self.write(f'Score: {self.score} High Score: {self.high_score}', False, align='center', font=('Arial', 16, 'normal'))

    def add_point(self):
        self.score += 1

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', False, align='center',
                   font=('Arial', 16, 'normal'))

    def save_score(self):
        if self.score > self.high_score:
            with open('scores.txt', 'w') as f:
                f.write(str(self.score))




    def game_over(self):
        self.clear()
        with open('scores.txt') as f:
            hs = f.read()
            self.write(f'Game Over! Final Score: {self.score} High Score: {hs}', False, align='center',
                            font=('Arial', 16, 'normal'))  # Set game over screen
            self.score = 0


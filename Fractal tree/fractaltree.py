import turtle
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class TurtleFacade:
    def __init__(self):
        self.turtle = TurtleAdapter()
        self.turtle.setup()

    def draw_tree(self, branch_length):
        self.turtle.draw_tree(branch_length)

class TurtleAdapter:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed("fastest")

    def setup(self):
        self.t.penup()
        self.t.goto(0, -450)
        self.t.pendown()
        self.t.hideturtle()
    
    def draw_branch(self, length):
        self.t.forward(length)

    def turn_left(self, angle):
        self.t.left(angle)

    def turn_right(self, angle):
        self.t.right(angle)

    def move_backward(self, length):
        self.t.backward(length)

class TreeBuilder:
    def __init__(self, turtle_adapter):
        self.turtle_adapter = turtle_adapter

    def build_tree(self, length):
        if length < 5:
            return
        else:
            self.turtle_adapter.draw_branch(length)
            self.turtle_adapter.turn_left(30)
            self.build_tree(3 * length / 4)
            self.turtle_adapter.turn_right(60)
            self.build_tree(3 * length / 4)
            self.turtle_adapter.turn_left(30)
            self.turtle_adapter.move_backward(length)

if __name__ == "__main__":
    branch_length = int(os.getenv("BRANCH_LENGTH", 250))  # Example using .env variable
    turtle_facade = TurtleFacade()
    tree_builder = TreeBuilder(turtle_facade.turtle)
    tree_builder.build_tree(branch_length)
    turtle.done()

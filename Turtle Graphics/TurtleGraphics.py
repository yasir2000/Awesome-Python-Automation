import os
from dotenv import load_dotenv
import turtle

# Adapter for environment variables
load_dotenv()

class Config:
    def __init__(self):
        self.bg_color = os.getenv('BACKGROUND_COLOR')
        self.turtle_shape = os.getenv('TURTLE_SHAPE')
        self.turtle_color = os.getenv('TURTLE_COLOR')
        self.turtle_speed = int(os.getenv('TURTLE_SPEED'))
        self.forward_distance = int(os.getenv('FORWARD_DISTANCE'))
        self.turn_angle = int(os.getenv('TURN_ANGLE'))
        self.rotate_angle = int(os.getenv('ROTATE_ANGLE'))
        self.final_move_distance = int(os.getenv('FINAL_MOVE_DISTANCE'))
        self.num_squares = int(os.getenv('NUM_SQUARES'))

config = Config()

# Singleton for Turtle Screen
class TurtleScreen:
    __instance = None

    @staticmethod
    def get_instance():
        if TurtleScreen.__instance is None:
            TurtleScreen()
        return TurtleScreen.__instance

    def __init__(self):
        if TurtleScreen.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.screen = turtle.Screen()
            TurtleScreen.__instance = self

# Factory Method for Turtle creation
class TurtleFactory:
    @staticmethod
    def create_turtle():
        screen = TurtleScreen.get_instance().screen
        screen.bgcolor(config.bg_color)
        return turtle.Turtle()

# Builder Pattern for Turtle configuration
class TurtleBuilder:
    def __init__(self):
        self.turtle = TurtleFactory.create_turtle()

    def set_shape(self):
        self.turtle.shape(config.turtle_shape)
        return self

    def set_color(self):
        self.turtle.color(config.turtle_color)
        return self

    def set_speed(self):
        self.turtle.speed(config.turtle_speed)
        return self

    def get_turtle(self):
        return self.turtle

# Strategy for different draw actions
class DrawStrategy:
    def draw(self, turtle_instance):
        pass

class DrawSquareStrategy(DrawStrategy):
    def draw(self, turtle_instance):
        for _ in range(4):
            turtle_instance.forward(config.forward_distance)
            turtle_instance.left(config.turn_angle)

# Main Turtle Drawing Application
class TurtleDrawingApp:
    def __init__(self, draw_strategy):
        self.turtle = TurtleBuilder().set_shape().set_color().set_speed().get_turtle()
        self.draw_strategy = draw_strategy

    def run(self):
        for _ in range(config.num_squares):
            self.draw_strategy.draw(self.turtle)
            self.turtle.right(config.rotate_angle)
        self.turtle.forward(config.final_move_distance)
        turtle.done()

# Client Code
if __name__ == "__main__":
    draw_strategy = DrawSquareStrategy()
    app = TurtleDrawingApp(draw_strategy)
    app.run()

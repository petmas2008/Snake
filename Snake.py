import pgzrun
import time

WIDTH = 400
HEIGHT = 400

# need to implement coord system

class GameObjects:

    def __init__(self, cell_number):
        self.cell_number = cell_number
        self.cell_size = WIDTH // cell_number, HEIGHT // cell_number
        self.board = {}


class Snake:

    def __init__(self, size):
        self.size = size
        self.snake_counter = 0
        self.snake_direction = None
        self.snake_speed = 0.5
        # The lower the number the fastest the snake goes
        # This is because this number is used as a parameter for time.sleep

    def get_snake_rect(self):
        x = self.snake_counter * game_objects.cell_size[0]
        y = self.snake_counter * game_objects.cell_size[1]
        if self.snake_direction == "down":
            x = y - game_objects.cell_size[1]
            print("down")
        return x, y

    def move_snake(self):
        snake_rect = Rect((self.get_snake_rect()), game_objects.cell_size)
        self.snake_counter += 1
        return snake_rect


game_objects = GameObjects(20)
snake = Snake(game_objects.cell_number)

for row in range(game_objects.cell_number):
    for column in range(game_objects.cell_number):
        game_objects.board[row, column] = "empty"
        

def on_key_down(key):
    if key == keys.W:
        snake.snake_direction = "up"
    if key == keys.S:
        snake.snake_direction = "down"
        snake.snake_counter += 1
        print("d")
    if key == keys.A:
        snake.snake_direction = "left"
    if key == keys.D:
        snake.snake_direction = "right"


def draw():
    screen_rect = Rect((0, 0), (WIDTH, HEIGHT))
    screen.draw.rect(screen_rect, (255, 255, 255))
    for cell in range(game_objects.cell_number):
        row_cell = cell * game_objects.cell_size[0]
        screen.draw.line(
            (row_cell, 0),
            (row_cell, HEIGHT),
            (255, 255, 255)
        )

    for cell in range(game_objects.cell_number):
        col_cell = cell * game_objects.cell_size[1]
        screen.draw.line(
            (0, col_cell),
            (WIDTH, col_cell),
            (255, 255, 255)
        )


def update():
    print("Hello")
    screen.clear()
    screen.draw.filled_rect(snake.move_snake(), (255, 255, 255))
    time.sleep(snake.snake_speed)


pgzrun.go()
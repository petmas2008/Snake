import pgzrun
import time

WIDTH = 400
HEIGHT = 400

# need to implement coord system


class GameObjects:

    def __init__(self, cell_number):
        self.cell_number = cell_number
        self.cell_size = WIDTH // cell_number, HEIGHT // cell_number


class Snake:

    def __init__(self, size):
        self.size = size
        self.x, self.y = 0, 0
        self.current_direction = None
        self.speed = 0.5
        # The lower the number the fastest the snake goes
        # This is because this number is used as a parameter for time.sleep

    def get_snake_rect(self):
        current_x = self.x * game_objects.cell_size[0]
        current_y = self.y * game_objects.cell_size[1]
        print(game_objects.cell_size)
        return current_x, current_y

    def move(self, direction):
        self.current_direction = direction
        if direction == "up":
            self.y -= 1
        elif direction == "down":
            self.y += 1
        elif direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1

    def draw_snake(self):
        self.move(self.current_direction)
        time.sleep(self.speed)
        snake_rect = Rect((self.get_snake_rect()), game_objects.cell_size)
        return snake_rect


game_objects = GameObjects(20)
snake = Snake(game_objects.cell_number)


def on_key_down(key):
    if key == keys.W:
        snake.move("up")
    if key == keys.S:
        snake.move("down")
    if key == keys.A:
        snake.move("left")
    if key == keys.D:
        snake.move("right")


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
    screen.clear()
    screen.draw.filled_rect(snake.draw_snake(), (255, 255, 255))


pgzrun.go()
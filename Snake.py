import pgzrun
import time
import random

WIDTH = 400
HEIGHT = 400

# need to implement coord system


class GameObjects:

    def __init__(self, cell_number):
        self.cell_number = cell_number
        self.cell_size = WIDTH // cell_number, HEIGHT // cell_number


class Snake:

    def __init__(self, board_size, speed):
        self.board_size = board_size
        self.x, self.y = self.board_size // 2 - 1, self.board_size // 2 - 1
        self.current_direction = None
        self.speed = speed
        self.move_status = True
        self.blocked_direction = None
        # The lower the number the fastest the snake goes
        # This is because this number is used as a parameter for time.sleep

    def get_snake_rect(self):
        current_x = self.x * game_objects.cell_size[0]
        current_y = self.y * game_objects.cell_size[1]
        return current_x, current_y
    
    def check_movement_against_side(self, direction, blocked_direction):
        if blocked_direction != direction:
            return True
        else:
            return False

    def move(self, direction):
        self.current_direction = direction
        if self.move_status or self.check_movement_against_side(direction, self.blocked_direction):
            if direction == "up":
                self.y -= 1
            elif direction == "down":
                self.y += 1
            elif direction == "left":
                self.x -= 1
            elif direction == "right":
                self.x += 1

    def check_boundaries(self, x, y, boundary):
        if x == boundary - 1:
            self.move_status = False
            self.blocked_direction = "right"
        elif y == boundary - 1:
            self.move_status = False
            self.blocked_direction = "down"
        elif x <= 0:
            self.move_status = False
            self.blocked_direction = "left"
        elif y <= 0:
            self.move_status = False
            self.blocked_direction = "up"
        else:
            self.move_status = True
            self.blocked_direction = None

    def draw_snake(self):
        self.check_boundaries(self.x, self.y, self.board_size)
        self.move(self.current_direction)
        time.sleep(self.speed)
        snake_rect = Rect((self.get_snake_rect()), game_objects.cell_size)
        return snake_rect

class Consumable:
    
    def __init__(self, board_size):
        self.board_size = board_size
        self.x, self.y = 0, 0
        self.hit = False
        self.start_of_game = True
    
    def check_if_hit(self, snake_x, snake_y, cons_x, cons_y):
        print("snake =>", snake_x, snake_y)
        print("cons =>", cons_x, cons_y)
        if (snake_x, snake_y) == (cons_x, cons_y):
            self.hit = True
        else:
            self.hit = False

    def randomize_pos(self):
        # Checks whether the consumable has been eaten
        self.check_if_hit(snake.x, snake.y, self.x, self.y)
        if consumable.hit or self.start_of_game:
            self.x = random.randint(0, self.board_size) 
            self.y = random.randint(0, self.board_size)
            current_x = self.x * game_objects.cell_size[0]
            current_y = self.y * game_objects.cell_size[1]
            self.start_of_game = False
        return self.x * game_objects.cell_size[0], self.y * game_objects.cell_size[1]

    def draw_consumable(self):
        return Rect(self.randomize_pos(), game_objects.cell_size)


game_objects = GameObjects(20)
snake = Snake(game_objects.cell_number, 0.25)
consumable = Consumable(game_objects.cell_number)


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
    # These are rectangles for  
    # certain objects in the programme
    screen_rect = Rect((0, 0), (WIDTH, HEIGHT))
    snake_rect = snake.draw_snake()
    consumable_rect = consumable.draw_consumable()

    screen.draw.rect(screen_rect, (255, 255, 255))
    screen.draw.filled_rect(snake_rect, (0, 255, 0))
    screen.draw.filled_rect(consumable_rect, (255, 0, 0))

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


pgzrun.go()

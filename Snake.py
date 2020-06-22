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
        self.start_of_game = True


class Snake:

    def __init__(self, board_size, speed):
        self.board_size = board_size
        self.x, self.y = 0, 0
        self.current_direction = None
        self.speed = speed
        self.move_status = True
        self.blocked_direction = None
        self.length = 1
        # The lower the number the fastest the snake goes
        # This is because this number is used as a parameter for time.sleep
    
    def analyse_length(self, length, direction, cell_size_x, cell_size_y):
        # cx, cy are the current_x and current_y for the rect 
        # in the function where it is being called
        if direction == "up":
            cy -= game_objects.cell_size[1] * length
        if direction == "down":
            cy += game_objects.cell_size[1] * length
        if direction == "left":
            cx -= game_objects.cell_size[0] * length
        if direction == "right":
            cx += game_objects.cell_size[0] * length
        return cell_size_x, cell_size_y


    def get_snake_rect(self, length, direction):
        current_x = self.x * game_objects.cell_size[0]
        current_y = self.y * game_objects.cell_size[1]
        return current_x, current_y
    
    def check_movement_against_side(self, direction, blocked_direction):
        # returns a true or false
        return direction not in blocked_direction

    def move(self, direction):
        movement_status = self.check_movement_against_side(direction, self.blocked_direction)
        if self.move_status or movement_status:
            if direction == "up":
                self.y -= 1
            elif direction == "down":
                self.y += 1
            elif direction == "left":
                self.x -= 1
            elif direction == "right":
                self.x += 1

    def check_boundaries(self, x, y, boundary):
        self.move_status = True
        self.blocked_direction = []
        if x == 0:
            self.move_status = False
            self.blocked_direction.append("left")
        if y == 0:
            self.move_status = False
            self.blocked_direction.append("up")
        if x == boundary - 1:
            self.move_status = False
            self.blocked_direction.append("right")
        if y == boundary - 1:
            self.move_status = False
            self.blocked_direction.append("down")

    def draw_snake(self):
	    self.check_boundaries(self.x, self.y, self.board_size)
        self.move(self.current_direction)
        time.sleep(self.speed)
        snake_rect = Rect((self.get_snake_rect(self.length, self.current_direction)), game_objects.cell_size)
        return snake_rect


class Consumable:
    
    def __init__(self, board_size):
        self.board_size = board_size
        self.x, self.y = 0, 0
        self.hit = False
    
    def check_if_hit(self, snake_x, snake_y, cons_x, cons_y):
        if (snake_x, snake_y) == (cons_x, cons_y):
            snake.length += 1
            self.hit = True
        else:
            self.hit = False

    def randomize_pos(self):
        # Checks whether the consumable has been eaten
        self.check_if_hit(snake.x, snake.y, self.x, self.y)
        if consumable.hit or game_objects.start_of_game:
            # I am doing -1 because it thats the way it needs to be drawn
            self.x = random.randint(0, self.board_size - 1) 
            self.y = random.randint(0, self.board_size - 1)
            game_objects.start_of_game = False
        current_x = self.x * game_objects.cell_size[0]
        current_y = self.y * game_objects.cell_size[1]
        return current_x, current_y

    def draw_consumable(self):
        return Rect(self.randomize_pos(), game_objects.cell_size)
        


game_objects = GameObjects(20)
snake = Snake(game_objects.cell_number, 0.10)
consumable = Consumable(game_objects.cell_number)


def on_key_down(key):
    if key == keys.W:
        snake.current_direction = "up"
    if key == keys.S:
        snake.current_direction = "down"
    if key == keys.A:
        snake.current_direction = "left"
    if key == keys.D:
        snake.current_direction = "right"


def draw():
    # These are rectangles for  
    # certain objects in the programme
    screen_rect = Rect((0, 0), (WIDTH, HEIGHT))
    snake_rect = snake.draw_snake()
    consumable_rect = consumable.draw_consumable()
    # Actually drawing the rectangles on the screen 
    screen.draw.rect(screen_rect, (255, 255, 255))
    screen.draw.filled_rect(snake_rect, (0, 255, 0))
    screen.draw.filled_rect(consumable_rect, (255, 0, 0))
    # Draws a grid
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

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
        self.x, self.y = 0, 0
        self.current_direction = None
        self.speed = speed
        self.move_status = True
        self.blocked_direction = None
        self.length = 1
        self.create_coord_sys()
        # cooThe lower the number the fastest the snake goes
        # This is because this number is used as a parameter for time.sleep

    def create_coord_sys(self):
        self.coord_sys = {}
        for y in range(game_objects.cell_number):
            for x in range(game_objects.cell_number):
                self.coord_sys[x, y] = False
        self.coord_sys[self.x, self.y] = True

    def clear_coord_sys(self):
        for x, y in self.coord_sys.keys():
            self.coord_sys[x, y] = False

    def update_coord_sys(self):
        self.coord_sys[self.x, self.y] = True
        for current_length in range(self.length):
            self.coord_sys[self.analyse_length(current_length)] = True

    def analyse_length(self, current_length):
        if self.current_direction == "up":
            return self.y + current_length, self.x
        if self.current_direction == "down":
            return self.y - current_length, self.x
        if self.current_direction == "left":
            return self.y, self.x  - current_length
        if self.current_direction == "right":
            return self.y, self.x + current_length

    def get_snake_rect(self):
        current_x = self.x * game_objects.cell_size[0]
        current_y = self.y * game_objects.cell_size[1]
        return current_x, current_y

    def check_movement_against_side(self):
        # returns a true or false
        return self.current_direction not in self.blocked_direction

    def move(self, direction):
        movement_status = self.check_movement_against_side()
        if self.move_status or movement_status:
            if direction == "up":
                self.y -= 1
            elif direction == "down":
                self.y += 1
            elif direction == "left":
                self.x -= 1
            elif direction == "right":
                self.x += 1
        self.clear_coord_sys()
        self.update_coord_sys()
        print(self.coord_sys)

    def check_boundaries(self):
        self.move_status = True
        self.blocked_direction = []
        if self.x == 0:
            self.move_status = False
            self.blocked_direction.append("left")
        if self.y == 0:
            self.move_status = False
            self.blocked_direction.append("up")
        if self.x == self.board_size - 1:
            self.move_status = False
            self.blocked_direction.append("right")
        if self.y == self.board_size - 1:
            self.move_status = False
            self.blocked_direction.append("down")

    def draw_snake(self):
        # size = self.analyse_length()
        self.check_boundaries()
        self.move(self.current_direction)
        time.sleep(self.speed)
        # snake_rect = Rect((self.get_snake_rect()), size)
        # return snake_rect
        snake_info = []
        for x, y in self.coord_sys.keys():
            if self.coord_sys[x, y]:
                snake_info.append((x * game_objects.cell_size[0], y * game_objects.cell_size[1]))
        return snake_info
 

class Consumable:

    def __init__(self, board_size):
        self.board_size = board_size
        self.randomize_pos()
        self.hit = False

    def check_if_hit(self):
        if (snake.x, snake.y) == (self.x, self.y):
            snake.length += 1
            snake.coord_sys[snake.x, snake.y] = True
            self.hit = True
        else:
            self.hit = False

    def randomize_pos(self):
        self.x = random.randint(0, self.board_size - 1)
        self.y = random.randint(0, self.board_size - 1)

    def move_if_needed(self):
        # Checks whether the consumable has been eaten
        self.check_if_hit()
        if self.hit:
            # I am doing -1 because it thats the way it needs to be drawn
            self.randomize_pos()
        return self.get_consumable_rect()

    def get_consumable_rect(self):
        current_x = self.x * game_objects.cell_size[0]
        current_y = self.y * game_objects.cell_size[1]
        return current_x, current_y

    def draw_consumable(self):
        return Rect(self.move_if_needed(), game_objects.cell_size)


game_objects = GameObjects(20)
snake = Snake(game_objects.cell_number, 0.15)
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
    # snake_rect = snake.draw_snake()
    consumable_rect = consumable.draw_consumable()
    # Actually drawing the rectangles on the screen 
    screen.draw.rect(screen_rect, (255, 255, 255))
    # screen.draw.filled_rect(snake_rect, (0, 255, 0))
    screen.draw.filled_rect(consumable_rect, (255, 0, 0))

    for x, y in snake.draw_snake():
        current_rect = Rect((x, y), game_objects.cell_size)
        screen.draw.filled_rect(current_rect, (0, 255, 0))

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

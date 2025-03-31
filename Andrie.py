
import simplegui
import math

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 500
BUTTON_SIZE = (200, 50)
TITLE_POS = (CANVAS_WIDTH / 2, 100)
BUTTON_START_POS = (CANVAS_WIDTH / 2 - BUTTON_SIZE[0] / 2, 180)
BUTTON_HELP_POS = (CANVAS_WIDTH / 2 - BUTTON_SIZE[0] / 2, 250)
BUTTON_QUIT_POS = (CANVAS_WIDTH / 2 - BUTTON_SIZE[0] / 2, 320)

game_state = "MENU"  

time = 0

YELLOW = '#FFFF00'
BLACK = '#000000'
BLUE = '#0000FF'
DARK_BLUE = '#000080'
WHITE = '#FFFFFF'
RED = '#FF0000'
PINK = '#FFC0CB'
ORANGE = '#FFA500'
CYAN = '#00FFFF'

pacman_pos = [50, 50]
pacman_dir = [1, 0]
pacman_speed = 3
pacman_radius = 15
pacman_mouth_angle = 0.7  

ghosts = [
    {"pos": [CANVAS_WIDTH - 50, 50], "color": RED},
    {"pos": [CANVAS_WIDTH - 100, 100], "color": PINK},
    {"pos": [CANVAS_WIDTH - 150, 150], "color": CYAN},
    {"pos": [CANVAS_WIDTH - 200, 200], "color": ORANGE}
]

dots = []
for x in range(50, CANVAS_WIDTH - 50, 30):
    for y in range(400, 450, 30):
        dots.append((x, y))

def draw_pacman(canvas, x, y, mouth_angle):
    if time % 30 < 15:
        canvas.draw_circle((x, y), pacman_radius, 1, YELLOW, YELLOW)
        mouth_point = (x + pacman_radius * math.cos(0), y + pacman_radius * math.sin(0))
        canvas.draw_polygon([
            (x, y),
            (x + pacman_radius * math.cos(-mouth_angle/2), y + pacman_radius * math.sin(-mouth_angle/2)),
            (x + pacman_radius * math.cos(mouth_angle/2), y + pacman_radius * math.sin(mouth_angle/2))
        ], 1, BLACK, BLACK)
    else:
        canvas.draw_circle((x, y), pacman_radius, 1, YELLOW, YELLOW)
    
    canvas.draw_circle((x, y - pacman_radius/2), pacman_radius/8, 1, BLACK, BLACK)

def draw_ghost(canvas, x, y, color):
    canvas.draw_polygon([
        (x - 15, y),
        (x - 10, y - 10),
        (x - 5, y - 13),
        (x, y - 15),
        (x + 5, y - 13),
        (x + 10, y - 10),
        (x + 15, y)
    ], 1, color, color)
    
    canvas.draw_polygon([
        (x - 15, y), 
        (x + 15, y),
        (x + 15, y + 20),
        (x + 10, y + 15),
        (x + 5, y + 20),
        (x, y + 15),
        (x - 5, y + 20),
        (x - 10, y + 15),
        (x - 15, y + 20)
    ], 1, color, color)
   
    canvas.draw_circle((x - 5, y - 3), 3, 1, WHITE, WHITE)
    canvas.draw_circle((x + 5, y - 3), 3, 1, WHITE, WHITE)
    canvas.draw_circle((x - 5, y - 3), 1, 1, BLACK, BLACK)
    canvas.draw_circle((x + 5, y - 3), 1, 1, BLACK, BLACK)

def draw_button(canvas, pos, size, text, text_pos, text_size):
   
    fill_color = BLUE
    border_width = 2
    
    canvas.draw_polygon([
        (pos[0], pos[1]),
        (pos[0] + size[0], pos[1]),
        (pos[0] + size[0], pos[1] + size[1]),
        (pos[0], pos[1] + size[1])
    ], border_width, YELLOW, fill_color)
    
    canvas.draw_text(text, text_pos, text_size, YELLOW)

def draw_handler(canvas):
    global time, pacman_pos
    time += 1
    
    canvas.draw_polygon([(0, 0), (CANVAS_WIDTH, 0), 
                        (CANVAS_WIDTH, CANVAS_HEIGHT), 
                        (0, CANVAS_HEIGHT)], 
                       1, BLACK, BLACK)
    
    for dot in dots:
        canvas.draw_circle(dot, 3, 1, YELLOW, YELLOW)
    
    if game_state == "MENU":
        pacman_pos[0] = (pacman_pos[0] + pacman_dir[0] * pacman_speed) % CANVAS_WIDTH
        pacman_pos[1] = (pacman_pos[1] + pacman_dir[1] * pacman_speed) % 400
        
        draw_pacman(canvas, pacman_pos[0], pacman_pos[1], pacman_mouth_angle)
        
        for ghost in ghosts:
            draw_ghost(canvas, ghost["pos"][0], ghost["pos"][1], ghost["color"])
            ghost["pos"][0] = (ghost["pos"][0] - 1) % CANVAS_WIDTH
        
        title_size = 72 + math.sin(time / 10) * 5
        canvas.draw_text("PACMAN", 
                        [TITLE_POS[0] - 120, TITLE_POS[1]], 
                        title_size, YELLOW)
        
        canvas.draw_text("THE CLASSIC ARCADE GAME", 
                       [TITLE_POS[0] - 160, TITLE_POS[1] + 40], 
                       24, WHITE)
        
        draw_button(
            canvas,
            BUTTON_START_POS, 
            BUTTON_SIZE,
            "Start Game",
            [BUTTON_START_POS[0] + 50, BUTTON_START_POS[1] + 35],
            24
        )
        
        draw_button(
            canvas,
            BUTTON_HELP_POS, 
            BUTTON_SIZE,
            "Help",
            [BUTTON_HELP_POS[0] + 75, BUTTON_HELP_POS[1] + 35],
            24
        )
        
        draw_button(
            canvas,
            BUTTON_QUIT_POS, 
            BUTTON_SIZE,
            "Quit",
            [BUTTON_QUIT_POS[0] + 75, BUTTON_QUIT_POS[1] + 35],
            24
        )
        
        canvas.draw_text("(c) 2023", 
                       [CANVAS_WIDTH / 2 - 30, CANVAS_HEIGHT - 20], 
                       16, WHITE)
    
    elif game_state == "HELP":
        canvas.draw_text("HOW TO PLAY", [TITLE_POS[0] - 120, 80], 50, YELLOW)
        
        y_pos = 150
        for instruction in [
            "- Use ARROW KEYS to move PacMan",
            "- Eat all dots to advance to the next level",
            "- Avoid ghosts or lose a life",
            "- Eat power pellets to hunt ghosts",
            "- Score points by eating dots and ghosts"
        ]:
            canvas.draw_text(instruction, [100, y_pos], 20, WHITE)
            y_pos += 30
        
        canvas.draw_text("CONTROLS:", [100, y_pos + 20], 24, YELLOW)
        canvas.draw_text("UP DOWN LEFT RIGHT : Move PacMan", [120, y_pos + 50], 20, WHITE)
        canvas.draw_text("P : Pause Game", [120, y_pos + 80], 20, WHITE)
        
        canvas.draw_text("Press B to return to menu", [CANVAS_WIDTH / 2 - 140, CANVAS_HEIGHT - 50], 24, YELLOW)
        
        draw_pacman(canvas, 50, CANVAS_HEIGHT - 80, pacman_mouth_angle)
        draw_ghost(canvas, CANVAS_WIDTH - 50, CANVAS_HEIGHT - 80, RED)
    
    elif game_state == "GAME":
        canvas.draw_text("GAME STARTED", [TITLE_POS[0] - 120, TITLE_POS[1]], 50, YELLOW)
        canvas.draw_text("This is where the game would run", [150, 200], 20, WHITE)
        
        draw_pacman(canvas, CANVAS_WIDTH / 2, 250, pacman_mouth_angle)
        
        for i, ghost in enumerate(ghosts):
            draw_ghost(canvas, CANVAS_WIDTH / 2 - 100 + i * 50, 250, ghost["color"])
        
        canvas.draw_text("SCORE: 0", [50, 50], 24, WHITE)
        canvas.draw_text("LIVES: 3", [CANVAS_WIDTH - 150, 50], 24, WHITE)
        canvas.draw_text("LEVEL: 1", [CANVAS_WIDTH / 2 - 50, 50], 24, WHITE)
        
        canvas.draw_text("Press B to return to menu", [CANVAS_WIDTH / 2 - 140, CANVAS_HEIGHT - 50], 24, YELLOW)

def mouse_handler(position):
    global game_state
    
    if game_state == "MENU":
        if (BUTTON_START_POS[0] < position[0] < BUTTON_START_POS[0] + BUTTON_SIZE[0] and
            BUTTON_START_POS[1] < position[1] < BUTTON_START_POS[1] + BUTTON_SIZE[1]):
            game_state = "GAME"
        
        elif (BUTTON_HELP_POS[0] < position[0] < BUTTON_HELP_POS[0] + BUTTON_SIZE[0] and
              BUTTON_HELP_POS[1] < position[1] < BUTTON_HELP_POS[1] + BUTTON_SIZE[1]):
            game_state = "HELP"
        
        elif (BUTTON_QUIT_POS[0] < position[0] < BUTTON_QUIT_POS[0] + BUTTON_SIZE[0] and
              BUTTON_QUIT_POS[1] < position[1] < BUTTON_QUIT_POS[1] + BUTTON_SIZE[1]):
            frame.stop()

def key_handler(key):
    global game_state
    
    if key == simplegui.KEY_MAP['b']:
        if game_state == "HELP" or game_state == "GAME":
            game_state = "MENU"

frame = simplegui.create_frame("PacMan Menu", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(mouse_handler)
frame.set_keydown_handler(key_handler)

frame.start()

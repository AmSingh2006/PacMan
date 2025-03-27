try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

game_started = False

sprite_sheet_url = "https://www.cs.rhul.ac.uk/home/znac610/cs1822/gamesprite.png"
sprite_sheet = simplegui.load_image(sprite_sheet_url)

# Button dimensions and position
button_pos = (280, 300)  
button_size = (70, 40)   
# Pac-Man ball properties
ball_pos = [300, 360]  
ball_radius = 8       
ball_speed = 3         

# Key state for movement
key_states = {"left": False, "right": False, "up": False, "down": False}

# Handler for the start button
def start_game():
    global game_started
    game_started = True
    frame.set_draw_handler(game_draw)  
    frame.start()  

#  welcome screen
def welcome_draw(canvas):
    canvas.draw_text("Welcome to Ball-Man!", (100, 200), 50, "Yellow")
    canvas.draw_text("Press the Start button to begin!", (140, 290), 30, "White")
    
    # Draw the custom button
    canvas.draw_polygon([button_pos, 
                         (button_pos[0] + button_size[0], button_pos[1]), 
                         (button_pos[0] + button_size[0], button_pos[1] + button_size[1]), 
                         (button_pos[0], button_pos[1] + button_size[1])], 
                        1, "White", "Blue")
    canvas.draw_text("Start", (button_pos[0] + 10, button_pos[1] + 30), 24, "White")

# Draw handler for the game
def game_draw(canvas):
    canvas.draw_image(sprite_sheet, 
                      (sprite_sheet.get_width() / 2, sprite_sheet.get_height() / 2),  # Center of the image
                      (sprite_sheet.get_width(), sprite_sheet.get_height()),        # Full image dimensions
                      (300, 250),                                                  # Display above the game
                      (550, 450))                                                  # Display dimensions

    # Draw the Pac-Man ball
    canvas.draw_circle(ball_pos, ball_radius, 2, "Yellow", "Yellow")
    
    # Update ball position based on key states
    if key_states["left"]:
        ball_pos[0] -= ball_speed
    if key_states["right"]:
        ball_pos[0] += ball_speed
    if key_states["up"]:
        ball_pos[1] -= ball_speed
    if key_states["down"]:
        ball_pos[1] += ball_speed

    # Ensure ball stays within canvas bounds
    ball_pos[0] = max(ball_radius, min(600 - ball_radius, ball_pos[0]))
    ball_pos[1] = max(ball_radius, min(500 - ball_radius, ball_pos[1]))

# Mouse click handler
def mouse_click(pos):
    if (button_pos[0] <= pos[0] <= button_pos[0] + button_size[0] and
        button_pos[1] <= pos[1] <= button_pos[1] + button_size[1]):
        start_game()

# Key down handler
def key_down(key):
    if key == simplegui.KEY_MAP["left"]:
        key_states["left"] = True
    elif key == simplegui.KEY_MAP["right"]:
        key_states["right"] = True
    elif key == simplegui.KEY_MAP["up"]:
        key_states["up"] = True
    elif key == simplegui.KEY_MAP["down"]:
        key_states["down"] = True

# Key up handler
def key_up(key):
    if key == simplegui.KEY_MAP["left"]:
        key_states["left"] = False
    elif key == simplegui.KEY_MAP["right"]:
        key_states["right"] = False
    elif key == simplegui.KEY_MAP["up"]:
        key_states["up"] = False
    elif key == simplegui.KEY_MAP["down"]:
        key_states["down"] = False


frame = simplegui.create_frame("Pac-Man Game", 600, 500)
frame.set_draw_handler(welcome_draw)
frame.set_mouseclick_handler(mouse_click)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
frame.start()

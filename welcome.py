# Import the SimpleGUI module
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Global variable to track game state
game_started = False

# Button dimensions and position
button_pos = (280, 300)  # X, Y position of the button
button_size = (70, 40)   # Width, Height of the button

# Handler for the start button
def start_game():
    global game_started
    game_started = True
    frame.set_draw_handler(game_draw)  # Set the draw handler for the game
    frame.start()  # Start the frame

# Draw handler for the welcome screen
def welcome_draw(canvas):
    # Centered text
    canvas.draw_text("Welcome to Ball-Man!", (100, 200), 50, "Yellow")
    canvas.draw_text("Press the Start button to begin!", (140, 290), 30, "White")
    
    # Draw the custom button
    canvas.draw_polygon([button_pos, 
                         (button_pos[0] + button_size[0], button_pos[1]), 
                         (button_pos[0] + button_size[0], button_pos[1] + button_size[1]), 
                         (button_pos[0], button_pos[1] + button_size[1])], 
                        1, "White", "Blue")
    canvas.draw_text("Start", (button_pos[0] + 10, button_pos[1] + 30), 24, "White")

# Draw handler for the game (placeholder)
def game_draw(canvas):
    canvas.draw_text("Game is starting...", (100, 100), 36, "Yellow")
    # Here you would add your game logic and drawing code

# Mouse click handler
def mouse_click(pos):
    if (button_pos[0] <= pos[0] <= button_pos[0] + button_size[0] and
        button_pos[1] <= pos[1] <= button_pos[1] + button_size[1]):
        start_game()

# Create a frame
frame = simplegui.create_frame("Pac-Man Game", 600, 500)

# Set the draw handler for the welcome screen
frame.set_draw_handler(welcome_draw)

# Set the mouse click handler
frame.set_mouseclick_handler(mouse_click)

# Start the frame
frame.start()
try:
    import simplegui
except ImportError: 
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

sprite_sheet_url = "gamesprite.png"  
sprite_sheet = simplegui.load_image(sprite_sheet_url)
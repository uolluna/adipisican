import pygame

# Initialize Pygame and the joystick
pygame.init()
pygame.joystick.init()

# Assuming you have at least one joystick connected
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if the Y button (typically button index 3) is pressed
    if joystick.get_button(3):  # Y button
        print("Y button pressed")

# Clean up
pygame.quit()

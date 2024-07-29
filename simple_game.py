import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Collision Theory")

# Define colors
PURPLE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Player settings
player_size = 50
player_x = 375
player_y = 275
player_speed = 5

# Enemy settings
enemy_size = 50
num_enemies = 5
enemies = [{'x': random.randint(0, 750), 'y': random.randint(0, 550), 'speed': 3} for _ in range(num_enemies)]

# Score
score = 0
font = pygame.font.Font(None, 36)

# Load sounds
pygame.mixer.music.load('C:/Users/momoh/Documents/background_music.mp3.mp3')
collision_sound = pygame.mixer.Sound('C:/Users/momoh/Documents/collision_sound.wav.mp3')

# Play background music
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the set of keys pressed
    keys = pygame.key.get_pressed()

    # Move the player based on key presses
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Prevent the player from moving off the screen
    if player_x < 0:
        player_x = 0
    if player_x > 800 - player_size:
        player_x = 800 - player_size
    if player_y < 0:
        player_y = 0
    if player_y > 600 - player_size:
        player_y = 600 - player_size

    # Move the enemies
    for enemy in enemies:
        enemy['x'] += random.choice([-enemy['speed'], enemy['speed']])
        enemy['y'] += random.choice([-enemy['speed'], enemy['speed']])

        # Prevent the enemies from moving off the screen
        if enemy['x'] < 0:
            enemy['x'] = 0
        if enemy['x'] > 800 - enemy_size:
            enemy['x'] = 800 - enemy_size
        if enemy['y'] < 0:
            enemy['y'] = 0
        if enemy['y'] > 600 - enemy_size:
            enemy['y'] = 600 - enemy_size

    # Check for collision
    for enemy in enemies:
        if (player_x < enemy['x'] + enemy_size and
            player_x + player_size > enemy['x'] and
            player_y < enemy['y'] + enemy_size and
            player_y + player_size > enemy['y']):
            collision_sound.play()
            running = False

    # Update the score
    score += 1
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))

    # Fill the screen with a color
    screen.fill(PURPLE)

    # Draw the player character
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    # Draw the enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy['x'], enemy['y'], enemy_size, enemy_size))

    # Draw the score
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

import pygame
import sys
import random

# Constants for screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 50
ENEMY_SIZE = 50
NUM_ENEMIES = 5
PLAYER_SPEED = 5
PURPLE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Collision Theory")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.running = True
        self.player_x = SCREEN_WIDTH // 2 - PLAYER_SIZE // 2
        self.player_y = SCREEN_HEIGHT // 2 - PLAYER_SIZE // 2
        self.enemies = [{'x': random.randint(0, SCREEN_WIDTH - ENEMY_SIZE), 'y': random.randint(0, SCREEN_HEIGHT - ENEMY_SIZE), 'speed': 3} for _ in range(NUM_ENEMIES)]
        self.load_sounds()
        pygame.mixer.music.play(-1)  # Play background music indefinitely

    def load_sounds(self):
        try:
            pygame.mixer.music.load('C:/Users/momoh/Documents/background_music.mp3.mp3')
            self.collision_sound = pygame.mixer.Sound('C:/Users/momoh/Documents/collision_sound.wav.mp3')
        except pygame.error as e:
            print(f"Error loading sound: {e}")
            sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def move_player(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.player_x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.player_y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.player_y += PLAYER_SPEED

        # Ensure the player doesn't move off the screen
        self.player_x = max(0, min(self.player_x, SCREEN_WIDTH - PLAYER_SIZE))
        self.player_y = max(0, min(self.player_y, SCREEN_HEIGHT - PLAYER_SIZE))

    def move_enemies(self):
        for enemy in self.enemies:
            enemy['x'] += random.choice([-enemy['speed'], enemy['speed']])
            enemy['y'] += random.choice([-enemy['speed'], enemy['speed']])
            enemy['x'] = max(0, min(enemy['x'], SCREEN_WIDTH - ENEMY_SIZE))
            enemy['y'] = max(0, min(enemy['y'], SCREEN_HEIGHT - ENEMY_SIZE))

    def check_collision(self):
        for enemy in self.enemies:
            if (self.player_x < enemy['x'] + ENEMY_SIZE and
                self.player_x + PLAYER_SIZE > enemy['x'] and
                self.player_y < enemy['y'] + ENEMY_SIZE and
                self.player_y + PLAYER_SIZE > enemy['y']):
                self.collision_sound.play()
                self.running = False

    def update_score(self):
        self.score += 1
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))

    def draw(self):
        self.screen.fill(PURPLE)
        pygame.draw.rect(self.screen, BLUE, (self.player_x, self.player_y, PLAYER_SIZE, PLAYER_SIZE))
        for enemy in self.enemies:
            pygame.draw.rect(self.screen, RED, (enemy['x'], enemy['y'], ENEMY_SIZE, ENEMY_SIZE))

    def run(self):
        while self.running:
            self.handle_events()
            self.move_player()
            self.move_enemies()
            self.check_collision()
            self.update_score()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()

import pygame
import os
import sys

pygame.init()
pygame.mixer.init()

# Window
WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

# Colors
BLACK = (10, 10, 10)
GREEN = (0, 200, 100)
DARK_GREEN = (0, 150, 80)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)

# Font
font = pygame.font.SysFont("Arial", 26)

# Playlist
playlist = [
    {"file": "Practice-09/music_player/songs/song1pack/song1.mp3", "cover": "Practice-09/music_player/songs/song1pack/cover1.jpeg"},
    {"file": "Practice-09/music_player/songs/song2pack/song2.mp3", "cover": "Practice-09/music_player/songs/song2pack/cover2.jpg"},
    {"file": "Practice-09/music_player/songs/song3pack/song3.mp3", "cover": "Practice-09/music_player/songs/song3pack/cover3.png"}
]

current_track = 0
playing = False
started = False

# Load track
def load_track():
    global started
    pygame.mixer.music.load(playlist[current_track]["file"])
    pygame.mixer.music.play()
    started = True

# Load cover
def get_cover():
    img = pygame.image.load(playlist[current_track]["cover"]).convert_alpha()
    return pygame.transform.scale(img, (200, 200))

# Button class with animation
class CircleButton:
    def __init__(self, x, y, radius, text):
        self.x = x
        self.y = y
        self.base_radius = radius
        self.radius = radius
        self.text = text
        self.pressed = False

    def draw(self):
        color = DARK_GREEN if self.pressed else GREEN
        pygame.draw.circle(screen, color, (self.x, self.y), int(self.radius))

        label = font.render(self.text, True, BLACK)
        rect = label.get_rect(center=(self.x, self.y))
        screen.blit(label, rect)

    def update(self):
        # Animation: shrink when pressed
        if self.pressed:
            self.radius = self.base_radius * 0.9
        else:
            self.radius += (self.base_radius - self.radius) * 0.2

    def is_clicked(self, pos):
        dist = ((pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2) ** 0.5
        return dist <= self.radius


# Create buttons
btn_prev = CircleButton(300, 320, 30, "<")
btn_toggle = CircleButton(400, 320, 40, "||")
btn_next = CircleButton(500, 320, 30, ">")

# UI
def draw_ui():
    screen.fill(BLACK)

    # Album cover
    cover = get_cover()
    screen.blit(cover, (50, 100))

    # Track name
    name = os.path.basename(playlist[current_track]["file"])
    text = font.render(name, True, WHITE)
    screen.blit(text, (300, 120))

    # Status
    status = "Playing" if playing else "Paused"
    status_text = font.render(status, True, GRAY)
    screen.blit(status_text, (300, 160))

    # Progress
    pos = pygame.mixer.music.get_pos() // 1000
    time_text = font.render(f"{pos} sec", True, GRAY)
    screen.blit(time_text, (300, 200))

    # Update icon
    btn_toggle.text = "||" if playing else "V"

    # Update + draw buttons
    for btn in [btn_prev, btn_toggle, btn_next]:
        btn.update()
        btn.draw()

    pygame.display.flip()


# Main loop
clock = pygame.time.Clock()
running = True

while running:
    draw_ui()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if btn_toggle.is_clicked(pos):
                btn_toggle.pressed = True

                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    if not started:
                        load_track()
                    else:
                        pygame.mixer.music.unpause()
                    playing = True

            elif btn_next.is_clicked(pos):
                btn_next.pressed = True
                current_track = (current_track + 1) % len(playlist)
                load_track()
                playing = True

            elif btn_prev.is_clicked(pos):
                btn_prev.pressed = True
                current_track = (current_track - 1) % len(playlist)
                load_track()
                playing = True

        if event.type == pygame.MOUSEBUTTONUP:
            btn_toggle.pressed = False
            btn_next.pressed = False
            btn_prev.pressed = False

        # Keyboard (optional)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p or event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    if not started:
                        load_track()
                    else:
                        pygame.mixer.music.unpause()
                    playing = True

            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(playlist)
                load_track()
                playing = True

            elif event.key == pygame.K_b:
                current_track = (current_track - 1) % len(playlist)
                load_track()
                playing = True

            elif event.key == pygame.K_q:
                running = False

    clock.tick(60)

pygame.quit()
sys.exit()
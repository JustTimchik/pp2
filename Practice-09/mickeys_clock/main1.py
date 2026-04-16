import pygame
import sys
import datetime

# Initialize pygame
pygame.init()

# Load images

clock_img = pygame.image.load("Practice-09/mickeys_clock/images1/clock.png")
minute_hand_img = pygame.image.load("Practice-09/mickeys_clock/images1/firsthand.png")
second_hand_img = pygame.image.load("Practice-09/mickeys_clock/images1/secondhand.png")
clock_w, clock_h = clock_img.get_size()
minute_hand_img = pygame.transform.scale(minute_hand_img, (clock_w // 6, clock_h // 2.5))
second_hand_img = pygame.transform.scale(second_hand_img, (clock_w // 6, clock_h // 2.5))

# Get window size from clock image
width, height = clock_img.get_size()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Clock")
screen.fill((255, 255, 255))  # white background

# Center of the clock
center = (width // 2, height // 2)
center = pygame.math.Vector2(width // 2, height // 2)

# These control where the hand "attaches"
minute_offset = pygame.math.Vector2(0, 78)
second_offset = pygame.math.Vector2(0, 80)

# Rotation function
def rotate_around_pivot(image, angle, pivot, offset):
    rotated_image = pygame.transform.rotozoom(image, -angle, 1)
    rotated_offset = offset.rotate(angle)
    rect = rotated_image.get_rect(center=(pivot[0] - rotated_offset.x, pivot[1] - rotated_offset.y))
    return rotated_image, rect

# Clock to control updates
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current system time
    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    # Calculate angles
    # 360 degrees / 60 units = 6 degrees per unit
    minute_angle = minutes * 6
    second_angle = seconds * 6

    # Rotate hands
    rotated_minute, minute_rect = rotate_around_pivot(minute_hand_img, minute_angle, center, minute_offset)
    rotated_second, second_rect = rotate_around_pivot(second_hand_img, second_angle, center, second_offset)

    # Draw everything
    screen.blit(clock_img, (0, 0))
    screen.blit(rotated_minute, minute_rect)
    screen.blit(rotated_second, second_rect)

    pygame.display.flip()

    # Update every second (real-time sync)
    pygame.time.wait(1000)

pygame.quit()
sys.exit()
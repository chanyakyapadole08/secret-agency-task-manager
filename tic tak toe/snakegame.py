import pygame
import random

# ---------- Initialize ----------
pygame.init()

# Screen settings
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Joyful Snake Game")

# Colors
BLACK = (20, 20, 20)
GREEN = (0, 255, 100)
YELLOW = (255, 220, 0)
RED = (255, 80, 80)
WHITE = (255, 255, 255)

# Snake settings
BLOCK = 20
SPEED = 12

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("arial", 28)
score_font = pygame.font.SysFont("arial", 24)


# ---------- Functions ----------
def show_score(score):
    value = score_font.render("Score: " + str(score), True, YELLOW)
    screen.blit(value, [10, 10])


def draw_snake(block, snake_list):
    for i, x in enumerate(snake_list):
        # head different color
        if i == len(snake_list) - 1:
            pygame.draw.rect(screen, WHITE, [x[0], x[1], block, block])
        else:
            pygame.draw.rect(screen, GREEN, [x[0], x[1], block, block])


def message(msg, color):
    text = font_style.render(msg, True, color)
    screen.blit(text, [WIDTH / 8, HEIGHT / 3])


# ---------- Game Loop ----------
def game_loop():

    game_over = False
    game_close = False

    x = WIDTH // 2
    y = HEIGHT // 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK) / BLOCK) * BLOCK
    food_y = round(random.randrange(0, HEIGHT - BLOCK) / BLOCK) * BLOCK

    while not game_over:

        # ---------- Game Over Screen ----------
        while game_close:
            screen.fill(BLACK)
            message("Game Over! Press C-Play Again or Q-Quit", RED)
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        return game_loop()

        # ---------- Controls ----------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK
                    x_change = 0

        # ---------- Wall collision ----------
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change

        # ---------- Draw background ----------
        screen.fill(BLACK)

        # Draw food (circle)
        pygame.draw.circle(
            screen,
            RED,
            (int(food_x + BLOCK / 2), int(food_y + BLOCK / 2)),
            BLOCK // 2,
        )

        # ---------- Snake logic ----------
        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Self collision
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(BLOCK, snake_list)
        show_score(snake_length - 1)

        pygame.display.update()

        # ---------- Food collision (FIXED) ----------
        if abs(x - food_x) < BLOCK and abs(y - food_y) < BLOCK:
            food_x = round(random.randrange(0, WIDTH - BLOCK) / BLOCK) * BLOCK
            food_y = round(random.randrange(0, HEIGHT - BLOCK) / BLOCK) * BLOCK
            snake_length += 1

        clock.tick(SPEED)

    pygame.quit()
    quit()


# ---------- Start Game ----------
game_loop()


# https://www.youtube.com/watch?v=Qf3-aDXG8q4

import pygame
import sys
import random

# 1. Setup
# 1.1. Game logic
# 1.2. Data

# 2. Loop
# 2.1. Drawing
# 2.2. Updating

pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

ball_speed_x, ball_speed_y = 9 * random.choice((1, -1)), 9 * random.choice((1, -1))
player_speed = 0
opponent_speed = 9


def ball_animation():
    global ball_speed_y, ball_speed_x

    ball.x += ball_speed_x  # defining the rectangle's (ball) x position
    ball.y += ball_speed_y  # y position incremented by 7 every frame (60x / second)

    # reverse speed for each axis if on corner
    # vertical or y axis
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    # horizontal or x axis
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    # collision logic
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def player_animation():
    # movement
    player.y += player_speed

    # collision
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_animation():
    # movement
    if opponent.top < ball.y:
        opponent.top += opponent_speed * 2
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed * 2

    # collision
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_restart():
    global ball_speed_y, ball_speed_x

    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))


while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_DOWN:
                player_speed -= 7

    # animations & movements
    ball_animation()
    player_animation()
    opponent_animation()

    # Visuals
    screen.fill(bg_color)  # background color
    pygame.draw.rect(screen, light_grey, player)  # (surface, color, rectangle to be drawn on surface)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)  # magic => elipse becomes a circle (our ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    # Updating the window
    pygame.display.flip()  # draws the screen
    clock.tick(60)  # limits how fast the loop runs to 60 frames (times) per second





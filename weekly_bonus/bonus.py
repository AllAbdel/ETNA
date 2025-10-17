import pygame, random, sys

pygame.init()
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
paddle = pygame.Rect(w//2 - 60, h - 30, 120, 15)
ball = pygame.Rect(w//2 - 10, h//2 - 10, 20, 20)
ball_speed = [10, -3]
blocks = [pygame.Rect(10 + 80*x, 50 + 30*y, 70, 20) for y in range(5) for x in range(10)]
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= 8
    if keys[pygame.K_RIGHT] and paddle.right < w:
        paddle.x += 8
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]
    if ball.left <= 0 or ball.right >= w:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.colliderect(paddle):
        ball_speed[1] = -abs(ball_speed[1])
    hit_index = ball.collidelist(blocks)
    if hit_index != -1:
        hit_block = blocks.pop(hit_index)
        if abs(ball.bottom - hit_block.top) < 10 and ball_speed[1] > 0:
            ball_speed[1] = -ball_speed[1]
        elif abs(ball.top - hit_block.bottom) < 10 and ball_speed[1] < 0:
            ball_speed[1] = -ball_speed[1]
        else:
            ball_speed[0] = -ball_speed[0]
    if ball.bottom >= h:
        run = False
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.draw.ellipse(screen, (255, 0, 0), ball)
    for b in blocks:
        pygame.draw.rect(screen, (0, 150, 255), b)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

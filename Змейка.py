import pygame
from random import randint
 
FPS = 3
W = 800
H = 600

BLACK = 0, 0, 0
RED = 255, 0, 0

RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"
STOP = "stop"

snake_length = 3

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption(f"Snake")
clock = pygame.time.Clock()
 
xu = 40
yu = 40
x = (W // xu // 2) * (xu)
y = (H // yu // 2) * (yu)

element_shift = (xu + yu) // 2 // 15
elements = [[x, y]]
apple = [randint(0, W // (xu) - 1) * xu, randint(0, H // yu - 1) * yu]

motion = STOP
won = False
dead = False
 
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT and motion != RIGHT:
                motion = LEFT
                break
            elif i.key == pygame.K_RIGHT and motion != LEFT:
                motion = RIGHT
                break
            elif i.key == pygame.K_UP and motion != DOWN:
                motion = UP
                break
            elif i.key == pygame.K_DOWN and motion != UP:
                motion = DOWN
                break

    if dead:
        pygame.display.set_caption(f"You dead! Score: {snake_length - 3}")
    elif won:
        pygame.display.set_caption(f"You won! Score: {snake_length - 3}")
    else:
        if motion == LEFT:
            x -= xu
        elif motion == RIGHT:
            x += xu
        elif motion == UP:
            y -= yu
        elif motion == DOWN:
            y += yu

        if motion != STOP:
            elements.append([x, y])
        if len(elements) > snake_length:
            elements = elements[1:]
            
        if [x, y] in elements[:-1] or x >= W or x < 0 or y >= H or y < 0:
            dead = True

        if apple == [x, y]:
            if snake_length == (W // xu) * (H // yu):
                won = True
            else:
                while apple in elements:
                    apple = [randint(0, W // (xu) - 1) * xu, randint(0, H // yu - 1) * yu]
                snake_length += 1
                pygame.display.set_caption(f"Score: {snake_length - 3}")

        sc.fill(BLACK)
        pygame.draw.rect(sc, RED, (apple[0] + xu // 4, apple[1] + yu // 4, xu // 2, yu // 2))
        for i in range(len(elements)):
            x_start = elements[i][0] + element_shift
            y_start = elements[i][1] + element_shift
            x_shift = xu - element_shift * 2
            y_shift = yu - element_shift * 2

            if i:
                if elements[i][0] - xu == elements[i-1][0]:
                    x_start -= element_shift * 2
                    x_shift += element_shift * 2
                elif elements[i][0] + xu == elements[i-1][0]:
                    x_shift += element_shift * 2
                elif elements[i][1] - yu == elements[i-1][1]:
                    y_start -= element_shift * 2
                    y_shift += element_shift * 2
                elif elements[i][1] + yu == elements[i-1][1]:
                    y_shift += element_shift * 2

            pgmnt = 255 - (len(elements) - i - 1)
            pgmnt = pgmnt if pgmnt >= 150 else 150

            pygame.draw.rect(sc, (0, pgmnt, 0), (x_start, y_start, x_shift, y_shift))
        pygame.display.update()
 
    clock.tick(FPS)

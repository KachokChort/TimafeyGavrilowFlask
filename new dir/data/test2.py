import pygame

size = width, height = 400, 300
screen = pygame.display.set_mode(size)
screen2 = pygame.Surface((100, 100))
FPS = 60
clock = pygame.time.Clock()

# создаем дополнительную поверхность с зеленым квадратом
screen.fill(pygame.Color('black'))
pygame.draw.rect(screen2, (0, 255, 0), ((0, 0), (100, 100)))
r = screen.blit(screen2, (0, 0))
x, y = 0, 0
x_top_square, y_top_square = 0, 0  # координаты верхнего левого угла квадрата (доп. поверхности)
running = True
dragging = False
bool = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_click, y_click = event.pos
            if x_click >= x_top_square and y_click >= y_top_square  and x_click <= x_top_square + 100 and y_click <= y_top_square + 100:
                dragging = True
                x = x_click - x_top_square
                y = y_click - y_top_square
        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            x, y = 0, 0
        if event.type == pygame.MOUSEMOTION:
            if x > 0:
                x_click, y_click = event.pos
                x_top_square = x_click - x
                y_top_square = y_click - y

    if dragging:
        # стираем все что было и рисуем новую screen2
        screen.fill(pygame.Color('black'))


        #print(x, y)
        r = screen.blit(screen2, (x_top_square, y_top_square))
        # print(r)

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
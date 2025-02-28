import pygame


pygame.init()

try:
    a, n = [int(i) for i in input().split()]
    b = a * n * 2
    print(b)
    screen = pygame.display.set_mode((b, b))
    pygame.display.set_caption('first')

    def draw(x, y, color, r):
        pygame.draw.ellipse(screen, color, (x, y, r, r), a)

    def draw1():
        for i in range(n):
            if i % 3 == 0:
                draw(i * a, i * a, 'red', b - (i * a * 2))
            elif i % 3 == 1:
                draw(i * a, i * a, 'green', b - (i * a * 2))
            elif i % 3 == 2:
                draw(i * a, i * a, 'blue', b - (i * a * 2))


    draw1()
    running = True
    while running:



        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

except Exception:
    print('Неправильный формат ввода')
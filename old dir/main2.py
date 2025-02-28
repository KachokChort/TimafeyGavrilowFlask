import pygame


pygame.init()

try:
    a, n = [int(i) for i in input().split()]
    b = a // n
    print(b)
    screen = pygame.display.set_mode((a, a))
    pygame.display.set_caption('first')

    def draw(x, y, color):
        pygame.draw.rect(screen, color, (x, y, b, b))

    def draw1():
        if n % 2 == 0:
            for x in range(n):
                for y in range(n):
                    #print(x)
                    if x % 2 == 0:
                        if y % 2 == 0:
                            draw(x * b, y * b, 'white')
                    else:
                        if y % 2 != 0:
                            draw(x * b, y * b, 'white')
        else:
            for x in range(n):
                for y in range(n):
                    # print(x)
                    if x % 2 != 0:
                        if y % 2 == 0:
                            draw(x * b, y * b, 'white')
                    else:
                        if y % 2 != 0:
                            draw(x * b, y * b, 'white')

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
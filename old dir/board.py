import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                if self.board[j][i] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), ((self.left + i * self.cell_size, self.top + j * self.cell_size), (self.cell_size, self.cell_size)), 1)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (
                    (self.left + i * self.cell_size, self.top + j * self.cell_size), (self.cell_size, self.cell_size)),)

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if 0 <= cell_x < self.width and 0 <= cell_y < self.height:
            return (cell_x, cell_y)

    def on_click(self, cell_pos, screen):
        print(cell_pos)
        for i in range(self.width):
            if i != cell_pos[0]:
                if self.board[cell_pos[1]][i] == 0:
                    self.board[cell_pos[1]][i] = 1
                else:
                    self.board[cell_pos[1]][i] = 0
        for j in range(self.height):
            if self.board[j][cell_pos[0]] == 0:
                self.board[j][cell_pos[0]] = 1
            else:
                self.board[j][cell_pos[0]] = 0
        self.render(screen)



    def get_click(self, mouse_pos, screen):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell, screen)


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    board = Board(10, 10)
    board.set_view(0, 0, 50)
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos, screen)
        screen.fill((0, 0, 0))
        board.render(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main()
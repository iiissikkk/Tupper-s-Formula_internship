from functools import reduce
import pygame
import math
import numpy as np
import tupper
import tupper.constants
import sys

WIDTH = 725
LENGTH = 100
WIN = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("Tupper's self-referential formula")

k = 4858450636189713423582095962494202044581400587983244549483093085061934704708809928450644769865524364849997247024915119110411605739177407856919754326571855442057210445735883681829823754139634338225199452191651284348332905131193199953502413758765239264874613394906870130562295813219481113685339535565290850023875092856892694555974281546386510730049106723058933586052544096664351265349363643957125565695936815184334857605266940161251266951421550539554519153785457525756590740540157929001765967965480064427829131488548259914721248506352686630476300

GREY = (190, 190, 190)
BLACK= (0, 0, 0)
WHITE = (255, 255, 255)

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.colour = WHITE
        self.width = width
        self.total_rows = total_rows

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))

    def __lt__(self, other):
        return False

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid

def make_point(self):
    self.colour = BLACK
def not_point(self):
    self.colour = WHITE

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()

def tuppers_formula(x, y):
    #return(((y // 17) // (1 << (17 * x + (y % 17)))) % 2)
    return ((k + y)//17//2**(17*int(x) + int(y)%17))%2 > 0.5

def draw_formula():
    H = 17
    W = 106
    gap = 800 // 106

    win = WIN

    yCoord = 0
    xCoord = 0

    for y in range(k + H - 1, k - 1, -1):
        xCoord = 0
        for x in range(W):
            if tuppers_formula(x, y):
                #закрашивать
                sys.stdout.write('*')
                #pygame.draw.line(win, BLACK, (0, x * gap), (106, x * gap))
                #pygame.draw.line(win, BLACK, (y * gap, 0), (y * gap, 106))
                #pygame.draw.line(win, BLACK, xCoord, yCoord)
                pygame.draw.rect(win, BLACK, (xCoord, yCoord, xCoord + gap, yCoord + gap))
            else:
                sys.stdout.write(' ')
                pygame.draw.rect(win, WHITE, (xCoord, yCoord, xCoord + gap, yCoord + gap))
            xCoord += gap
        sys.stdout.write('\n')
        yCoord += gap
    #----------------------------------------------------
    pygame.display.update()

def main(win, width):
    ROWS = 106
    grid = make_grid(ROWS, width)
    run = True
    started = False
    draw(win, grid, ROWS, width)
    while run:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False
            if started:
                continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    draw_formula()
    pygame.quit()

main(WIN, WIDTH)
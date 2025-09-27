import pygame
import sys

pygame.init()

LARGURA = 1024
ALTURA = 768
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
GROSSURA = 5


def draw_thick_point(surface, color, pos, radius):
    pygame.draw.circle(surface, color, pos, radius)


def draw_line_bresenham(surface, color, start_pos, end_pos, thickness):
    x0, y0 = start_pos
    x1, y1 = end_pos

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1

    err = dx - dy

    x, y = x0, y0

    while True:
        if 0 <= x < surface.get_width() and 0 <= y < surface.get_height():
            pygame.draw.circle(surface, color, (x, y), thickness // 2)

        if x == x1 and y == y1:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x += sx

        if e2 < dx:
            err += dx
            y += sy


tela = pygame.display.set_mode((LARGURA, ALTURA))
tela.fill(PRETO)

clock = pygame.time.Clock()
esperando_primeiro_clique = True
start_pos = None

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                pos_mouse = pygame.mouse.get_pos()

                if esperando_primeiro_clique:
                    start_pos = pos_mouse
                    esperando_primeiro_clique = False
                    draw_thick_point(tela, VERMELHO, start_pos, GROSSURA)

                else:
                    end_pos = pos_mouse
                    draw_line_bresenham(
                        tela, BRANCO, start_pos, end_pos, GROSSURA)
                    draw_thick_point(tela, VERMELHO, end_pos, GROSSURA)
                    esperando_primeiro_clique = True
                    start_pos = None

    pygame.display.flip()
    clock.tick(60)

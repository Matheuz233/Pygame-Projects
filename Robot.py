import pygame
import sys

pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Definição de cores (modelo RGB)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (100, 149, 237)
AZUL_ESCURO = (70, 130, 180)
VERMELHO = (220, 20, 60)
VERDE = (50, 205, 50)
AMARELO = (255, 215, 0)
CINZA = (169, 169, 169)
CINZA_ESCURO = (105, 105, 105)
LARANJA = (255, 140, 0)

def desenhar_robo():
    corpo_rect = pygame.Rect(300, 250, 200, 180)
    pygame.draw.rect(tela, AZUL, corpo_rect)
    pygame.draw.rect(tela, AZUL_ESCURO, corpo_rect, 3)
    
    cabeca_centro = (400, 200)
    pygame.draw.circle(tela, CINZA, cabeca_centro, 70)
    pygame.draw.circle(tela, CINZA_ESCURO, cabeca_centro, 70, 3)
    
    olho_esq = (375, 185)
    olho_dir = (425, 185)
    pygame.draw.circle(tela, VERDE, olho_esq, 15)
    pygame.draw.circle(tela, VERDE, olho_dir, 15)
    pygame.draw.circle(tela, PRETO, olho_esq, 8)
    pygame.draw.circle(tela, PRETO, olho_dir, 8)
    
    boca_rect = pygame.Rect(385, 210, 30, 8)
    pygame.draw.rect(tela, VERMELHO, boca_rect)
    
    braco_esq = pygame.Rect(220, 280, 80, 30)
    braco_dir = pygame.Rect(500, 280, 80, 30)
    pygame.draw.rect(tela, CINZA, braco_esq)
    pygame.draw.rect(tela, CINZA, braco_dir)
    pygame.draw.rect(tela, CINZA_ESCURO, braco_esq, 2)
    pygame.draw.rect(tela, CINZA_ESCURO, braco_dir, 2)
    
    mao_esq = (240, 295)
    mao_dir = (560, 295)
    pygame.draw.circle(tela, LARANJA, mao_esq, 20)
    pygame.draw.circle(tela, LARANJA, mao_dir, 20)
    pygame.draw.circle(tela, CINZA_ESCURO, mao_esq, 20, 2)
    pygame.draw.circle(tela, CINZA_ESCURO, mao_dir, 20, 2)
    
    perna_esq = pygame.Rect(330, 430, 40, 100)
    perna_dir = pygame.Rect(430, 430, 40, 100)
    pygame.draw.rect(tela, AZUL_ESCURO, perna_esq)
    pygame.draw.rect(tela, AZUL_ESCURO, perna_dir)
    
    pe_esq = pygame.Rect(310, 520, 80, 30)
    pe_dir = pygame.Rect(410, 520, 80, 30)
    pygame.draw.ellipse(tela, LARANJA, pe_esq)
    pygame.draw.ellipse(tela, LARANJA, pe_dir)
    
    pontos_painel = [(375, 300), (425, 300), (420, 340), (380, 340)]
    pygame.draw.polygon(tela, AMARELO, pontos_painel)
    pygame.draw.polygon(tela, LARANJA, pontos_painel, 2)
    
    pygame.draw.circle(tela, VERMELHO, (390, 315), 6)
    pygame.draw.circle(tela, VERDE, (410, 315), 6)
    pygame.draw.circle(tela, AZUL, (400, 330), 6)
    
    pygame.draw.line(tela, AZUL_ESCURO, (310, 270), (490, 270), 2)
    pygame.draw.line(tela, AZUL_ESCURO, (310, 360), (490, 360), 2)
    pygame.draw.line(tela, AZUL_ESCURO, (310, 400), (490, 400), 2)
    
    pygame.draw.circle(tela, CINZA_ESCURO, (300, 295), 8)
    pygame.draw.circle(tela, CINZA_ESCURO, (500, 295), 8)

def desenhar_fundo():
    chao = pygame.Rect(0, 550, LARGURA, 50)
    pygame.draw.rect(tela, BRANCO, chao)

clock = pygame.time.Clock()

while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  
    
    tela.fill(BRANCO)
    
    desenhar_fundo()
    desenhar_robo()
    
    pygame.display.flip()
    clock.tick(60)

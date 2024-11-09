import pygame
from random import randint

pygame.init()
relogio = pygame.time.Clock()

tamanho = (1280, 720)
tela = pygame.display.set_mode(tamanho)

pygame.display.set_caption("Rapid Fire")
dt = 0

def criaAlvo():
    posX = randint(5,1275)
    posY = randint(-20, -5)

    novoAlvo = {
        "sprites" : frameWalk,
        "velocidade" : randint(20, 100),
        "posicao" : pygame.Vector2(posX, posY),
        "direcao" : pygame.Vector2(-1, 1)
    }

    return novoAlvo

def desenhaAlvo(listaAlvo):
    for alvo in listaAlvo:
        tela.blit(alvo["sprites"][0], alvo["posicao"])

def animaAlvo(listaAlvo):
    for alvo in listaAlvo:
        alvo["posicao"].y += alvo["velocidade"] * alvo["direcao"].y * dt
        alvo["posicao"].x += alvo["velocidade"] * alvo["direcao"].x * dt
        
folhaSpritesWalk = pygame.image.load("assets/2/D_Walk.png").convert_alpha()
folhaSpritesDeath = pygame.image.load("assets/2/D_Death.png").convert_alpha()

frameWalk = []
frameDeath = []

for i in range(6):
    frame = folhaSpritesWalk.subsurface(i * 48, 0 , 48, 48)
    frame = pygame.transform.scale(frame, (256, 256))
    frameWalk.append(frame)

for i in range(6):
    frame = folhaSpritesDeath.subsurface(i * 48, 0 , 48, 48)
    frame = pygame.transform.scale(frame, (256, 256))
    frameDeath.append(frame)

indexFrameWalk = 0
tempoAnimacaoWalk = 0.0
velocidadeAnimacaoWalk = 10

indexFrameDeath = 0
tempoAnimacaoDeath = 0.0
velocidadeAnimacaoDeath = 8

alvoRect = frameWalk[0].get_rect(midbottom=(120, 490))
alvoRect = frameDeath[0].get_rect(midbottom=(120, 490))

velocidadeAlvo = 100

tempoJogo = 0
tempoJogo += dt

listAlvo = []
AUMENTA_DIFICULDADE = pygame.USEREVENT +1
pygame.time.set_timer(AUMENTA_DIFICULDADE, 10000)
tempoSurgimentoAlvo = 3000

ADICIONA_ALVO = pygame.USEREVENT + 2
pygame.time.set_timer(ADICIONA_ALVO, tempoSurgimentoAlvo)

system = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_NO)
bitmap_1 = pygame.cursors.Cursor(*pygame.cursors.arrow)
bitmap_2 = pygame.cursors.Cursor((24, 24), (0, 0), *pygame.cursors.compile(pygame.cursors.thickarrow_strings))
surf = pygame.Surface((40, 40))
surf.fill((120, 50, 50))
color = pygame.cursors.Cursor((20, 20), surf)
cursors = [system, bitmap_1, bitmap_2, color]
cursor_index = 0
pygame.mouse.set_cursor(cursors[cursor_index])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == AUMENTA_DIFICULDADE:
            velocidadeAlvo += 4

            if tempoSurgimentoAlvo > 1100:
                tempoSurgimentoAlvo -= 300
        
        if event.type == ADICIONA_ALVO:
            listAlvo.append(criaAlvo())

    tempoAnimacaoWalk += dt

    if tempoAnimacaoWalk >= 1 / velocidadeAnimacaoWalk:
        indexFrameWalk = (indexFrameWalk +1) % len(frameWalk)
        tempoAnimacaoWalk = 0.0


    
    tela.fill((255, 255, 255))

    desenhaAlvo(listAlvo)
    animaAlvo(listAlvo)

    pygame.display.update()
    dt = relogio.tick(60) / 1000    
    
            
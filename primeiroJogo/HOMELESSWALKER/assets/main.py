import pygame

pygame.init()
relogio = pygame.time.Clock()

tamanho = (1200, 500)
tela = pygame.display.set_mode(tamanho)

pygame.display.set_caption("Homeless Creed")
dt = 0

#Carrega  a spritesheet para nosso projeto
folhaSpritesIdle = pygame.image.load("assets/Homeless_3/Idle_2.png").convert_alpha()
folhaSpritesWalk = pygame.image.load("assets/Homeless_3/Walk.png").convert_alpha()

#Define os frames
framesIdle = []
frameWalk = []
for i in range(11):
    frame = folhaSpritesIdle.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (230, 230))
    framesIdle.append(frame)

for i1 in range(8):
    frames = folhaSpritesWalk.subsurface(i1 * 128, 0, 128, 128)
    frames = pygame.transform.scale(frames, (230, 230))
    frameWalk.append(frames)

#variaveis da animação do personagem parado
indexFrameIdle = 0
tempoAnimacaoIdle = 0.0
velocidadeAnimacaoIdle = 5

indexFrameWalk = 0
tempoAnimacaoWalk = 0.0
velocidadeAnimacaoWalk = 10

#retangulo do personagem

personagemRect = framesIdle[0].get_rect(midbottom=(120, 490))
personagemRect = frameWalk[0].get_rect(midbottom=(120, 490))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    tela.fill((255, 255, 255))

    #Atualiza a animação do personagem parado
    tempoAnimacaoIdle += dt
    tempoAnimacaoWalk += dt

    estaAndando = False

    if tempoAnimacaoIdle >= 1 / velocidadeAnimacaoIdle:
        indexFrameIdle = (indexFrameIdle +1) % len(framesIdle)
        tempoAnimacaoIdle = 0.0

    if tempoAnimacaoWalk >= 1 / velocidadeAnimacaoWalk:
        indexFrameWalk = (indexFrameWalk +1) % len(frameWalk)
        tempoAnimacaoWalk = 0.0

    #Movimenta o personagem
    teclas = pygame.key.get_pressed()


    if teclas[pygame.K_a]:
        virar = pygame.transform.flip(folhaSpritesWalk(True))
        personagemRect.x -= 200 * dt
        estaAndando = True
    if teclas[pygame.K_d]:
        personagemRect.x += 200 * dt
        estaAndando = True

    if estaAndando:
        tela.blit(frameWalk[indexFrameWalk], personagemRect)
    else:
        tela.blit(framesIdle[indexFrameIdle], personagemRect)
    #Desenha o personagem
    
    

    #desenha um retangulo em volta do personagem
    pygame.draw.rect(tela, (0, 0, 0), personagemRect, 2)

    pygame.display.update()
    dt = relogio.tick(60) / 800
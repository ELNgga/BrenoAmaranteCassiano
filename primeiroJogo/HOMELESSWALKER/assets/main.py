import pygame

pygame.init()
relogio = pygame.time.Clock()

tamanho = (1280, 720)
tela = pygame.display.set_mode(tamanho)

pygame.display.set_caption("Homeless Creed")
dt = 0

#Carrega  a spritesheet para nosso projeto
folhaSpritesIdle = pygame.image.load("assets/Homeless_3/Idle_2.png").convert_alpha()
folhaSpritesWalk = pygame.image.load("assets/Homeless_3/Walk.png").convert_alpha()
folhaSpritesJump = pygame.image.load("assets/Homeless_3/Jump.png").convert_alpha()
folhaSpritesRun = pygame.image.load("assets/Homeless_3/Run.png").convert_alpha()
folhaSpritesAttack = pygame.image.load("assets/Homeless_3/Attack_2.png").convert_alpha()
#Define os frames
framesIdle = []
frameWalk = []
frameJump = []
frameRun = []
frameAttack = []

for i in range(11):
    frame = folhaSpritesIdle.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (230, 230))
    framesIdle.append(frame)

for i1 in range(8):
    frames = folhaSpritesWalk.subsurface(i1 * 128, 0, 128, 128)
    frames = pygame.transform.scale(frames, (230, 230))
    frameWalk.append(frames)

for i2 in range(9):
    frames = folhaSpritesJump.subsurface(i2 * 128, 0, 128, 128)
    frames = pygame.transform.scale(frames, (230, 230))
    frameJump.append(frames)

for i3 in range(8):
    frames = folhaSpritesRun.subsurface(i3 * 128, 0, 128, 128)
    frames = pygame.transform.scale(frames, (230, 230))
    frameRun.append(frames)

for i4 in range(3):
    frames = folhaSpritesAttack.subsurface(i4 * 128, 0, 128, 128)
    frames = pygame.transform.scale(frames, (230, 230))
    frameAttack.append(frames)

#variaveis da animação do personagem parado
indexFrameIdle = 0
tempoAnimacaoIdle = 0.0
velocidadeAnimacaoIdle = 5

indexFrameWalk = 0
tempoAnimacaoWalk = 0.0
velocidadeAnimacaoWalk = 5

indexFrameJump = 0
tempoAnimacaoJump = 0.0
velocidadeAnimacaoJump = 10

indexFrameRun = 0
tempoAnimacaoRun = 0.0
velocidadeAnimacaoRun = 10

indexFrameAttack = 0
tempoAnimacaoAttack = 0.0
velocidadeAnimacaoAttack = 5
estaAndando = False
estaCorrendo = False

#
listBgImages = [
    pygame.image.load("assets/Apocalipse/Postapocalypce3/Pale/sky.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Postapocalypce3/Pale/moon.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Postapocalypce3/Pale/sand_back.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Postapocalypce3/Pale/sand&objects3.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Postapocalypce3/Pale/sand&objects2.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Postapocalypce3/Pale/sand&objects1.png").convert_alpha(),
    pygame.image.load("assets/Apocalipse/Postapocalypce3/Pale/sand.png").convert_alpha()
]
listBgVelocidade = [1, 3, 7, 9, 10, 15, 20]

listBgPosicoes = [0 for _ in range(len(listBgImages))]

for i in range(len(listBgImages)):
    listBgImages[i] = pygame.transform.scale(listBgImages[i], tamanho)

#retangulo do personagem

personagemRect = framesIdle[0].get_rect(midbottom=(120, 490))
personagemRect = frameWalk[0].get_rect(midbottom=(120, 490))
direcaoPersonagem = 1
gravidade = 1
chao = 600
correrPersonagem = 80
caminhaPersonagem = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    tela.fill((255, 255, 255))
    #Percorre todas as imagens do plano de fundo para movimentar
    for i in range(len(listBgImages)):
        if estaCorrendo:
            listBgPosicoes[i] -= listBgVelocidade[i] * correrPersonagem * dt * direcaoPersonagem
        if estaAndando:
            listBgPosicoes[i] -= listBgVelocidade[i] * caminhaPersonagem * dt * direcaoPersonagem

        #Verificar se a imagem saiu
        if listBgPosicoes[i] <= -tamanho[0]:
            listBgPosicoes[i] = 0

        if listBgPosicoes[i] >= tamanho[0]:
            listBgPosicoes[i] = 0

#Desenha o plano de fundo
    for i in range(len(listBgImages)):
        #Desenha a imagem de fundo que esta na tela
        tela.blit(listBgImages[i], (listBgPosicoes[i], 0))
        #Desenha a imagem do plano de fundo que esta fora da tela
        tela.blit(listBgImages[i], (listBgPosicoes[i] + tamanho[0], 0))

        tela.blit(listBgImages[i], (listBgPosicoes[i] + -tamanho[0], 0))

    #Atualiza a animação do personagem parado
        tempoAnimacaoIdle += dt
        tempoAnimacaoWalk += dt
        tempoAnimacaoJump += dt
        tempoAnimacaoRun += dt

    if tempoAnimacaoIdle >= 1 / velocidadeAnimacaoIdle:
        indexFrameIdle = (indexFrameIdle +1) % len(framesIdle)
        tempoAnimacaoIdle = 0.0

    if tempoAnimacaoWalk >= 1 / velocidadeAnimacaoWalk:
        indexFrameWalk = (indexFrameWalk +1) % len(frameWalk)
        tempoAnimacaoWalk = 0.0

    if tempoAnimacaoJump >= 1 / velocidadeAnimacaoJump:
        indexFrameJump = (indexFrameJump +1) % len(frameJump)
        tempoAnimacaoJump = 0.0

    if tempoAnimacaoRun >= 1 / velocidadeAnimacaoRun:
        indexFrameRun = (indexFrameRun +1) % len(frameRun)
        tempoAnimacaoRun = 0.0
    estaAndando = False
    estaCorrendo = False
    #Movimenta o personagem
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_a] and teclas[pygame.K_LSHIFT]:
        direcaoPersonagem = -1
        estaAndando = True
        estaCorrendo = False   
           
    if teclas[pygame.K_a]:
        direcaoPersonagem = -1
        estaCorrendo = True
        estaAndando = False

    if teclas[pygame.K_d]:
        estaCorrendo = True
        estaAndando = False
        direcaoPersonagem = 1

    if teclas[pygame.K_d] and teclas[pygame.K_LSHIFT]:
        direcaoPersonagem = 1
        estaAndando = True
        estaCorrendo = False

    if teclas[pygame.K_w]:
        if personagemRect.centery == chao:
            gravidade = -50
            indexFrameJump = 0

    gravidade += 3

    personagemRect.y += gravidade

    if personagemRect.centery >= chao:
        personagemRect.centery = chao

    if gravidade < 0:
        frame = frameJump[indexFrameJump]
    else:
        if estaAndando: # Verifica se o personagem está andando
            frame = frameWalk[indexFrameWalk]
        elif estaCorrendo:
            frame = frameRun[indexFrameRun]
        else: # Caso contrário, o personagem está parado
            frame = framesIdle[indexFrameIdle]

    if direcaoPersonagem == -1: # Verifica se o personagem está olhando para a esquerda e inverte a imagem
        frame = pygame.transform.flip(frame, True, False) # Inverte a imagem

    tela.blit(frame, personagemRect) # Desenha o personagem na tela
    

    #desenha um retangulo em volta do personagem
    #pygame.draw.rect(tela, (0, 0, 0), personagemRect, 2)

    pygame.display.update()
    dt = relogio.tick(60) / 10000
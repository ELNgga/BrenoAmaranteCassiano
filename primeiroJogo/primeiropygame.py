import pygame
#Inicializar o pygame
pygame.init()

tamanho = (900, 500)
#Cria uma tela com tamanho especificado
tela = pygame.display.set_mode(tamanho)

#Define o titulo da janela
pygame.display.set_caption("Hello games!")

#Define um relogio para controlar o FPS
relogio = pygame.time.Clock()

posicaoBola = pygame.Vector2(450,250)
dt = 0

direcaoY = 1
direcaoX = 1

while True:
    #Lida com os eventos da aplicação
    for evento in pygame.event.get():
        print(evento)
        if evento.type == pygame.QUIT:
            pygame.quit() #Fecha o jogo

    #Preenche a tela com uma cor
    tela.fill((40, 100, 200))

    #Desenha um circulo na tela
    pygame.draw.circle(tela, (10, 255, 200), posicaoBola, 50)

    posicaoBola.y += 150 * direcaoY * dt
    posicaoBola.x += 150 * direcaoX * dt

    if posicaoBola.y >=450 or posicaoBola.y <=50:
        direcaoY *= -1
    if posicaoBola.x >=850 or posicaoBola.x <=50:
        direcaoX *= -1
        
    pygame.display.update()

    dt = relogio.tick(60) / 1000 #Define a quantidade de FPS
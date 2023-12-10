import pygame
import random

# Configuración inicial de Pygame
pygame.init()

# Configuración de la ventana del juego
win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))

# Configuración del jugador
player_width = 50
player_height = 50
player_x = 50
player_y = win_height - player_height
player_vel = 10

# Configuración del cactus
cactus_width = 20
cactus_height = 50
cactus_x = win_width
cactus_y = win_height - cactus_height
cactus_vel = 5

# Configuración del salto
is_jumping = False
jump_count = 10

# Configuración del color de fondo
bg_color = (173, 216, 230)  # Color celeste pastel

# Configuración del contador de puntos
score = 0
font = pygame.font.Font(None, 36)

# Configuración de las montañas
mountain_color = (169, 169, 169)  # Color gris
mountain_height = 100

# Configuración de la pantalla de inicio
start_screen = True

# Bucle principal del juego
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(30)  # FPS

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if start_screen:
        # Pantalla de inicio
        if keys[pygame.K_SPACE]:
            start_screen = False
        continue

    # Movimiento del cactus
    cactus_x -= cactus_vel
    if cactus_x < -cactus_width:
        cactus_x = win_width
        cactus_y = win_height - cactus_height

    # Movimiento del jugador
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    # Detección de colisiones
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    cactus_rect = pygame.Rect(cactus_x, cactus_y, cactus_width, cactus_height)
    if player_rect.colliderect(cactus_rect):
        print("¡Has perdido!")
        game_over_text = font.render("Game Over. Points: " + str(score), 1, (255, 255, 255))
        win.blit(game_over_text, (win_width / 2 - game_over_text.get_width() / 2, win_height / 2 - game_over_text.get_height() / 2))
        pygame.display.update()
        pygame.time.wait(2000)
        run = False

    # Actualizar el contador de puntos
    if pygame.time.get_ticks() % 1000 < 30:  # Aumentar el contador de puntos cada segundo
        score += 1

    # Dibujar todo
    win.fill(bg_color)
    pygame.draw.polygon(win, mountain_color, [(0, win_height), (win_width / 2, win_height - mountain_height), (win_width, win_height)])  # Dibujar las montañas
    pygame.draw.rect(win, (0, 0, 0), (player_x, player_y, player_width, player_height))
    pygame.draw.rect(win, (0, 255, 0), (cactus_x, cactus_y, cactus_width, cactus_height))
    score_text = font.render("Puntos: " + str(score), 1, (255, 255, 255))
    win.blit(score_text, (win_width - 200, 50))
    pygame.display.update()

pygame.quit()

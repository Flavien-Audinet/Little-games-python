import pygame

# Initialiser Pygame
pygame.init()

# Définir la largeur et la hauteur de l'écran
screen_width = 800
screen_height = 600

# Créer l'écran de jeu
screen = pygame.display.set_mode((screen_width, screen_height))

# Définir les couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Définir la position de départ de la voiture
car_x = screen_width // 2
car_y = screen_height // 2

# Définir la vitesse de déplacement de la voiture
car_speed = 5

# Boucle principale du jeu
running = True
while running:
    # Récupérer les entrées de l'utilisateur (touches du clavier)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtenir les touches pressées
    keys = pygame.key.get_pressed()

    # Déplacer la voiture en fonction des touches pressées
    if keys[pygame.K_UP]:
        car_y -= car_speed
    if keys[pygame.K_DOWN]:
        car_y += car_speed
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    # Dessiner l'arrière-plan
    screen.fill(BLACK)

    # Dessiner la voiture
    pygame.draw.rect(screen, WHITE, (car_x, car_y, 50, 25))

    # Mettre à jour l'écran
    pygame.display.flip()

# Quitter Pygame
pygame.quit()

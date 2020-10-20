import pygame
W, H = 400, 400

pygame.init()
screen = pygame.display.set_mode((W, H))

image = pygame.image.load('imageJotaro.png')
print(image.get_width(), image.get_height())
# Изменение размера картинки
image = pygame.transform.scale(image, (image.get_width() // 2, image.get_height() // 2)
image_rect = image.get_rect(center=(W // 2, H // 2))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run False
    screen.blit(image, image_rect)
    pygame.display.update()

    pygame.quit()

import pygame
import random
import os
# Изменяемая переменная
num = random.randint(0, 100)
print(num)
# Константа
W = 480
H = 360
SILVER = (192, 192, 192)
BLACK = (0, 0, 0)
# Создание окна
pygame.init()
# Название окна
pygame.display.set_caption('Угадай число')
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((W, H))
# Добавление картинок в окно
path = os.path.dirname(os.path.abspath(__file__))
bg = pygame.image.load(os.path.join(path, 'Image/room.png'))
bg_rect = bg.get_rect(topleft=(0, 0))
cat = pygame.image.load(os.path.join(path, 'Image/cat.png'))
cat_rect = cat.get_rect(center=(70, 260))
dog = pygame.image.load(os.path.join(path, 'Image/dog.png'))
dog_rect = dog.get_rect(topleft=(300, 220))
owl = pygame.image.load(os.path.join(path, 'Image/owl.png'))
owl_rect = owl.get_rect(topleft=(180, 180))
dialog = pygame.image.load(os.path.join(path, 'Image/dialog.png'))
dialog_rect = dialog.get_rect()
dialog_cat_pos = (cat_rect.x, cat_rect.y - dialog_rect.h)
dialog_dog_pos = (dog_rect.x - dialog_rect.w // 2,  dog_rect.y - dialog_rect.h)
dialog_owl_pos = (owl_rect.x, owl_rect.y - dialog_rect.h)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False
    screen.blit(bg, bg_rect)
    screen.blit(cat, cat_rect)
    screen.blit(dog, dog_rect)
    screen.blit(owl, owl_rect)
    screen.blit(dialog, dialog_rect)
    pygame.display.update()

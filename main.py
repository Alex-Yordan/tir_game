import random
import pygame

pygame.init() ### Инициализация модуля Pygame

SCREEN_WIDTH = 800   ### Задаем размеры экрана
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")  ### Заголовок окна игры
icon = pygame.image.load("img/tirr.jpg")  ### Загружаем картинку из папки
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/252.png")  ### Загрузка картинки мишени
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)  ### Задаем рандомные координаты появления мишени.
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
 
    ### Задаем рандомный цвет экрана
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

running = True  ### Переменная для создания игрового цикла
while running:
    screen.fill(color)  ### Заливка экрана цветом
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: ### Определяет клик мыши по мишени
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()  ### Обновление экрана

pygame.quit() ### Закрытие модуля PyGame






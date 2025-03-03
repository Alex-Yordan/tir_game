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
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))




running = True  ### Переменная для создания игрового цикла
while running:
    pass








pygame.quit() ### Закрытие модуля PyGame






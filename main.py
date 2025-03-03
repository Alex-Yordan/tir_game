import pygame

pygame.init() ### Инициализация модуля Pygame

SCREEN_WIDTH = 800   ### Задаем размеры экрана
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")  ### Заголовок окна игры
icon = pygame.image.load("img/tirr.jpg")  ### Загружаем картинку из папки
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/252.png")
target_width = 80
target_height = 80



running = True  ### Переменная для создания игрового цикла
while running:
    pass








pygame.quit() ### Закрытие модуля PyGame






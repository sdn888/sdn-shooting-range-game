import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target4.png")
target_width = 80
target_height = 80

# Инициализация переменных
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
score = 0
font = pygame.font.Font(None, 36)
target_size_increase_duration = 0  # Время увеличения размера цели
target_size_increase_factor = 1.5  # Во сколько раз увеличить цель

running = True
while running:
        screen.fill(color)

        # Обновляем цвет фона
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Проверка на таймер увеличения размера цели
        if target_size_increase_duration > 0:
                target_width = int(target_width * target_size_increase_factor)
                target_height = int(target_height * target_size_increase_factor)
                target_size_increase_duration -= 1  # Уменьшить оставшееся время
        else:
                target_width = 80
                target_height = 80

        # Отображение счета
        score_text = font.render(f"Счет: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                                score += 1  # Увеличиваем счет
                                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                                target_size_increase_duration = 20  # Увеличиваем размер цели на 20 кадров

        screen.blit(target_img, (target_x, target_y))
        pygame.display.update()

pygame.quit()

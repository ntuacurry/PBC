import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)

WINDOW_W = 800
WINDOW_H = 600
gameDisplay = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
FPS = 10
BLOCK_SIZE = 50

font = pygame.font.SysFont(None, 40)
font_title = pygame.font.SysFont(None, 60)
target = pygame.image.load("target.png")
target = pygame.transform.scale(target, (BLOCK_SIZE, BLOCK_SIZE))


def draw_snake(snake_loc_list):
    head_x = snake_loc_list[-1][0]
    head_y = snake_loc_list[-1][1]
    pygame.draw.rect(gameDisplay, red, [head_x, head_y, BLOCK_SIZE, BLOCK_SIZE])
    for [body_x, body_y] in snake_loc_list[:-1]:
        pygame.draw.rect(gameDisplay, purple, [body_x, body_y, BLOCK_SIZE, BLOCK_SIZE])


def draw_target(target_x, target_y):
    gameDisplay.blit(target, [target_x, target_y])


def msg_to_screen(msg, color, x, y, isTitle=False):
    text = ""
    if isTitle:
        text = font_title.render(msg, True, color)
    else:
        text = font.render(msg, True, color)
    text_rect = text.get_rect(center=(x, y))
    gameDisplay.blit(text, text_rect)

# def generate_rand_target_loc():



def game_loop():
    # 遊戲初始化（每一輪都會重新初始）
    game_exit = False
    game_over = False

    head_x = WINDOW_W / 4
    head_y = WINDOW_H / 2
    head_x_change = 0
    head_y_change = 0

    snake_loc_list = []
    snake_len = 1

    score = 0

    #target_x, target_y = ...

    while not game_exit:
        # 遊戲結束（重新開始）畫面
        while game_over == True:
            gameDisplay.fill(red)
            
            pygame.display.update()

        # 遊戲進行畫面—
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            # 1. 按鍵偵測移動


        # head_x_change = BLOCK_SIZE  # 測試蛇是可以正確移動的，開始製作專案時請將本行刪除
        head_x += head_x_change
        head_y += head_y_change

        # 更新蛇各節點位置
        snake_loc_list.append((head_x, head_y))
        #your code...
        #print("snake_len:", snake_len, "\nsnake_loc_list:", snake_loc_list)
        

        # 偵測碰撞邊界遊戲結束
        

        # 吃到自己的身體遊戲結束
        

        # 吃到目標
        

        gameDisplay.fill(black)
        msg_to_screen(f"Score: {score}", white, 60, 20)
        draw_snake(snake_loc_list)
        # draw_target(target_x, target_y)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


game_loop()
#coding:utf-8

#######
# 游戏主程序
#######

import pygame
import settings
from ship import Ship
import game_functions as gf

def run_game():
    # 读取配置
    game_setting = settings.Settings()

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 设置窗体的宽高
    screen = pygame.display.set_mode((game_setting.screen_width,game_setting.screen_height))
    # 设置标题为游戏名称
    pygame.display.set_caption(game_setting.game_name)

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_event(ship)

        # 玩家飞船的位置移动
        ship.update()

        # 更新游戏界面
        gf.update_screen(game_setting,screen,ship)




if __name__ == '__main__':
    run_game()
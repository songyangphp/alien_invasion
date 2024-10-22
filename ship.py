#coding:utf-8

#######
# 玩家飞船类
#######

import pygame
import settings

class Ship():

    def __init__(self, screen):
        # 读取配置
        self.game_setting = settings.Settings()

        # 初始化飞船并设置其初始位置
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp') # 飞船图像
        self.rect = self.image.get_rect() # 玩家飞船的矩形对象
        self.screen_rect = screen.get_rect() # 屏幕的矩形对象

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - (self.game_setting.screen_height * 0.1)

        # 支持移动速度小数值
        self.center = float(self.rect.centerx)

        # 右移动标志
        self.move_right = False # false为静止 true为移动中

        # 左移动标志
        self.move_left = False  # false为静止 true为移动中


    def update(self):
        # 移动玩家飞船

        if self.move_right:
            self.center += self.game_setting.ship_speed_factor

        if self.move_left:
            self.center -= self.game_setting.ship_speed_factor

        self.rect.centerx = self.center


    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
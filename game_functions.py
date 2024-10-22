#coding:utf-8
import sys
import pygame

#######
# 逻辑方法封装
#######

def check_event(ship):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        # 如果是点击了关闭按钮
        if event.type == pygame.QUIT:
            # 关闭窗体程序
            sys.exit()

        # 监听键盘按下事件
        elif event.type == pygame.KEYDOWN:
            # 按下右箭头
            if event.key == pygame.K_RIGHT:
                ship.move_right = True
            # 按下左箭头
            elif event.key == pygame.K_LEFT:
                ship.move_left = True

        # 监听键盘松开事件
        elif event.type == pygame.KEYUP:
            # 松开右箭头
            if event.key == pygame.K_RIGHT:
                ship.move_right = False
            # 松开左箭头
            elif event.key == pygame.K_LEFT:
                ship.move_left = False


def update_screen(settings, screen, ship):
    # 每次循环时都重绘屏幕
    # 注入背景颜色
    screen.fill(settings.bg_color)

    # 显示玩家飞船
    ship.blitme()

    # 让最近的绘制屏幕课件
    pygame.display.flip()
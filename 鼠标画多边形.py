import pygame
from pygame.locals import *
import sys
width=980         #窗口宽
height = 600      #窗口高

WHITE=(255,255,255)  #颜色

BLUE=(0,0,255)

GREEN=(0,255,0)

RED=(255,0,0)

BLACK=(0,0,0)



background=GREEN


  #储存点的变量

def draw_triggle():
	running=True
	drawing = False
	points=[]
	pygame.init()    #初始化
	screen=pygame.display.set_mode((width,height))   #设置屏幕对象
	while running:
		for event in pygame.event.get():  #循环所有的事件

			if event.type==QUIT:
				running=False
			elif event.type==KEYDOWN:      #键盘按钮按下事件

				if event.key==K_ESCAPE:    #按esc键
					
					if len(points)>0:      
						points.pop()       #抛出列表中最后一个元素
			elif event.type==MOUSEBUTTONDOWN:     #鼠标按下事件
				print(event.pos)
				points.append(event.pos)
				drawing=True
			elif event.type==MOUSEBUTTONUP:       #鼠标松开事件
				drawing=False

			elif event.type==pygame.MOUSEMOTION and drawing:
				points[-1]=event.pos

		screen.fill(background)
		if len(points)>1:
			rect=pygame.draw.lines(screen,RED,True,points,5)
			pygame.draw.rect(screen,GREEN,rect,1)
		pygame.display.update()
	pygame.quit()


draw_triggle()
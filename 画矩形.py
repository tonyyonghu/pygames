import pygame
from pygame.locals import *

width=960
height=480
background=(127,127,127)
RED=(255,0,0)
GREEN=(150,255,150)
BLUE=(0,0,255)
pygame.init()

screen=pygame.display.set_mode((width,height))

running=True

while running:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
	screen.fill(background)

	pygame.draw.rect(screen,RED,(50,50,200,200)) #50 50代表起点坐标，200,200代表宽高
	pygame.draw.rect(screen,GREEN,(150,150,200,200))
	pygame.draw.rect(screen,BLUE,(250,250,200,200))

	pygame.draw.rect(screen,RED,(450,50,200,200),1) #50 50代表起点坐标，200,200代表宽高,1代表边框
	pygame.draw.rect(screen,GREEN,(550,150,200,200),5)
	pygame.draw.rect(screen,BLUE,(650,250,200,200),10)


	pygame.display.update()

pygame.quit()
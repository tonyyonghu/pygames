import pygame
from pygame.locals import *

width=980
height=480
RED=(255,0,0)
GREEN=(173,160,160)
BLUE=(0,0,255)
background=GREEN
pygame.init()

screen=pygame.display.set_mode((width,height))
running=True

while running:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
		if event.type==MOUSEBUTTONDOWN:
			print(event)
		if event.type==MOUSEBUTTONUP:
			print(event)

	screen.fill(background)
	pygame.draw.ellipse(screen,RED,(50,20,160,100))
	pygame.draw.ellipse(screen,BLUE,(100,110,160,100))
	pygame.draw.ellipse(screen,BLUE,(150,200,160,100))



	pygame.draw.ellipse(screen,RED,(450,20,160,100),1)
	pygame.draw.ellipse(screen,BLUE,(550,110,160,100),8)
	pygame.draw.ellipse(screen,BLUE,(650,200,160,100),15)
	pygame.display.update()
pygame.quit()
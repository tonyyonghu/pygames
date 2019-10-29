import pygame
from pygame.locals import *

width=980
height = 600

WHITE=(255,255,255)

BLUE=(0,0,255)

GREEN=(0,255,0)

RED=(255,0,0)

BLACK=(0,0,0)

pygame.init()

screen=pygame.display.set_mode((width,height))

background=GREEN

running=True
drawing = False
points=[]

while running:
	for event in pygame.event.get():

		if event.type==QUIT:
			running=False
		elif event.type==KEYDOWN:
			if event.key==K_ESCAPE:
				print(event.key)
				if len(points)>0:
					points.pop()
		elif event.type==MOUSEBUTTONDOWN:
			points.append(event.pos)
			drawing=True
		elif event.type==MOUSEBUTTONUP:
			drawing=False

		elif event.type==pygame.MOUSEMOTION and drawing:
			points[-1]=event.pos

	screen.fill(background)
	if len(points)>1:
		rect=pygame.draw.lines(screen,RED,True,points,5)
		pygame.draw.rect(screen,GREEN,rect,1)
	pygame.display.update()
pygame.quit()
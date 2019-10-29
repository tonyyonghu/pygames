import pygame

from pygame.locals import *

'''
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/tonyyonghu/pygames.git
git push -u origin master

'''

width=980
height=600

WHITE=(255,255,255)

BLUE=(0,0,255)

GREEN=(0,255,0)

RED=(255,0,0)

BLACK=(0,0,0)

pygame.init()

start=(0,0)

size=(0,0)

drawing=False

rect_list = []

screen=pygame.display.set_mode((width,height))

running=True
while running:
	for event in pygame.event.get():
		if event.type==QUIT:
			running=False

		elif event.type==MOUSEBUTTONDOWN:
			start = event.pos
			size=0,0
			drawing = True
		elif event.type == MOUSEBUTTONUP:
			end = event.pos
			size=end[0]-start[0],end[1]-start[1]
			rect=pygame.Rect(start,size)
			rect_list.append(rect)
			drawing=False
		elif event.type==MOUSEMOTION and drawing:
			end=event.pos
			size=end[0]-start[0],end[1]-start[1]

	screen.fill(WHITE)
	for rect in rect_list:
		pygame.draw.rect(screen,BLUE,rect,1)
	pygame.draw.rect(screen,RED,(start,size),3)
	pygame.display.update()
pygame.quit()
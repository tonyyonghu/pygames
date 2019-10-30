import pygame
from pygame.locals import *

import time

WIDTH=980
HEIGHT=600
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
pygame.init()

screen=pygame.display.set_mode((WIDTH,HEIGHT))

text = "this text is editable"

font=pygame.font.SysFont(None,50)
img=font.render(text,True,RED)

rect=img.get_rect()
rect.topleft=(20,20)

cursor=Rect(rect.topright,(3,rect.height))
background = GRAY
running=True

while running:
	for event in pygame.event.get():
		if event.type==QUIT:
			running=False
		elif event.type==KEYDOWN:
			if event.key==K_BACKSPACE:
				if len(text)>0:
					text=text[:-1]
					print(event.unicode)
			else:
				text +=event.unicode
		img=font.render(text,True,RED)
		rect.size=img.get_size()
		cursor.topleft=rect.topright
	screen.fill(background)
	screen.blit(img,rect)
	if time.time() % 1>0.5:
		pygame.draw.rect(screen,RED,cursor)
	pygame.display.update()
pygame.quit()			

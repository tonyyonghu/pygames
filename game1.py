import pygame

from pygame.locals import *

width=980
height=600
screen=pygame.display.set_mode((width,height)) #设置窗口大小
img=pygame.image.load('basketball.gif')

img.convert()
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GRAY=(127,127,127)
rect = img.get_rect()
print(rect)
rect.center=width//2,height//2

print(rect.center)
pygame.init() #初始化

running=True

moving=False

while running:
	#循环事件
	for event in pygame.event.get():
		if event.type==QUIT:
			running=False
		elif event.type==MOUSEBUTTONDOWN:
			print(rect.collidepoint(event.pos))

			if rect.collidepoint(event.pos):
				moving=True
		elif event.type==MOUSEBUTTONUP:
			moving=False
		elif event.type==MOUSEMOTION and moving:
			print(event.rel)
			rect.move_ip(event.rel)
	screen.fill(GRAY)
	screen.blit(img,rect)
	pygame.draw.rect(screen,RED,rect,1)

	pygame.display.update()

pygame.quit()
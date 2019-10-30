import pygame
import math
from pygame.locals import *

width=980
height=600
screen=pygame.display.set_mode((width,height)) #设置窗口大小
original=pygame.image.load('basketball.gif')

original.convert()


WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)

GREEN = (0, 255, 0)
GRAY = (150, 150, 150)
rect0 = original.get_rect()

pygame.draw.rect(original,GREEN,rect0,1)

img=original
center=width//2,height//2

mouse=center
rect=img.get_rect()
rect.center=center

print(rect0.center)

print(rect0)
print(rect)

pygame.init() #初始化

running=True

moving=False

angle=0
scale=1

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
		
		elif event.type==KEYDOWN:
			caption="background color =" + str(WHITE)
			pygame.display.set_caption(caption)

			if event.key ==K_r:
				# print(event)
				# print(KMOD_SHIFT)
				if event.mod & KMOD_SHIFT:
					angle-=10
				else:
					angle+=10
				# img=pygame.transform.rot
				img=pygame.transform.rotozoom(original,angle,scale)
			elif event.key==K_s:
				# print(event)
				if event.mod & KMOD_SHIFT:
					scale /=1.1
				else:
					scale*=1.1
				img=pygame.transform.rotozoom(original,angle,scale)
			elif event.key ==K_o:
				img=original
				angle=0
				scale=1
			elif event.key==K_h:
				img = pygame.transform.flip(img,True,False)
			elif event.key==K_v:
				img = pygame.transform.flip(img,False,True)
			elif event.key==K_1:
				img=pygame.transform.laplacian(img)
			elif event.key==K_2:
				img = pygame.transform.scale2x(img)
			rect=img.get_rect()
			rect.center=center
		elif event.type==MOUSEMOTION:
			
			rect.move_ip(event.rel)
			mouse=event.pos
			x=mouse[0]-center[0]
			y=mouse[1]-center[1]
			d=math.sqrt(x**2 + y**2)
			angle=math.degrees(-math.atan2(y,x))
			scale=abs(5*d/width)
			img=pygame.transform.rotozoom(original,angle,scale)
			rect=img.get_rect()
			rect.center=center


	screen.fill(GRAY)
	screen.blit(img,rect)
	pygame.draw.rect(screen,RED,rect,1)
	pygame.draw.line(screen,GREEN,center,mouse,1)
	pygame.draw.circle(screen,RED,center,6,1)
	pygame.draw.circle(screen,RED,mouse,6,1)


	pygame.display.update()

pygame.quit()
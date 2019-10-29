import pygame
import sys
from datetime import time
from pygame.locals import *
pygame.init()

width=1200

height=800


screen=pygame.display.set_mode((width,height))

BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(150,255,150)
BLUE=(0,0,255)
YELLOW=(255,255,0)
CYAN=(0,255,255)
MAGENTA=(255,0,255)
GRAY=(127,127,127)
WHITE=(255,255,255)



running=True

background=GREEN
# screen.fill(background)
# pygame.display.update()

speed=[1,1]
# key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE,
#     K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}
# print(key_dict)
key_dict={K_k:BLACK,K_r:RED,K_g:GREEN,K_b:BLUE,K_y:YELLOW,K_c:CYAN,K_m:MAGENTA,K_w:WHITE}
# print(key_dict)
ball = pygame.image.load("basketball.gif")
ballrect=ball.get_rect()



while running:
	for event in pygame.event.get():
		if event.type==QUIT:
			running=False
		if event.type==KEYDOWN:
			
			if event.key in key_dict:
				background=key_dict[event.key]
				caption="background color =" + str(background)
				pygame.display.set_caption(caption)
			# if event.key == pygame.K_r:
			# 	background = RED
			# elif event.key == pygame.K_g:
			# 	background = GREEN
			# exit()
	ballrect=ballrect.move(speed)
	
	
	if ballrect.left < 0 or ballrect.right>width:
		speed[0]=-speed[0]
		background=WHITE
		screen.fill(background)
		pygame.display.update()
	if ballrect.top<0 or ballrect.bottom >height:
		speed[1] = -speed[1]
		background=RED
		screen.fill(background)
		pygame.display.update()
	screen.blit(ball,ballrect)
	pygame.display.flip()



pygame.quit()
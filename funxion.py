import pygame
import math

def grafik(vershina,parametr):
	if parametr[2] > 0:
		x = vershina[0] + 250
		y = 250 - vershina[1]
		pygame.draw.circle(win, (parametr[3]), (x + parametr[0], y - parametr[1]), 1)
		pygame.display.update()
		x_1 = 250 - vershina[0] 
		y_1 = 250 - vershina[1]
		pygame.draw.circle(win, (parametr[3]), (x_1 + parametr[0], y_1 - parametr[1]), 1)
		pygame.display.update()
	elif parametr[2] < 0:
		x_2 = vershina[0] + 250
		y_2 = 250 - vershina[1]
		pygame.draw.circle(win, (parametr[3]), (x_2 + parametr[0], y_2 - parametr[1]), 1)
		pygame.display.update()
		x_3 = 250 - vershina[0] 
		y_3 = 250 - vershina[1]
		pygame.draw.circle(win, (parametr[3]), (x_3 + parametr[0], y_3 - parametr[1]), 1)
		pygame.display.update()
run = True
a = float(input('введите а:'))
b = float(input('введите b:'))
c = float(input('введите c:'))
m = round(-((b / 2)*(1 / a)))
n = round(-(b**2 - 4*a*c) / (a * 4))
red = (255, 0, 0)
green = (0, 200, 64)
yellow= (225, 225, 0)
pink = (230, 50, 230) 
blue = (100 , 100 , 250 , 200)
orange = (222, 152, 31)
blue_black = (37,31,222)
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption('Графики функции')
pygame.draw.line(win, (255,255,255), (0,250), (500, 250), 1)
pygame.draw.line(win, (255,255,255), (250, 0), (250, 500), 1)
#x
pygame.draw.line(win, (255,255,255), (480,260), (490, 270), 1)
pygame.draw.line(win, (255,255,255), (490,260), (480, 270), 1)
#y
pygame.draw.line(win, (255,255,255), (230,10), (235, 15), 1)
pygame.draw.line(win, (255,255,255), (235,10), (235, 20), 1)
pygame.display.update()
while run:	
		pygame.time.delay(100)				
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		x_mnimoe = 0
		y_mnimoe = 0
		for i in range(50):
			x_mnimoe += 1
			y_mnimoe = round(a * (x_mnimoe**2))
			grafik((x_mnimoe,y_mnimoe),(m,n,a,red))
	

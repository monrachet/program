import pygame
from random import randint

def circle_inside(x_y,food):
	if x_y[0] >= food[0] and x_y[0] <= food[0] + 20:
		if x_y[1] >= food[1] and x_y[1] <= food[1] + 20:
			return True 
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption('Игра')
x = 500 // 2
y = 500 // 2
r = 10
speed_player = 5
speed_robot = 5
eat_x = randint(7,490)
eat_y = randint(7,490)
x_robot = 200
y_robot = 100
r_robot = 10
rud = (255,0,0)
run = True
r_food = 10
a = 0
while run:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	#я
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and x > r:	
		x -= speed_player
	if keys[pygame.K_RIGHT] and x < 500 - r:
		x += speed_player
	if keys[pygame.K_UP] and y > r:
		y -= speed_player
	if keys[pygame.K_DOWN] and y < 500 - r:
		y += speed_player
	win.fill((0,0,0))
	#еда
	pygame.draw.circle(win, (255,0,255), (eat_x, eat_y),r_food)
	pygame.display.update()
	if eat_x < 500 - r_food and eat_x > r_food:
		eat_x += randint(1,3)
	if eat_y < 500 - r_food and eat_y > r_food:
		eat_y += randint(1,3)
	pygame.draw.circle(win, (225,255,255), (x, y), r)
	pygame.display.update()
	#мой противник
	if x_robot < eat_x:
		x_robot += speed_robot
	if x_robot > eat_x:
		x_robot -= speed_robot
	if y_robot < eat_y:
		y_robot += speed_robot
	if y_robot > eat_y:
		y_robot -= speed_robot
	pygame.draw.circle(win, (14,12,255), (x_robot,y_robot),r_robot)
	pygame.display.update()
	win.fill((0,0,0))
	#я ем
	if circle_inside((x,y),(eat_x,eat_y)) == True:
		r += r_food
		speed_player -= 1
		eat_x = randint(5,495)
		eat_y = randint(5,495)
		win.fill((0,0,0))
	if circle_inside((x,y),(x_robot,y_robot)) == True:
		if r > r_robot:
			r += r_robot
			speed_player -= 1
			you_foot = 1
			r_robot = 0
			win.fill((0,0,0))
	#робот ест
	if circle_inside((x_robot,y_robot),(eat_x,eat_y)) == True:
		r_robot += r_food
		speed_robot -= 1
		eat_x = randint(5,495)
		eat_y = randint(5,495)
		win.fill((0,0,0))
	if circle_inside((x_robot,y_robot),(x,y)) == True:
		if r_robot > r:
			speed_robot -= 1
			r_robot += r
			win.fill((0,0,0))
pygame.quit()

import pygame
from random import randint
import secrets
#функция для расставления кораблей
def click_inside_cell(click, cell):
	if click[0] > cell["x"] and click[0] < cell["x"] + cell["width"]:
		if click[1] > cell["y"] and click[1] < cell["y"] + cell["height"]:
			return True
pygame.init()
win = pygame.display.set_mode((500,500))
#поле
pygame.display.set_caption('Игра')
#цикл игры
run = True
b = 0
cell_1 = {"x": 50, "y": 100, "width": 40, "height": 40, "has_ship": False,"nomer":1}
cell_2 = {"x": 90, "y": 100, "width": 40, "height": 40, "has_ship": False,"nomer":2}
cell_3 = {"x": 130, "y": 100, "width": 40, "height": 40, "has_ship": False,"nomer":3}
cell_4 = {"x": 50, "y": 140, "width": 40, "height": 40, "has_ship": False, "nomer":4}
cell_5 = {"x": 90, "y": 140, "width": 40, "height": 40, "has_ship": False,"nomer":5}
cell_6 = {"x": 130, "y": 140, "width": 40, "height": 40, "has_ship": False,"nomer":6}
cell_7 = {"x": 50, "y": 180, "width": 40, "height": 40, "has_ship": False, "nomer":7}
cell_8 = {"x": 90, "y": 180, "width": 40, "height": 40,"has_ship": False, "nomer":8}
cell_9 = {"x": 130, "y": 180, "width": 40, "height": 40, "has_ship": False,"nomer":9}
cells_player = [cell_1, cell_2, cell_3, cell_4, cell_5, cell_6, cell_7, cell_8, cell_9]
#кординаты робота
cell_1_r = {"x": 350, "y": 100, "width": 40, "height": 40, "has_ship": False}
cell_2_r = {"x": 390, "y": 100, "width": 40, "height": 40, "has_ship": False}
cell_3_r = {"x": 430, "y": 100, "width": 40, "height": 40, "has_ship": False}
cell_4_r = {"x": 350, "y": 140, "width": 40, "height": 40, "has_ship": False}
cell_5_r = {"x": 390, "y": 140, "width": 40, "height": 40, "has_ship": False}
cell_6_r = {"x": 430, "y": 140, "width": 40, "height": 40, "has_ship": False}
cell_7_r = {"x": 350, "y": 180, "width": 40, "height": 40, "has_ship": False}
cell_8_r = {"x": 390, "y": 180, "width": 40, "height": 40, "has_ship": False}
cell_9_r = {"x": 430, "y": 180, "width": 40, "height": 40, "has_ship": False}
cells_robot = [cell_1_r, cell_2_r, cell_3_r, cell_4_r, cell_5_r, cell_6_r, cell_7_r, cell_8_r, cell_9_r]
#робот расставляет корабли
c = 0 
a = 0
cell_popal = 0
kol_korablei = randint(1,9)
for _ in range(kol_korablei):
	random_cell = secrets.choice(cells_robot)
	random_cell["has_ship"] = True
#робот атакует
while run:			
	pygame.time.delay(100)
	#сетка поля
	numbers = [50, 100, 50 ,220, 350, 100 , 350, 220]   
	thickness = 3
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	for _ in range(4):
		if pygame.draw.line(win, (0,0,255), (numbers[0], numbers[1]), (numbers[2], numbers[3]), thickness):
			numbers[0] += 40
			numbers[2] += 40
	for _ in range(4):
		if pygame.draw.line(win, (0,0,255), (numbers[4],numbers[5]), (numbers[6],numbers[7]), thickness):
			numbers[4] += 40
			numbers[6] += 40
	numbers_2 = [50,100,170,100,350,100,470,100]
	for _ in range(4):
		if pygame.draw.line(win, (0,0,255), (numbers_2[0], numbers_2[1]), (numbers_2[2], numbers_2[3]), thickness):
			numbers_2[1] += 40
			numbers_2[3] += 40  
	for _ in range(4):
		if pygame.draw.line(win, (0,0,255), (numbers_2[4], numbers_2[5]), (numbers_2[6],numbers_2[7]), thickness):
			numbers_2[5] += 40
			numbers_2[7] += 40 
	pygame.display.update()
	while 1:
		for i in pygame.event.get():
			if i.type == pygame.QUIT:
				exit()
			if i.type == pygame.MOUSEBUTTONDOWN:
				if i.button == 1:
					click_x_y = i.pos[0], i.pos[1]
					#расставляю корабли
					for cell in cells_player:
						if click_inside_cell((click_x_y[0],click_x_y[1]), cells_player[b]) == True:
							pygame.draw.circle(win, (255,255,255), (20 + cells_player[b]["x"], 20 + cells_player[b]["y"]), 19)
							pygame.display.update()
							cells_player[b]["has_ship"] = True
						b += 1
						if b == 9:
							b = 0
					#бью корабли
					for cell in cells_robot:
						if click_inside_cell((click_x_y[0],click_x_y[1]), cells_robot[a]) == True:
							if cells_robot[a]["has_ship"] == True:
								pygame.draw.circle(win, (255,0,0), (cells_robot[a]["x"] + 20, cells_robot[a]["y"] + 20), 19)
								pygame.display.update()
							else: 
								pygame.draw.circle(win, (70,68,66), (cells_robot[a]["x"] + 20, cells_robot[a]["y"] + 20), 19)
								pygame.display.update()
								c += 1
						a += 1
						if a == 9:
							a = 0
		#робот атакует
		if c != 0:
			random_cell_atack = secrets.choice(cells_player) 
			if random_cell_atack["has_ship"] == True:
				pygame.draw.circle(win, (250,0,0), (random_cell_atack["x"] + 20, random_cell_atack["y"] + 20), 19)
				pygame.display.update()
			else:
				pygame.draw.circle(win, (70,68,66), (random_cell_atack["x"] + 20, random_cell_atack["y"] + 20), 19)
				pygame.display.update()
			c = 0	

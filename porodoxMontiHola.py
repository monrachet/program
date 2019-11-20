from random import randint

doors = [0, 0, 0]
print(doors)
print('Породокс Монти Хола \n1 - коза, 5 - машина \n1 дверь - цифра 0, 2 - 1, 3 - 2.')
random_door = randint(0,2)
number_door = int(input('Введите номер двери:'))
doors[3 - random_door - number_door] = 1
print(doors)
doors[random_door] = 5
Monty = input('Вы не поменяли решение(да, нет):')
if Monty == 'да':
	number_door_2 = int(input('Введите номер двери:'))
	if number_door_2 == random_door:
		print('Вы выйграли автомобиль')
		print(doors)
if Monty == 'нет':
	if number_door == random_door:
		print('Вы выйграли автомобиль')
		print(doors)
	else:
		print("Увы, но вы проиграли")
		print(doors)

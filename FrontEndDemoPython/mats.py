import request
import numpy as np

np.set_printoptions(precision=8, linewidth=800, suppress=True)  # 8 is default precision


def euclid(x, y):
	import math
	return math.sqrt(x**2 + y**2)


def mat(ourPos=0, MarsPos=100, StatPosFar=50, StatPosNear=50, AsPos=-100):
	"""Takes in no inputs by default, returns matrix outlining weighted positions of objects on the map.
	Weights can be altered for each position by changing the default values."""

	ini = request.getData()
	extents = [[ini['constants']['ROOM_DIMENSIONS']['X_MIN'], ini['constants']['ROOM_DIMENSIONS']['Y_MIN']],
	           [ini['constants']['ROOM_DIMENSIONS']['X_MAX'], ini['constants']['ROOM_DIMENSIONS']['Y_MAX']]]
	size = [extents[1][0]-extents[0][0], extents[1][1]-extents[0][1]] # In [x, y]

	mapMatrix = np.ones(size)

	mapMatrix[ini['location']['x'], ini['location']['y']] = ourPos # Fill our position
	mapMatrix[ini['mapData']['Mars']['x'], ini['mapData']['Mars']['y']] = MarsPos # Fill Mars' position
	# Fill Station's positions
	distToOne = euclid(ini['mapData']['Station1']['x'], ini['mapData']['Station1']['y'])
	distToTwo = euclid(ini['mapData']['Station2']['x'], ini['mapData']['Station2']['y'])
	if distToOne < distToTwo:
		mapMatrix[ini['mapData']['Station1']['x'], ini['mapData']['Station1']['y']] = StatPosNear
		mapMatrix[ini['mapData']['Station2']['x'], ini['mapData']['Station2']['y']] = StatPosFar
	else:
		mapMatrix[ini['mapData']['Station1']['x'], ini['mapData']['Station1']['y']] = StatPosFar
		mapMatrix[ini['mapData']['Station2']['x'], ini['mapData']['Station2']['y']] = StatPosNear

	for i in range(len(ini['mapData']['Asteroids'])):
		mapMatrix[ini['mapData']['Asteroids'][i]['x'], ini['mapData']['Asteroids'][i]['y']] = AsPos

	print('Indexing remains the same regardless of orientation,\n but this matrix is oriented with South up.')
	return mapMatrix

def isAsteroid():
	"""Check if the thing directly ahead is an asteroid."""
	ini = request.getData()
	direction = ini['direction']
	if direction is 'N':
		goingTo = [ini['location']['x']+1, ini['location']['y']]
	elif direction is 'S':
		goingTo = [ini['location']['x']-1, ini['location']['y']]
	elif direction is 'E':
		goingTo = [ini['location']['x'], ini['location']['y']+1]
	else:
		goingTo = [ini['location']['x'], ini['location']['y'] - 1]
		print('Assumed spaceship is facing West.')
	asPos = []
	for i in range(len(ini['mapData']['Asteroids'])):
		asPos.append([ini['mapData']['Asteroids'][i]['x'], ini['mapData']['Asteroids'][i]['y']])

	if goingTo in asPos:
		print('Asteroid dead-ahead!')
		return True
	else:
		return False

def asteroid(mapMatrix):
	"""Steer around an asteroid using the map matrix."""
	ini = request.getData()
	#otherWay = False
	direction = ini['direction']
	usX = ini['location']['x']; usY = ini['location']['y']
	if direction is 'N':
		if mapMatrix[usX + 1, usY] == -100 or mapMatrix[usX + 1, usY + 1] == -100 or mapMatrix[usX + 1, usY + 2] == -100 or \
				mapMatrix[usX, usY + 2] == -100:
			#otherWay = True
			request.turn('W')
			request.move(1)
			request.turn('N')
			request.move(2)
			request.turn('E')
			request.move(1)
			request.turn('N')
		else:
			request.turn('E')
			request.move(1)
			request.turn('N')
			request.move(2)
			request.turn('W')
			request.move(1)
			request.turn('N')
	elif direction is 'S':
		if mapMatrix[usX - 1, usY] == -100 or mapMatrix[usX - 1, usY + 1] == -100 or mapMatrix[usX - 1, usY + 2] == -100 or \
				mapMatrix[usX, usY + 2] == -100:
			#otherWay = True
			request.turn('W')
			request.move(1)
			request.turn('S')
			request.move(2)
			request.turn('E')
			request.move(1)
			request.turn('S')
		else:
			request.turn('E')
			request.move(1)
			request.turn('S')
			request.move(2)
			request.turn('W')
			request.move(1)
			request.turn('S')
	elif direction is 'E':
		if mapMatrix[usX, usY - 1] == -100 or mapMatrix[usX + 1, usY - 1] == -100 or mapMatrix[usX + 2, usY - 1] == -100 or \
				mapMatrix[usX + 2, usY] == -100:
			#otherWay = True
			request.turn('N')
			request.move(1)
			request.turn('E')
			request.move(2)
			request.turn('S')
			request.move(1)
			request.turn('E')
		else:
			request.turn('S')
			request.move(1)
			request.turn('E')
			request.move(2)
			request.turn('N')
			request.move(1)
			request.turn('E')
	else:
		print('Hopefully the spaceship is facing West.')
		if mapMatrix[usX, usY - 1] == -100 or mapMatrix[usX - 1, usY - 1] == -100 or mapMatrix[usX - 2, usY - 1] == -100 or \
				mapMatrix[usX - 2, usY] == -100:
			#otherWay = True
			request.turn('N')
			request.move(1)
			request.turn('W')
			request.move(2)
			request.turn('S')
			request.move(1)
			request.turn('W')
		else:
			request.turn('S')
			request.move(1)
			request.turn('W')
			request.move(2)
			request.turn('N')
			request.move(1)
			request.turn('W')
	#if isAsteroid():

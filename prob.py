import random


blue = [3,3,3,3,3,3]
yel = [6,6,2,2,2,2]
red = [5,5,5,1,1,1]
green = [0,0,4,4,4,4]

dice1 = 0
dice2 = 0

for x in range(1000):
	if blue[random.randint(0, 5)] + blue[random.randint(0, 5)] > yel[random.randint(0,5)] + yel[random.randint(0,5)]:
		dice1 = dice1+1
	else:
		dice2 = dice2+1

print('Blue vs Yellow: Blue has ' + str(dice1) + ' and Yellow has ' + str(dice2))

dice1 = 0
dice2 = 0

for x in range(1000):
        if blue[random.randint(0, 5)] + blue[random.randint(0, 5)] > red[random.randint(0,5)] + red[random.randint(0,5)]:
                dice1 = dice1+1
        else:
                dice2 = dice2+1

print('Blue vs Red: Blue has ' + str(dice1) + ' and Red has ' + str(dice2))

dice1 = 0
dice2 = 0

for x in range(1000):
        if blue[random.randint(0, 5)] + blue[random.randint(0, 5)] > green[random.randint(0,5)] + green[random.randint(0,5)]:
                dice1 = dice1+1
        else:
                dice2 = dice2+1

print('Blue vs Green: Blue has ' + str(dice1) + ' and Green has ' + str(dice2))

dice1 = 0
dice2 = 0

for x in range(1000):
        if yel[random.randint(0, 5)] + yel[random.randint(0, 5)] > red[random.randint(0,5)] + red[random.randint(0,5)]:
                dice1 = dice1+1
        else:
                dice2 = dice2+1

print('Yellow vs Red: Yellow has ' + str(dice1) + ' and Red has ' + str(dice2))

dice1 = 0
dice2 = 0

for x in range(1000):
        if green[random.randint(0, 5)] + green[random.randint(0, 5)] > red[random.randint(0,5)] + red[random.randint(0,5)]:
                dice1 = dice1+1
        else:
                dice2 = dice2+1

print('Green vs Red: Green has ' + str(dice1) + ' and Red has ' + str(dice2))


dice1 = 0
dice2 = 0

for x in range(1000):
        if green[random.randint(0, 5)] + green[random.randint(0, 5)] > yel[random.randint(0,5)] + yel[random.randint(0,5)]:
                dice1 = dice1+1
        else:
                dice2 = dice2+1

print('Green vs Yellow: Green has ' + str(dice1) + ' and Yellow has ' + str(dice2))

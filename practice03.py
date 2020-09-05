#猜數字遊戲
import random

pwd = random.randint(1,100)

maxN = 100
minN = 1

while  True:
    guess = int( input('請輸入{}~{}間的數字: '.format(minN,maxN)))
    if guess > maxN or guess < minN:
        print('猜測數字超過範圍!', end='')
        continue
    if guess == pwd:
        print('答對了,密碼是', pwd)
        break
    if guess < pwd:
        minN = guess + 1
    elif guess > pwd:
        maxN = guess - 1
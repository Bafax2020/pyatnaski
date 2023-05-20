import pygame
import random
pygame.init()

WIN = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]

global image_list


def geti():
    image_list = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    image_list[1] = pygame.image.load("images\i1.jpg")
    image_list[2] = pygame.image.load("images\i2.jpg")
    image_list[3] = pygame.image.load("images\i3.jpg")
    image_list[4] = pygame.image.load("images\i4.jpg")
    image_list[5] = pygame.image.load("images\i5.jpg")
    image_list[6] = pygame.image.load("images\i6.jpg")
    image_list[7] = pygame.image.load("images\i7.jpg")
    image_list[8] = pygame.image.load("images\i8.jpg")
    image_list[9] = pygame.image.load("images\i9.jpg")
    image_list[10] = pygame.image.load("images\i10.jpg")
    image_list[11] = pygame.image.load("images\i11.jpg")
    image_list[12] = pygame.image.load("images\i12.jpg")
    image_list[13] = pygame.image.load("images\i13.jpg")
    image_list[14] = pygame.image.load("images\i14.jpg")
    image_list[15] = pygame.image.load("images\i15.jpg")
    return image_list


def paint_exe():
    x = 0
    y = 0
    for z_fold in range(16):
        if xiaomy_list[z_fold] > 0:
            Windows.blit(image_list[xiaomy_list[z_fold]], (x,y))
        x += 100
        if z_fold == 3 or z_fold == 7 or z_fold == 11:
            x = 0
            y += 100


def paint_exe_random_exe():
    xiaomy = list(range(16))
    random.shuffle(xiaomy)
    return xiaomy


def available_muw(newgame):
    gg = list()
    ggbibaindex = newgame.index(0)
    if ggbibaindex == 0:
        gg.append(newgame[1])
        gg.append(newgame[4])
    elif ggbibaindex == 1:
        gg.append(newgame[0])
        gg.append(newgame[2])
        gg.append(newgame[5])
    elif ggbibaindex == 2:
        gg.append(newgame[1])
        gg.append(newgame[3])
        gg.append(newgame[6])
    elif ggbibaindex == 3:
        gg.append(newgame[2])
        gg.append(newgame[7])
    elif ggbibaindex == 4:
        gg.append(newgame[0])
        gg.append(newgame[5])
        gg.append(newgame[8])
    elif ggbibaindex == 5:
        gg.append(newgame[1])
        gg.append(newgame[4])
        gg.append(newgame[6])
        gg.append(newgame[9])
    elif ggbibaindex == 6:
        gg.append(newgame[2])
        gg.append(newgame[5])
        gg.append(newgame[7])
        gg.append(newgame[10])
    elif ggbibaindex == 7:
        gg.append(newgame[3])
        gg.append(newgame[6])
        gg.append(newgame[11])
    elif ggbibaindex == 8:
        gg.append(newgame[4])
        gg.append(newgame[9])
        gg.append(newgame[12])
    elif ggbibaindex == 9:
        gg.append(newgame[5])
        gg.append(newgame[8])
        gg.append(newgame[10])
        gg.append(newgame[13])
    elif ggbibaindex == 10:
        gg.append(newgame[6])
        gg.append(newgame[9])
        gg.append(newgame[11])
        gg.append(newgame[14])
    elif ggbibaindex == 11:
        gg.append(newgame[7])
        gg.append(newgame[10])
        gg.append(newgame[15])
    elif ggbibaindex == 12:
        gg.append(newgame[8])
        gg.append(newgame[13])
    elif ggbibaindex == 13:
        gg.append(newgame[9])
        gg.append(newgame[12])
        gg.append(newgame[14])
    elif ggbibaindex == 14:
        gg.append(newgame[10])
        gg.append(newgame[13])
        gg.append(newgame[15])
    elif ggbibaindex == 15:
        gg.append(newgame[11])
        gg.append(newgame[14])
    return gg


xiaomy_list = paint_exe_random_exe()  # рандомим местопололожениееее картинок
image_list = geti()  # лист бумаги формата а4 из картинок
# окно
winX = 399
WinY = 399
Windows = pygame.display.set_mode((winX,WinY))
pygame.display.set_caption("капибара считает")
back = (0,0,0)

FPS = 30
clock = pygame.time.Clock()

#игровой цикл
game = True
while game:
    for k in pygame.event.get():
        if k.type == pygame.QUIT:
            game = False

    muv = available_muw(xiaomy_list)
    if k.type == pygame.MOUSEBUTTONDOWN:
        pozition = k.pos
        bystop = int(pozition[0]/100) + int(pozition[1]/100)*4
        if xiaomy_list[bystop] in muv:
            ziro = xiaomy_list.index(0)
            xiaomy_list[ziro] = xiaomy_list[bystop]
            xiaomy_list[bystop] = 0

    if WIN == xiaomy_list:
        game = False







    Windows.fill(back)
    paint_exe()
    clock.tick(FPS)
    pygame.display.update()
    
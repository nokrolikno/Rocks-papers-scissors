import pygame as pg
import random as rn
import sys
from time import sleep
from objects import Object
RES = WIDTH, HEIGHT = 600, 600
FPS = 30
clock = pg.time.Clock()
all_sprites = pg.sprite.Group()
sc = pg.display.set_mode(RES)

Players = ['Scissor', 'Paper', 'Rock']
obj_images = ['Scissor.png', 'Paper.png', 'Rock.png']
obj_pngs = [pg.image.load(path).convert_alpha() for path in obj_images]
sounds = [pg.mixer.Sound("Rock.wav"),
          pg.mixer.Sound("Scissor.wav"),
          pg.mixer.Sound("Paper.wav")]

MOBS = 100
SPEED = 1

for i in range(MOBS):
    me = rn.randint(0, 2)
    x = rn.random() * (WIDTH - 100) + 50
    y = rn.random() * (HEIGHT - 100) + 50
    image = obj_pngs[me]
    player = Players[me]
    sound = sounds[me]
    new_sprite = Object(x,y, image, player, SPEED, 0, 0, sound)
    all_sprites.add(new_sprite)

List = all_sprites.sprites()
timer = 0
go = False

while True:
    if go:
        all_sprites.update(List)

        sc.fill((255, 76, 91))
        pg.draw.rect(sc, (255, 255, 255), 
                     (50 + (timer // 10), 50 + (timer // 10),
                      500 - 2*(timer // 10), 500 - 2*(timer // 10)))
        all_sprites.draw(sc)
        timer += 1
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit(0)
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                go = True
    pg.display.update()
    clock.tick(FPS)

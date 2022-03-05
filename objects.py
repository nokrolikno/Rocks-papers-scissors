import pygame as pg
import math
import random as rn
pg.mixer.pre_init(44100, -16, 1, 512)
pg.init()

class Object(pg.sprite.Sprite):    
    def __init__(self, posx, posy, png, me, speed, vector_x, vector_y, sound):
        
        pg.sprite.Sprite.__init__(self)
        self.image = png
        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy)
        self.me = me
        self.sound = sound
        self.speed = speed
        self.vector_x = vector_x
        self.vector_y = vector_y
        self.timer = 0

    def winning(self, obj):
        if self.me == 'Scissor':
            if obj.me == 'Paper':
                return True
            if obj.me == 'Rock':
                return False
        elif self.me == 'Paper':
            if obj.me == 'Rock':
                return True
            if obj.me == 'Scissor':
                return False
        else:
            if obj.me == 'Scissor':
                return True
            return False

    def deltas(self, pos, obj):
        delta_x = obj.rect.center[0] - pos[0]
        delta_y = obj.rect.center[1] - pos[1]
        return delta_x, delta_y

    def vector_change(self, obj):
        WIDTH, HEIGHT = 400, 400
        delta_x, delta_y = self.deltas(self.rect.center, obj)
        if math.sqrt(delta_x**2 + delta_y**2) > 13:
            if delta_x != 0 and delta_y != 0:
                if self.winning(obj):
                    self.vector_x += 100/(delta_x*abs(delta_x))
                    self.vector_y += 100/(delta_y*abs(delta_y))
                else:
                    self.vector_x -= 900/(delta_x*abs(delta_x))
                    self.vector_y -= 900/(delta_y*abs(delta_y))
        else:
            if not self.winning(obj):
                self.me = obj.me
                self.image = obj.image
                self.sound.play()
                self.sound = obj.sound
        

    def update(self, List):
        for obj in List:
            if obj != self:
                if obj.me != self.me:
                    self.vector_change(obj)
                    
        self.vector_x = self.vector_x
        self.vector_y = self.vector_y

        Right_wall = self.rect.x+12 < 550 - (self.timer // 10)
        Left_wall = self.rect.x > 50 + (self.timer // 10)
        Up_wall = self.rect.y > 50 + (self.timer // 10)
        Down_wall = self.rect.y+12 < 550 - (self.timer // 10)
        
        randx, randy = rn.randint(-1, 1), rn.randint(-1, 1)
        if (randx > 0 and Right_wall):
            self.rect.x += randx
        if (randy > 0 and Down_wall):
            self.rect.y += randy
        if (randx < 0 and Left_wall):
            self.rect.x += randx
        if (randy < 0 and Up_wall):
            self.rect.y += randy
            
        if (self.vector_x == 0):
            self.vector_x = rn.randint(-3, 3)
        if (self.vector_y == 0):
            self.vector_y = rn.randint(-3, 3)

        if (self.vector_x > 0 and Right_wall):
            self.rect.x += 2
        if (self.vector_x < 0 and Left_wall):
            self.rect.x -= 2
        if (self.vector_y > 0 and Down_wall):
            self.rect.y += 2
        if (self.vector_y < 0 and Up_wall):
            self.rect.y -= 2
            
        if (self.vector_x > 2000 and Right_wall):
            self.rect.x += 2
        if (self.vector_x < -2000 and Left_wall):
            self.rect.x -= 2
        if (self.vector_y > 2000 and Down_wall):
            self.rect.y += 2
        if (self.vector_y < -2000 and Up_wall):
            self.rect.y -= 2

        self.vector_x, self.vector_y = 0, 0
        self.timer += 1
                             
        

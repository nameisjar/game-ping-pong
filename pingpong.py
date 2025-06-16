from pygame import *

BLACK = (0, 0, 0)
img_back = "background.jpg"
img_racket_r = "racket_r.png"
win_width = 700
win_height = 500
display.set_caption("PingPong")
window = display.set_mode((win_width, win_height))
# window.fill(BLACK)
background = transform.scale(image.load(img_back), (win_width, win_height))
fps = time.Clock()

class GameSprite(sprite.Sprite):
#class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #call for the class (Sprite) constructor:
        sprite.Sprite.__init__(self)
        #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        #every sprite must have the rect property that represents the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
#method drawing the character on the window
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#main player class
class Racket_Right(GameSprite):
    #method to control the sprite with arrow keys
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Racket_Left(GameSprite):
    #method to control the sprite with arrow keys
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

racket_r = Racket_Right(img_racket_r, 450, 250, 50, 50, 2)

run = True
while run:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    racket_r.reset()
    display.update()
    fps.tick(60)

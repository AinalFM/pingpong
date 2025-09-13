from pygame import *

#parent class for sprites
class GameSprite(sprite.Sprite): # untuk objek bolanya
    def __init__(self, player_image, player_x, player_y, player_speed, widht, height):
        super().__init__() # mewarisi semua properti dri kelas sprite
        self.image = transform.scale(image.load(player_image), (widht, height)) #e.g. 55,55 - parameters
        self.speed = player_speed
        self.rect = self.image.get_rect() # buat hitbox 
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self): # untuk pergerakan bola
        ball.rect.x += speed_x
        ball.rect.y += speed_y

class Player(GameSprite): # untuk objek padle
    def update_r(self): # ini utk padle sebelah kanan
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self): # utk padle sebelah kiri
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#game scene:
back = (200, 255, 255) #background color (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

#creating ball and paddles   
racket1 = Player('racket.png', 30, 200, 4, 50, 150) 
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 0, 50, 50)

# buat objek timer untuk atur besaran FPS
game = True
clock = time.Clock()
FPS = 60
# kecepatan bola
speed_x = 3
speed_y = 3

# pembuatan font 
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back) 
        racket1.reset()
        racket2.reset()
        ball.reset()
        racket1.update_l()
        racket2.update_r()
        ball.update()
        # tabrakan yang terjadi antar raket
        # tabrakan antar bole dengan raket1
        if sprite.collide_rect(racket1, ball):
            speed_x *= -1
            speed_y *= 1
        # tabrakan antar bola dengan raket2
        if sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        # kalau mantul ke bagian bawah
        if ball.rect.y > win_height-50:
            speed_y *= -1
        # # kalau mantul ke bagian atas
        if ball.rect.y < 0:
            speed_y *= 1
        #if ball flies behind this paddle, display loss condition for player 1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game = True
        #if the ball flies behind this paddle, display loss condition for player 2
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game = True
    display.update()
    clock.tick(FPS)
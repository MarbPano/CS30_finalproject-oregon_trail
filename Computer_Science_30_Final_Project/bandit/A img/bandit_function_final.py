import pygame
import time 
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("Bandit function")

walkRight = [pygame.image.load('HR1.png'), pygame.image.load('HR2.png'), pygame.image.load('HR3.png'), pygame.image.load('HR4.png'), pygame.image.load('HR5.png'), pygame.image.load('HR6.png'), pygame.image.load('HR7.png'), pygame.image.load('HR8.png'), pygame.image.load('HR9.png')]
walkLeft = [pygame.image.load('HL1.png'), pygame.image.load('HL2.png'), pygame.image.load('HL3.png'), pygame.image.load('HL4.png'), pygame.image.load('HL5.png'), pygame.image.load('HL6.png'), pygame.image.load('HL7.png'), pygame.image.load('HL8.png'), pygame.image.load('HL9.png')]
bg = pygame.image.load('bg.jpg')

bullet_img_right = pygame.image.load('bullet_right.png')
bullet_img_left = pygame.image.load('bullet_left.png')
#everything above is loading the images
clock = pygame.time.Clock()


health = 3

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0#walkcount is the image load in the list 0 is the first
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):#drawing the character
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):#drawing when not standing in place
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))#to show image and location 
                self.walkCount +=1
        else:#drawing when right or left
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 100#where it start
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)#setting up text
        text = font1.render('-1', 1, (255,0,0))
        win.blit(text, (250 - (text.get_width()/2),200))#so whenever u get hit it shows how much u lost
        pygame.display.update()#important
        i = 0
        while i < 200:#to restart the thing. this is important to putting the player in certain spot after getting hit
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()
                


class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing# so the vel is going left or right depending on the side facing

    def draw(self,win):
        if facing > -1: #on the positive x(right)
            win.blit(bullet_img_right, (self.x, self.y))
            
        else:#left
            win.blit(bullet_img_left, (self.x, self.y))


class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
#everythig above is loading sprites
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 5
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 25#need to hit 25 times, so need 25 bullets 
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:#to show it died
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')

        

def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render('Health: ' + str(health), 1, (0,0,0))
    bullet_amount_text = font.render("Bullets: " + str(bullet_amount), 1, (0,0,0))
    
    win.blit(bullet_amount_text, (320, 40))#second coma is the location
    win.blit(text, (350, 10))
    man.draw(win)
    bandit.draw(win)#gotta put the window so we know where to draw it on

    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()


#mainloop
font = pygame.font.SysFont('comicsans', 30, True)
man = player(200, 410, 64,64)#assign man
bandit = enemy(100, 410, 64, 64, 450)#assign bandit
shootLoop = 0
bullets = []
bullet_amount = 35

run = True
while run:
    clock.tick(27)
    
    if health <= 0:#when health is used game dies
        #code to connect the food inventory to here
        run = False
        
    if bullet_amount <= 0:#when bullet amount disappears game dies bandit has taken stuff
        #code to connect the food inventory here
        run = False 

    if bandit.visible == True:#collision only happens once visible 
        if man.hitbox[1] < bandit.hitbox[1] + bandit.hitbox[3] and man.hitbox[1] + man.hitbox[3] > bandit.hitbox[1]:#this is actually too complicated to explain
            if man.hitbox[0] + man.hitbox[2] > bandit.hitbox[0] and man.hitbox[0] < bandit.hitbox[0] + bandit.hitbox[2]:
                man.hit()
                health -= 1
                
    elif bandit.visible == False:#once bandit dies game ends
        run = False

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    for bullet in bullets:
        if bullet.y - bullet.radius < bandit.hitbox[1] + bandit.hitbox[3] and bullet.y + bullet.radius > bandit.hitbox[1]:
            if bullet.x + bullet.radius > bandit.hitbox[0] and bullet.x - bullet.radius < bandit.hitbox[0] + bandit.hitbox[2]:
                bandit.hit()#doing it so when the enemy is hit
                bullets.pop(bullets.index(bullet))#bullets disappear at collision
                
        if bullet.x < 500 and bullet.x > 0:#500 and 0 is the direction and distance
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()#activate keys geting pressed

    if keys[pygame.K_SPACE] and shootLoop == 0:
        
        if man.left:
            facing = -1#left side is negative
        else:
            facing = 1#right is positive
            
        if len(bullets) < 3:#shoot only 3 bullet at a time 
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))
            bullet_amount -= 1

        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1#the jumping is a quadratic formula to follow a jump path.
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()



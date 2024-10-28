import pygame
import random
pygame.init()

SIZE = WIDTH,HEIGHT = 1200,700
SCREEN = pygame.display.set_mode(SIZE)

WHITE =255,255,255
RED = 255,0,0
BLUE = 0,0,255
BLACK = 0,0,0

def homeScreen():
    bg_img = pygame.image.load("C:/Users/Asus/Pictures/20220112_184634.jpg")
    font = pygame.font.SysFont(None,80)
    text = font.render(f"Welcome to Space Shooter",True,WHITE)
    text_2 = font.render(f"Press SPACE to Strat Game",True,BLACK)
    while True:
        
        eventlist = pygame.event.get()
        for event in eventlist:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
        SCREEN.blit(bg_img,(0,0))
        SCREEN.blit(text,(100,300))
        SCREEN.blit(text_2,(200,400))
        pygame.display.flip()

def playerHealth(count):
    font = pygame.font.SysFont(None,30)
    text = font.render(f"Health :{count}",True , BLACK)
    SCREEN.blit(text,(5,500))

def gameOver():
    font = pygame.font.SysFont(None,80)
    text = font.render(f"Game Over",True,BLACK)
    while True:
        eventlist = pygame.event.get()
        for event in eventlist:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        SCREEN.blit(text,(300,300))
        pygame.display.flip()

def main():
    move_x = 0
    ship = pygame.image.load("C:/Users/Asus/Pictures/SS1.gif")
    ship_w = ship.get_width()
    ship_h = ship.get_height()
    ship_x = WIDTH//2-ship_w//2
    ship_y = HEIGHT - ship_h

    enemyShip = pygame.image.load("C:/Users/Asus/Pictures/ssv.gif")
    eship_w = enemyShip.get_width()
    eship_h = enemyShip.get_height()

    enemylist = []
    nrows = 1
    ncols = WIDTH//eship_w

    bullet_y = ship_y
    bullet_w = 3
    bullet_h = 5
    moveBullet = 0

    for i in range(nrows):
        for j in range(ncols):
            enemyX = eship_w*j
            enemyY = eship_h*i
            enemyRect = pygame.Rect(enemyX,enemyY,eship_w,eship_h)
            enemylist.append(enemyRect)

        random_enemy = random.choice(enemylist)
        enemy_bullet_w = 1
        enemy_bullet_h = 1
        enemy_bullet_x = random_enemy.x + eship_w //2
        enemy_bullet_y = random_enemy.bottom - 10

        playerHealthCount = 100

        while True:
            bullet_x = ship_x + ship_w//2-2
            eventlist = pygame.event.get()
            for event in eventlist:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        move_x = 2
                    elif event.key == pygame.K_LEFT:
                        move_x = -2
                    elif event.key == pygame.K_SPACE:
                        moveBullet = -7
                       

                else:
                    move_x = 0
            SCREEN.fill(WHITE)
            bullet_rect = pygame.draw.rect(SCREEN,RED,[bullet_x,bullet_y,bullet_w,bullet_h])
            bullet_y += moveBullet
            SCREEN.blit(ship,(ship_x,ship_y))
            ship_x +=move_x
            ship_rect = pygame.Rect(ship_x,ship_y,ship_w,ship_h)
            enemyBullet = pygame.draw.rect(SCREEN, BLUE, [enemy_bullet_x,enemy_bullet_y,enemy_bullet_h,enemy_bullet_y])
            enemy_bullet_y +=7
            for i in range(len(enemylist)):
                SCREEN.blit(enemyShip,(enemylist[i].x,enemylist[i].y))

            for i in range(len(enemylist)):
                if bullet_rect.colliderect(enemylist[i]):
                    del enemylist[i]
                    bullet_y = ship_y
                    moveBullet = 0
                    break
            if bullet_y < 0:
                bullet_y = ship_y
                moveBullet = 0
            if enemy_bullet_y > HEIGHT:
                random_enemy = random.choice(enemylist)
                enemy_bullet_x = random_enemy.x + eship_w//2
                enemy_bullet_y = random_enemy.bottom - 10
                
            if enemyBullet.colliderect(ship_rect):
                playerHealthCount -=1
            if playerHealthCount == 0:
                gameOver()
            playerHealth(playerHealthCount)
            pygame.display.flip()
homeScreen()

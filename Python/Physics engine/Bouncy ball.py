import pygame as pg
Image = r"C:\Users\Wolke\Downloads\kenney_rolling-ball-assets\PNG\Default\ball_red_small.png"
pg.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Gravity Simulation")

clock = pg.time.Clock()
FPS = 90

ball = pg.image.load(Image)
rect = ball.get_rect()
rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

velocity = pg.math.Vector2(0, 0)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    velocity.x -= .01
    velocity.y += .2
    
    rect.center += velocity
    
    if rect.bottom + 50 > SCREEN_HEIGHT:
        velocity.y += -1
    
    if rect.left + 50 > 0:
        velocity.x += .01
        
    elif rect.right - 1000 < SCREEN_WIDTH:
        velocity.x -= .01
        
    
    screen.fill((255, 255, 255))
    
    screen.blit(ball, rect)
    
    pg.display.flip()
    clock.tick(FPS)
            
pg.quit()
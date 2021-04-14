import pygame



BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()


size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PingPong by Xioxostic Creations")

rect_x = 400
rect_y = 580

rect_change_x = 0
rect_change_y = 0

ball_x = 50
ball_y = 50

ball_change_x = 5
ball_change_y = 5

score = 0

def drawrect(screen,x,y):
    if x <= 0:
        x = 0
    if x >= 699:
        x = 699    
    pygame.draw.rect(screen,RED,[x,y,100,20])

    
done = False
clock=pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect_change_x = -6
            elif event.key == pygame.K_RIGHT:
                rect_change_x = 6
         

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rect_change_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                rect_change_y = 0            

    screen.fill(BLACK)
    rect_x += rect_change_x
    rect_y += rect_change_y

    

    ball_x += ball_change_x
    ball_y += ball_change_y

    if ball_x<0:
        ball_x=0
        ball_change_x = ball_change_x * -1
    elif ball_x>785:
        ball_x=785
        ball_change_x = ball_change_x * -1
    elif ball_y<0:
        ball_y=0
        ball_change_y = ball_change_y * -1
    elif ball_x>rect_x and ball_x<rect_x+100 and ball_y==565:
        ball_change_y = ball_change_y * -1
        score = score + 1
    elif ball_y>600:
        ball_change_y = ball_change_y * -1
        score = 0                        
    pygame.draw.rect(screen,WHITE,[ball_x,ball_y,15,15])
    
    drawrect(screen,rect_x,rect_y)
    
    font= pygame.font.SysFont('Calibri', 25, False, False)
    text = font.render("Score = " + str(score), True, WHITE)
    screen.blit(text,[600,100])    

       
    pygame.display.flip()         
    clock.tick(60)

pygame.quit()   
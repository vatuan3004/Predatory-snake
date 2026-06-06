import pygame as pg
import random
pg.init()
pg.mixer.init()
face_img = pg.image.load("face.png")
food_img = pg.image.load("food.png")
bg_img = pg.image.load("background.png")
eat_sound = pg.mixer.Sound("eat.mp3")
game_over = pg.mixer.Sound("game over.mp3")
game_over.set_volume(0.4)
#Resize picture
face_img = pg.transform.scale(face_img, (70,70))
food_img = pg.transform.scale(food_img, (70,70))
bg_img = pg.transform.scale(bg_img, (1280,720))
#Window game
screen = pg.display.set_mode((1280,720))
pg.display.set_caption("Snake Game")
#Var
score = highscore = 0
snake_part = 20
x = y = 200
x_change = y_change = 0
body_snake = []
length = 1
#Create food
food_x = random.randint(0,27)*snake_part
food_y = random.randint(0,27)*snake_part
#Speed snake
clock = pg.time.Clock()
FBS = 30
speed = 5
#Def function
def check_col():
    if x<0 or x>1280 or y<0 or y>1280 or (x,y) in body_snake[:-1]:
        game_over.play()
        return False
    return True
def score_view():
    font = pg.font.Font(None,36)
    if gameplay:
        score_txt =  font.render(f"Score: {score}",True,(255,255,255))
        screen.blit(score_txt,(0,0))
        score_txt =  font.render(f"High Score: {highscore}",True,(255,255,255))
        screen.blit(score_txt,(170,0))
    else:
        note_txt =  font.render(f"Press space to paly again:",True,(255,255,255))
        screen.blit(note_txt,(0,0))
        
#Game loop
gameplay = True
running = True
while True:
    clock.tick(FBS)
    for event in pg.event.get():
        #Quit
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        #Snake move
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT and x_change == 0:
                x_change = -snake_part
                y_change = 0
            elif event.key == pg.K_RIGHT and x_change == 0:
                x_change = snake_part
                y_change = 0
            elif event.key == pg.K_UP and y_change == 0:
                x_change = 0
                y_change = -snake_part
            elif event.key == pg.K_DOWN and y_change == 0:
                x_change = 0
                y_change = snake_part
                
            elif event.key == pg.K_SPACE:
                gameplay = True
        #Clear screen
        screen.blit(bg_img,(0,0))
        score_view()
        if gameplay:
            #Update snake position
            x += x_change
            y += y_change
            #Add snake part
            body_snake.append((x,y))
            #Remove snake part
            if len(body_snake)>length:
                del body_snake[0]
            #Check snake eat food
            if x == food_x and y == food_y:
                eat_sound.play()
                length += 1
                score += 1
                if score > highscore: highscore=score
                #Random food
                food_x = random.randint(0,63)*snake_part
                food_y = random.randint(0,35)*snake_part
            #Draw snake 
            for x,y in body_snake:
                screen.blit(face_img, (x,y))  
            #Draw food
            screen.blit(food_img,(food_x,food_y))
            gameplay = check_col()
          
           
        else:
            #Reset game
            x = y = 200
            x_change = y_change = 0
            body_snake = []
            length = 1
            score = 1


    #Update screen
    pg.display.update() 
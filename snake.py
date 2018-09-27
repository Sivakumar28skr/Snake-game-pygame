import pygame,random,time,shelve
from pygame.locals import *

pygame.init()
pygame.mixer.init()
# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
red=(255,0,0)
brick=(178, 121, 41)
blue=(0,0,255)
lightG=(108, 249, 32)
dark_green=(0,199,0)
dark_red=(200,0,0)
bright_black=(50,50,50)
green=(0,255,0)
display_width=800
display_height=600
screen= pygame.display.set_mode((display_width,display_height))


pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
apple_width=19
apple_height=19

pygame.mixer.music.load('Snake.mp3')
eat=pygame.mixer.Sound('EatSound.ogg')
die=pygame.mixer.Sound('DieSound.ogg')

introImg=pygame.image.load('frontimage.png')
introImg=pygame.transform.scale(introImg,(750,550))
    
appleImg=pygame.image.load('apple.png')
appleImg=pygame.transform.scale(appleImg,(19,19))


bgrImg=pygame.image.load('background.jpg')
bgrImg=pygame.transform.scale(bgrImg,(760,560))

wallImg=pygame.image.load('wall.jpg')
wallImg=pygame.transform.scale(wallImg,(1000,1000))
pygame.display.flip()

def unpause():
    countdown()
    global pause
    pause=False
    
def paused():
    while pause:
        message_display('Paused',60,blue,(display_width/2),(display_height/2))
        message_display('press space for continue',60,blue,(display_width/2),(display_height/2+100))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    unpause()
def apples(thingx,thingy):
    
    screen.blit(appleImg,(thingx,thingy))
def message_display(text,size,color,x,y):
    largeText=pygame.font.SysFont('comicsansms',size)
    textSurf=largeText.render(text,True,color)
    TextRect= textSurf.get_rect()
    TextRect.center= (x,y)
    screen.blit(textSurf,TextRect)
    pygame.display.update()
def carscore(count):
    font=pygame.font.SysFont(None,30)
    text=font.render('Score: '+ str(count), True, WHITE)
    screen.blit(text,(0,0))
def crash(score):
    #pygame.mixer.music.stop()
    if musics==True:
        die.play()
        time.sleep(1)
        die.stop()
    #die.fadeout(1)
    #screen.blit(wallImg,(0,0))
    #screen.blit(bgrImg,(20,20))
    message_display('Game Over',60,blue,(display_width/2),(display_height/2))
    time.sleep(2)
    screen.fill(BLACK)
    message_display('Game Over',60,WHITE,(display_width/2),(display_height/2))
    message_display('Click Space for Restart',20,red,(display_width/2),(display_height/2+100))
    message_display('Click Esc for Quit',20,red,(display_width/2),(display_height/2+180))
    shelfFile=shelve.open('snake')
    highScore=shelfFile[typeName]
    
    if score > highScore:
        shelfFile[typeName]=score
        shelfFile.close
        message_display(('Highscore :'+str(score)),25,WHITE,(display_width/2-100),(display_height/2+270))
        message_display(('Score :'+str(score)),30,WHITE,(display_width/2-100),(display_height/2+230))
    else:
        message_display(('Highscore :'+str(highScore)),25,WHITE,(display_width/2-100),(display_height/2+270))
    message_display(('Score :'+str(score)),30,WHITE,(display_width/2-100),(display_height/2+230))
    
    while True:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                
                pygame.quit()
                quit()
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    option()
                elif event.key ==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            
def intro():
    pygame.mixer.music.play()
    screen.fill(BLACK)
    screen.blit(introImg,(25,25))
    time.sleep(1)
    while True:
        
        message_display('Click Space to Begin',
                    30,WHITE,(display_width/2),(display_height/2+210))
        message_display('Click Space to Begin',
                    30,red,(display_width/2),(display_height/2+210))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    option()
        
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
             
        pygame.display.update()
        clock.tick(15)
def option():
    global musics
    musics=True
    screen.fill(BLACK)
    regNo = 0
    clicked=False
    onoff='on'
    while True:
        if regNo<0:
            regNo=4
        if regNo>4:
            regNo=1
        message_display('Snake Game',
                    80,red,(330),(100))
        mouse = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quite()
                quit()
            if event.type==pygame.KEYDOWN:
                
                if event.key==pygame.K_UP:
                    regNo-=1
                if event.key==pygame.K_DOWN:
                    regNo+=1
                if event.key==pygame.K_KP_ENTER:
                    clicked=True
                    if musics==True:
                        musics=False
                    else:
                        musics=True
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_KP_ENTER:
                    clicked = False
                    
        
        click = pygame.mouse.get_pressed()
        
        if (250 < mouse[0] <250 + 300 and 200 < mouse[1] < 250) or regNo==1:
            pygame.draw.rect(screen, bright_black,(250,200,300,50))
            message_display('Classic Mode',30,WHITE,(360),(220))
            if click[0]==1 or clicked==True:
                gameloopclass()
        else:
            pygame.draw.rect(screen, BLACK,(250,200,300,50))
            message_display('Classic Mode',30,WHITE,(360),(220))
        if (250 < mouse[0] <250 + 300 and 270< mouse[1] <320) or regNo==2:
            pygame.draw.rect(screen, bright_black,(250,270,300,50))
            message_display('Standard Mode',30,WHITE,(360),(290))
            if click[0]==1 or clicked==True:
                gameloop()
        else:
            pygame.draw.rect(screen, BLACK,(250,270,300,50))
            message_display('Standard Mode',30,WHITE,(360),(290))
        
        if (250 < mouse[0] <250 + 300 and 340< mouse[1] <390) or regNo==3:
            pygame.draw.rect(screen, bright_black,(250,340,300,50))
            message_display('Sound '+str(onoff),30,WHITE,(360),(360))
            if click[0]==1 or clicked==True:
                if musics==True:
                    pygame.mixer.music.unpause()
                    onoff='on'
                elif musics==False:
                    pygame.mixer.music.pause()
                    onoff='off'
        else:
            pygame.draw.rect(screen, BLACK,(250,340,300,50))
            message_display('Sound '+str(onoff),30,WHITE,(360),(360))
        if (250 < mouse[0] <250 + 300 and 410< mouse[1] <460) or regNo==4:
            pygame.draw.rect(screen, bright_black,(250,410,300,50))
            message_display('Quit',30,WHITE,(360),(430))
            if click[0]==1 or clicked==True:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(screen, BLACK,(250,410,300,50))
            message_display('Quit',30,WHITE,(360),(430))
    
                
        pygame.display.update()
        clock.tick(10)          
            
def countdown():
    pygame.mixer.music.stop()
    if count== True:
        for i in range(3,0,-1):
            screen.fill(BLACK)
            message_display(str(i),60,WHITE,(display_width/2),(display_height/2))
            #screen.blit(wallImg,(0,0))
            #screen.blit(bgrImg,(20,20))
            time.sleep(1)
        pygame.display.update()
        clock.tick(5)
def gameloop():
    #pygame.mixer.music.play(2)
    s=0
    speed=5
    score=0
    k=1
    pygame.display.update()
    segment_width = 19
    segment_height = 19

    segment_margin = 1
    x_change = segment_width + segment_margin
    y_change = 0
    thingx=0
    thingy=0
    x1=random.randint(1,38)
    y1=random.randint(1,28)
        
    thingx=x1*20
    thingy=y1*20
    
    global pause,count, typeName
    count=True
    typeName='highscore'
    allspriteslist = pygame.sprite.Group()
    snake_segments = []
    
    class Segment(pygame.sprite.Sprite):
        """ Class to represent one segment of the snake. """
        # -- Methods
        # Constructor function
        def __init__(self, x, y):
            # Call the parent's constructor
            super().__init__()
     
            # Set height, width
            self.image = pygame.Surface([segment_width, segment_height])
            self.image.fill(WHITE)
            #self.image=pygame.transform.scale(snakeImg2,(19,19))

            # Make our top-left corner the passed-in location.
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
      
    for i in range(4):
        x = 100 - (segment_width + segment_margin) * i
        y = 300
        
        
        segment = Segment(x, y)
        
        snake_segments.append(segment)
        allspriteslist.add(segment)
    
    n=0    
    done = False

    while True:
        
        
        countdown()
        count=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            # Set the speed based on the key pressed
            # We want the speed to be enough that we move a full
            # segment, plus the margin.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and k!=1:
                    k=0
                if event.key == pygame.K_RIGHT and k!=0:
                    
                    k=1
                if event.key == pygame.K_UP and k!=3:
                    
                    k=2
                if event.key == pygame.K_DOWN and k!=2:
                    
                    k=3
                if event.key==pygame.K_SPACE:
                    s=1
                if event.key==pygame.K_ESCAPE:
                    pause=True
                    paused()
            
        if k==0:
            x_change = (segment_width + segment_margin) * -1
            y_change = 0
        if k==1:
            x_change = (segment_width + segment_margin)
            y_change = 0
        if k==2:
            x_change = 0
            y_change = (segment_height + segment_margin) * -1
        if k==3:
            x_change = 0
            y_change = (segment_height + segment_margin)
        # Get rid of last segment of the snake
        # .pop() command removes last item in list
        length=len(snake_segments)
        
        old_segment = snake_segments.pop()
        allspriteslist.remove(old_segment)
     
        # Figure out where new segment will be
        x = snake_segments[0].rect.x + x_change
        y = snake_segments[0].rect.y + y_change
        
        segment = Segment(x, y)
        
        # Insert new segment into the list
        snake_segments.insert(0, segment)
        allspriteslist.add(segment)
        
        # -- Draw everything
        # Clear screen
        
        screen.blit(wallImg,(0,0))
        pygame.draw.rect(screen, BLACK,(20,20, 760, 560))
        #screen.blit(bgrImg,(20,20))
        
        allspriteslist.draw(screen)
        
        #print(length)
        if thingx==x and thingy==y:
            x1=random.randint(1,38)
            y1=random.randint(1,28)
        
            thingx=x1*20
            thingy=y1*20
            x2 = snake_segments[length-1].rect.x + x_change
            y2 = snake_segments[length-1].rect.y + y_change
            segment = Segment(x2, y2)
            snake_segments.insert(length, segment)
            allspriteslist.add(segment)
            for coord in snake_segments[1:]:
                x3=coord.rect.x
                y3=coord.rect.y
                if x3==thingx and y3==thingy:
                    x1=random.randint(1,38)
                    y1=random.randint(1,28)
                    thingx=x1*20
                    thingy=y1*20
                    #print('hi')
            thingx=x1*20
            thingy=y1*20
            speed=speed+0.4
            score=score+1
            if musics==True:
                eat.play()
            elif musics==True:
                continue
                
            
        for coord in snake_segments[1:]:
            x3=coord.rect.x
            y3=coord.rect.y
            
            if x3==x and y3==y:
                crash(score)
                
        if x<=0 or y <=0 or x>=780 or y>=580:
            crash(score)
            
            
        
        apples(thingx,thingy)
        carscore(score)
        n=n+1
        pygame.display.update()
        clock.tick(speed)
def gameloopclass():
    #pygame.mixer.music.play(2)
    s=0
    speed=5
    score=0
    k=1
    pygame.display.update()
    segment_width = 19
    segment_height = 19

    segment_margin = 1
    x_change = segment_width + segment_margin
    y_change = 0
    thingx=0
    thingy=0
    x1=random.randint(1,38)
    y1=random.randint(1,28)
        
    thingx=x1*20
    thingy=y1*20
    
    global pause,count, typeName
    count=True
    typeName='highscoreClass'
    allspriteslist = pygame.sprite.Group()
    snake_segments = []
    
    class Segment(pygame.sprite.Sprite):
        """ Class to represent one segment of the snake. """
        # -- Methods
        # Constructor function
        def __init__(self, x, y):
            # Call the parent's constructor
            super().__init__()
     
            # Set height, width
            self.image = pygame.Surface([segment_width, segment_height])
            self.image.fill(WHITE)
            #self.image=pygame.transform.scale(snakeImg2,(19,19))

            # Make our top-left corner the passed-in location.
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
      
    for i in range(4):
        x = 100 - (segment_width + segment_margin) * i
        y = 300
        
        
        segment = Segment(x, y)
        
        snake_segments.append(segment)
        allspriteslist.add(segment)
    
    n=0    
    done = False

    while True:
        
        
        countdown()
        count=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            # Set the speed based on the key pressed
            # We want the speed to be enough that we move a full
            # segment, plus the margin.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and k!=1:
                    k=0
                if event.key == pygame.K_RIGHT and k!=0:
                    
                    k=1
                if event.key == pygame.K_UP and k!=3:
                    
                    k=2
                if event.key == pygame.K_DOWN and k!=2:
                    
                    k=3
                if event.key==pygame.K_SPACE:
                    s=1
                if event.key==pygame.K_ESCAPE:
                    pause=True
                    paused()
        a=snake_segments[0].rect.x
        b=snake_segments[0].rect.y
        
        if k==0:
            x_change = (segment_width + segment_margin) * -1
            y_change = 0
            if a==0:
                a=800
        if k==1:
            x_change = (segment_width + segment_margin)
            y_change = 0
            if a==780:
                a=-20
        if k==2:
            x_change = 0
            y_change = (segment_height + segment_margin) * -1
            if b==0:
                b=600
        if k==3:
            x_change = 0
            y_change = (segment_height + segment_margin)
            if b==580:
                b=-20
        # Get rid of last segment of the snake
        # .pop() command removes last item in list
        length=len(snake_segments)
        
        
        
        
        old_segment = snake_segments.pop()
        allspriteslist.remove(old_segment)

        
        
        # Figure out where new segment will be
        x = a + x_change
        y = b + y_change
        segment = Segment(x, y)
        
        # Insert new segment into the list
        snake_segments.insert(0, segment)
        allspriteslist.add(segment)
        
        # -- Draw everything
        # Clear screen
        screen.fill(BLACK)
        
        allspriteslist.draw(screen)
        
        #print(length)
        if thingx==x and thingy==y:
            x1=random.randint(0,39)
            y1=random.randint(0,29)
        
            thingx=x1*20
            thingy=y1*20
            x2 = snake_segments[length-1].rect.x + x_change
            y2 = snake_segments[length-1].rect.y + y_change
            segment = Segment(x2, y2)
            snake_segments.insert(length, segment)
            allspriteslist.add(segment)
            for coord in snake_segments[1:]:
                x3=coord.rect.x
                y3=coord.rect.y
                if x3==thingx and y3==thingy:
                    x1=random.randint(1,38)
                    y1=random.randint(1,28)
                    thingx=x1*20
                    thingy=y1*20
                    #print('hi')
            thingx=x1*20
            thingy=y1*20
            speed=speed+0.4
            score=score+1
            if musics==True:
                eat.play()
        #print(x,y)   
            
        for coord in snake_segments[1:]:
            x3=coord.rect.x
            y3=coord.rect.y
            
            if x3==x and y3==y:
                crash(score)
                
        
        
            
            
        
        apples(thingx,thingy)
        carscore(score)
        n=n+1
        pygame.display.update()
        clock.tick(speed)
intro()
gameloop()
pygame.quit()
quit()

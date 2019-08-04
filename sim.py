import pygame
import time
pygame.init()

Throttle = 0 #son Throttle
LastThrottle = 0
Yaw = 1500
Pitch = 1500
Roll = 1500
ErrorX = 0
ErrorY = 0
x = 208
y = 208
KpT = 0.01
KiT = 0
KdT = 0.01
I = 0
dt=0.1

font = pygame.font.Font('freesansbold.ttf', 10)
gameDisplay = pygame.display.set_mode((416,416))
pygame.display.set_caption('vayvay sim')
text = font.render('ErrorX:'+str(ErrorX)+' ErrorY:'+str(ErrorY)+' Throttle:'+str(Throttle)+' Yaw:'+str(Yaw)+' Pitch:'+str(Pitch)+' Roll:'+str(Roll), True, (0,255,255), (0,0,128))
textRect = text.get_rect()
textRect.center = (208,370)
white = (255,255,255)
clock = pygame.time.Clock()
crashed = False
droneImg = pygame.image.load('drone2.png')

def drone(x,y):
    gameDisplay.blit(droneImg, (x,y))



while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if the left button is pressed
            if event.button == 1:
                (x, y) = pygame.mouse.get_pos()
    gameDisplay.fill(white)
    gameDisplay.blit(text, textRect)
    pygame.draw.line(gameDisplay,(255,100,200),(208,0),(208,416))
    drone(x-90,y-45)
    pygame.draw.line(gameDisplay,(255,100,200),(0,208),(416,208))
    pygame.draw.line(gameDisplay,(100,255,50),(208,208),(x,y))
    #else:
    #   drone(((display_width * 0.5)-90),((display_height * 0.5)-45))
    ErrorX= x-208
    ErrorY= 208-y
    if(ErrorY > 1):
        oldErrorY = ErrorY
        P = KpT*ErrorY
        I = I + (KiT * ErrorY * dt)
        HataD = ErrorY-oldErrorY
        D = (KdT * HataD)/dt
        print(P+I+D)
        Throttle = LastThrottle+P+I+D
        if (Throttle>LastThrottle):
            it=(Throttle-LastThrottle)
            y=y+it
            LastThrottle = Throttle
            ErrorY = 208-y
    if (ErrorY<-1):
        oldErrorY = ErrorY
        P = KpT*ErrorY
        I = I + (KiT * ErrorY * dt)
        HataD = ErrorY-oldErrorY
        D = (KdT * HataD)/dt
        print(P+I+D)
        Throttle = LastThrottle-abs(P+I+D)
        if (Throttle<LastThrottle):
            it=(LastThrottle-Throttle)
            y=y-it
            LastThrottle = Throttle
            ErrorY = 208-y
    if(ErrorX>1):
        oldErrorX = ErrorX
        P = KpT*ErrorX
        I = I + (KiT * ErrorX * dt)
        HataD = ErrorX-oldErrorX
        D = (KdT * HataD)/dt
        print(P+I+D)
        Yaw = Yaw+abs(P+I+D)
        if (Yaw!=1500):
            iy=(Yaw-1500)
            x=x-iy
            Yaw=1500
    if(ErrorX<1):
        oldErrorX = ErrorX
        P = KpT*ErrorX
        I = I + (KiT * ErrorX * dt)
        HataD = ErrorX-oldErrorX
        D = (KdT * HataD)/dt
        print(P+I+D)
        Yaw = Yaw+abs(P+I+D)
        if (Yaw!=1500):
            iy=(Yaw-1500)
            x=x+iy
            Yaw=1500
    '''
    if (Roll!=1500):
        ir=(Roll-1500)/10
        drone(x+ir,y)
        Roll=1500
    if (Pitch!=1500):
        ip=Pitch-1500
        drone(x,y)
        Pitch=1500
    '''
    text = font.render('ErrorX:'+str(int(round(ErrorX)))+' ErrorY:'+str(int(round(ErrorY)))+' Throttle:'+str(int(round(Throttle)))+' Yaw:'+str(int(round(Yaw)))+' Pitch:'+str(Pitch)+' Roll:'+str(Roll), True, (0,255,255), (0,0,128))
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
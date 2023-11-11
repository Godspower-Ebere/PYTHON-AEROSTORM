import pygame
import time
import random
import pickle
import math
from pygame.locals import *
import numpy as np
pygame.init()
size=width,height=(1000,800)
screen=pygame.display.set_mode(size)
def game():
    pygame.init()
    pygame.font.init()
    global bg1
    global highscore
    global killnumber
    global sec
    read=open("asset/high.score","rb")
    highscore=pickle.load(read)
    bc=0
    image=[pygame.transform.scale(pygame.image.load("asset/Animation/1.png"),(200,200)),
           pygame.transform.scale(pygame.image.load("asset/Animation/2.png"),(200,200)),
           pygame.transform.scale(pygame.image.load("asset/Animation/3.png"),(200,200))
           ]
    ene1=[pygame.transform.scale(pygame.transform.flip(pygame.image.load("asset/e1/1.png"),False,True),(200,200)),
         pygame.transform.scale(pygame.transform.flip(pygame.image.load("asset/e1/2.png"),False,True),(200,200)),
         pygame.transform.scale(pygame.transform.flip(pygame.image.load("asset/e1/3.png"),False,True),(200,200))
         ]
    ene2=[pygame.transform.scale(pygame.transform.flip(pygame.image.load("asset/e2/1.png"),False,True),(200,200)),
         pygame.transform.scale(pygame.transform.flip(pygame.image.load("asset/e2/2.png"),False,True),(200,200)),
         pygame.transform.scale(pygame.transform.flip(pygame.image.load("asset/e2/3.png"),False,True),(200,200))
         ]
    ene3=[pygame.transform.scale(pygame.transform.flip(pygame.image.load("asset/e3/1.png"),False,True),(200,200)),
         pygame.transform.scale(pygame.transform.flip(pygame.image.load("asset/e3/2.png"),False,True),(200,200)),
         pygame.transform.scale(pygame.transform.flip(pygame.image.load("asset/e3/3.png"),False,True),(200,200))
         ]
    blow=[
        pygame.transform.scale(pygame.image.load("asset/blow/Explosion_1.png"),(200,200)),
        pygame.transform.scale(pygame.image.load("asset/blow/Explosion_2.png"),(200,200)),
        pygame.transform.scale(pygame.image.load("asset/blow/Explosion_3.png"),(200,200)),
        pygame.transform.scale(pygame.image.load("asset/blow/Explosion_4.png"),(200,200)),
        pygame.transform.scale(pygame.image.load("asset/blow/Explosion_5.png"),(200,200)),
        pygame.transform.scale(pygame.image.load("asset/blow/Explosion_6.png"),(200,200)),
        pygame.transform.scale(pygame.image.load("asset/blow/Explosion_7.png"),(200,200)),
        pygame.transform.scale(pygame.image.load("asset/blow/Explosion_8.png"),(200,200)),
        pygame.transform.scale(pygame.image.load("asset/blow/Explosion_9.png"),(200,200)),
        pygame.transform.scale(pygame.image.load("asset/blow/Explosion_10.png"),(200,200))
        ]
    blife=0
    bcount=0
    bx,by=-50,0
    bx2,by2=-50,-height
    px,py=(width/2)-100,600
    bg1=pygame.transform.scale(pygame.image.load("asset/bg/bg.png"),(width+100,height))
    bg2=bg1
    scorefont=pygame.font.SysFont("Tahoma",50,True)
    pygame.mixer.music.load("asset/sound/bgm.mp3")
    pygame.mixer.music.play(-1)
    pshot=pygame.mixer.Sound("asset/sound/pgun.wav")
    powerup=pygame.mixer.Sound("asset/sound/life.wav")
    explo=pygame.mixer.Sound("asset/sound/explo.wav")
    touch=pygame.mixer.Sound("asset/sound/touch.wav")
    powerup=pygame.mixer.Sound("asset/sound/powerup.wav")
    eneshot=pygame.mixer.Sound("asset/sound/eneshot.wav")
    eneshot2=pygame.mixer.Sound("asset/sound/eneshot2.wav")
    eneshot3=pygame.mixer.Sound("asset/sound/eneshot3.wav")

    pauses=pygame.transform.scale(pygame.image.load("asset/menu/pause.png"),(100,50))
    pauser=pauses.get_rect()
    pauser.center=width-(pauses.get_width()/2),30

    killed=pygame.transform.scale(pygame.image.load("asset/menu/killed.png"),(100,50))
    killedr=killed.get_rect()
    killedr.center=width-(killed.get_width()/2),600
    killnumber=0

    scoreimg=pygame.transform.scale(pygame.image.load("asset/menu/socre.png"),(100,50))
    scoreimgr=pauses.get_rect()
    scoreimgr.x=10
    scoreimgr.y=10

    extrahealth=pygame.image.load("asset/weapon/life.png")
    bomb=pygame.image.load("asset/weapon/bomb.png")
    enemybullet2=pygame.transform.scale(pygame.transform.rotate(pygame.image.load("asset/weapon/shot1.png"),90),(40,40))
    enemybullet=pygame.transform.scale(pygame.transform.rotate(pygame.image.load("asset/weapon/shot.png"),270),(40,40))
    lx,ly=random.randint(0,800),random.randint(-200,-100)
     
    e1p=[10,200,400,600,800]
    e1py=[-100,-200,-400,-600,-800]

    e2p=[10,300,500,700,800]
    e2py=[-250,-300,-500,-700,-800]

    e3p=[10,150,300,450,700]
    e3py=[-90,-280,-480,-560,-700]

    e1x,e1y=random.choice(e1p),random.choice(e1py)
    e2x,e2y=random.choice(e2p),random.choice(e2py)
    e3x,e3y=random.choice(e3p),random.choice(e3py)

    health1=200
    health2=200
    health3=200
    phealth=200
    count=0

    vel=5
    shift=50
    minimum=100
    reload=0.5
    enereload=5
    level=0

    show1=0
    show2=0
    show3=0

    die1=False
    die2=False
    die3=False

    c1=0
    c2=0
    c3=0

    r1=[]
    r2=[]
    r3=[]

    r1.append([e1x,e1y,health1])
    r2.append([e2x,e2y,health2])
    r3.append([e3x,e3y,health3])

    num1=6
    num2=8
    num3=10

    enelife=200

    now=time.time()
    t=time.time()
    t2=time.time()
    t3=time.time()

    ene1b=time.time()
    ene2b=time.time()
    ene3b=time.time()

    enebull1=[]
    enebull1.append([e1x,e1y])

    enebull2=[]
    enebull2.append([e2x,e2y])

    enebull3=[]
    enebull3.append([e3x,e3y])

    bullet=[]
    bullet2=[]

    bul2=False
    bul1=False

    bull=pygame.image.load("asset/weapon/bullet.png")

    onebull=pygame.transform.flip(bull,False,True)
    twobull=pygame.image.load("asset/weapon/twobullet.png")

    s1=pygame.transform.flip(bull,False,True)
    s2=pygame.image.load("asset/weapon/twobullet.png")
    
    turret=pygame.transform.scale(pygame.transform.flip(pygame.image.load("asset/weapon/turret.png"),False,True),(50,70))
    
    

    s1r=s1.get_rect()
    s1r.center=width-8,385

    s2r=s2.get_rect()
    s2r.center=width-30,385

    twox=random.randint(10,900)
    twoy=random.randint(-800,-100)
    onex=random.randint(10,900)
    oney=random.randint(-800,-100)

    twobullr=pygame.Rect(twox,twoy,64,32)
    onebullr=pygame.Rect(onex,oney,onebull.get_width(),onebull.get_height())
    lthan=False
    run=True
    addhealth=False
    showbull=False
    back=False
    score=0
    bgvel=4
    clock=pygame.time.Clock()
    
    secound=time.time()
    ###################### CAPTION AND ICON
    pygame.display.set_caption("AEROSTORM")
    icon=[pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/1.png"),(50,100)),270)]
    pygame.display.set_icon(icon[0])
    mega=False
    ########################################################################################################################
    ########################################################################################################################
    while run:
        r1=[]
        r2=[]
        r3=[]
        b1len=len(bullet)
        b2len=len(bullet2)
        sf=scorefont.render(f" :{score}",1,((255,255,255)))
        killscore=scorefont.render(f"{killnumber}",1,((255,255,255)),((255,0,0)))
        sec=int(time.time()-secound)
        sectime=scorefont.render(f"{sec}s",1,((255,255,255)))
        level+=1
        if score > highscore:
            highs=open("asset/high.score","wb")
            pickle.dump(score,highs)
        if level>=200:
            enereload-=0.1
            num1-=0.1
            num2-=0.1
            num3-=0.1
            level=0
            enelife-=2
            vel+=0.1
            reload-=0.001
            bgvel+=0.1
        if enereload<=0.6:
            enereload=0.6
        if reload<=0.2:
            reload=0.2
        if num1<=3:
            num1=3
        if num2<=5:
            num2=5
        if num3<=7:
            num1=7
        if enelife<=50:
            enelife=50
        if vel>=10:
            vel=10
        if bgvel>=7:
            bgvel=7
        
            
        powerup.set_volume(0.3)
        pshot.set_volume(0.3)
        eneshot.set_volume(0.3)
        eneshot2.set_volume(0.3)
        eneshot3.set_volume(0.3)
        
        ########## BATTERY PERCENT
        percent=int(phealth/200*100/1)
        prect=pygame.Rect(px,py+50,200,100)
        
        
        fps=clock.tick(100)
        e1y+=1
        start=time.time()-now
        start2=time.time()-now
        
        t1=time.time()-t
        t12=time.time()-t2
        t13=time.time()-t3
        if score>=600:
            mega=True
        
        by+=bgvel
        by2+=bgvel
        if by>=height:
            by=-height
        if by2>=height:
            by2=-height
        count+=0.2
        if count>=3:
            count=0
        plane=image[int(count)]
        e1=ene1[int(count)]
        e2=ene2[int(count)]
        e3=ene3[int(count)]
        e1r=pygame.Rect(e1x,e1y,200,200)

        bcount+=0.5
        if bcount>=10:
            bcount=0
        fire=blow[int(bcount)]
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sure2()
        ### KEY PRESS CHECK
        key=pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            if start >=reload:
                blife-=5
                bullet.append([px,py])
                bullet2.append([px,py])
                now=time.time()
                start=time.time()-now
                if bul1 or bul2:
                    pshot.play()
        if key[pygame.K_RIGHT]:
            px+=vel
        if key[pygame.K_LEFT]:
            px-=vel
        if key[pygame.K_p]:
            pause(screen)
        if key[pygame.K_d]:
            blife=0
        if py <=0:
            py=0
        if py>=height-200:
            py=height-200
        if px>=width-200:
            px=width-200
        if px<=0:
            px=0
        if mega:
            num1=3
            num2=3
            num3=3
            enereload=0.4
            if start >=reload-0.05:
                    blife-=5
                    if bul1 or bul2:
                        pshot.play()
                    bullet.append([px,py])
                    bullet2.append([px,py])
                    now=time.time()
                    start=time.time()-now
        screen.blit(bg1,(bx,by))
        screen.blit(bg2,(bx2,by2))
        
    ######## PLAYER BULLET COLLISION CHECK
        if bul1:
            for shots in bullet:
                brect=pygame.Rect(shots[0]+85,shots[1]+50,bull.get_width(),bull.get_height())
                shots[1]-=vel
                screen.blit(bull, (shots[0]+85,shots[1]+50))
                if shots[1]<=-height:
                    bullet.pop(bullet.index(shots))
                for i in r1:
                    ene1rect=pygame.Rect(i[0],i[1]+50,e1.get_width(),e1.get_height()-80)
                    if ene1rect.colliderect(brect):
                        touch.play()
                        screen.blit(blow[4], (ene1rect.x,ene1rect.y))
                        if shots in bullet:
                            bullet.pop(bullet.index(shots))
                            i[2]-=enelife
                for i in r2:
                    ene2rect=pygame.Rect(i[0],i[1]+50,e2.get_width(),e2.get_height()-80)
                    if ene2rect.colliderect(brect):
                        touch.play()
                        screen.blit(blow[4], (ene2rect.x,ene2rect.y))
                        if shots in bullet:
                            bullet.pop(bullet.index(shots))
                            i[2]-=enelife
                for i in r3:
                    ene3rect=pygame.Rect(i[0],i[1]+50,e3.get_width(),e3.get_height()-80)
                    if ene3rect.colliderect(brect):
                        touch.play()
                        screen.blit(blow[4], (ene3rect.x,ene3rect.y))
                        if shots in bullet:
                            bullet.pop(bullet.index(shots))
                            i[2]-=enelife
                ######    BULLET VS BULLET COLLISION ##################
                for b in enebull1:
                    b1r=pygame.Rect(b[0]+85,b[1]+150,bull.get_width(),bull.get_height())
                    ##COLLIDE
                    if b1r.colliderect(brect):
                        enebull1.pop(enebull1.index(b))
                        if shots in bullet:
                            bullet.pop(bullet.index(shots))
                for b in enebull2:
                    b2r=pygame.Rect(b[0]+85,b[1]+150,bull.get_width(),bull.get_height())
                    ##COLLIDE
                    if b2r.colliderect(brect):
                        enebull2.pop(enebull2.index(b))
                        if shots in bullet:
                            bullet.pop(bullet.index(shots))
                for b in enebull3:
                    b3r=pygame.Rect(b[0]+85,b[1]+150,bull.get_width(),bull.get_height())
                    ##COLLIDE
                    if b3r.colliderect(brect):
                        enebull3.pop(enebull3.index(b))
                        if shots in bullet:
                            bullet.pop(bullet.index(shots))
        ########################################## BULLET 2222
        if bul2:
            for shots2 in bullet2:
                brect=pygame.Rect(shots2[0]+85,shots2[1]+100,bull.get_width(),bull.get_height())
                shots2[1]-=vel
                if shots2[1]<=-height:
                    bullet2.pop(bullet2.index(shots2))
                screen.blit(bull, (shots2[0]+85,shots2[1]+100))
                
                for i in r1:
                    ene1rect=pygame.Rect(i[0],i[1]+50,e1.get_width(),e1.get_height()-80)
                    if ene1rect.colliderect(brect):
                        touch.play()
                        screen.blit(blow[4], (ene1rect.x,ene1rect.y))
                        if shots2 in bullet2:
                            bullet2.pop(bullet2.index(shots2))
                            i[2]-=enelife
                for i in r2:
                    ene2rect=pygame.Rect(i[0],i[1]+50,e2.get_width(),e2.get_height()-80)
                    if ene2rect.colliderect(brect):
                        touch.play()
                        screen.blit(blow[4], (ene2rect.x,ene2rect.y))
                        if shots2 in bullet2:
                            bullet2.pop(bullet2.index(shots2))
                            i[2]-=enelife
                for i in r3:
                    ene3rect=pygame.Rect(i[0],i[1]+50,e3.get_width(),e3.get_height()-80)
                    if ene3rect.colliderect(brect):
                        touch.play()
                        screen.blit(blow[4], (ene3rect.x,ene3rect.y))
                        if shots2 in bullet2:
                            bullet2.pop(bullet2.index(shots2))
                            i[2]-=enelife
                ######    BULLET VS BULLET COLLISION ##################
                for b in enebull1:
                    b1r=pygame.Rect(b[0]+85,b[1]+150,bull.get_width(),bull.get_height())
                    ##COLLIDE
                    if b1r.colliderect(brect):
                        enebull1.pop(enebull1.index(b))
                        if shots2 in bullet2:
                            bullet2.pop(bullet2.index(shots2))
                for b in enebull2:
                    b2r=pygame.Rect(b[0]+85,b[1]+150,bull.get_width(),bull.get_height())
                    ##COLLIDE
                    if b2r.colliderect(brect):
                        enebull2.pop(enebull2.index(b))
                        if shots2 in bullet2:
                            bullet2.pop(bullet2.index(shots2))
                for b in enebull3:
                    b3r=pygame.Rect(b[0]+85,b[1]+150,bull.get_width(),bull.get_height())
                    ##COLLIDE
                    if b3r.colliderect(brect):
                        enebull3.pop(enebull3.index(b))
                        if shots2 in bullet2:
                            bullet2.pop(bullet2.index(shots2))
                    
    #################### ENDS HERE HERE HERE          ##############################      
        if t1>=num1:
            e1x=random.choice(e1p)
            e1y=random.choice(e1py)
            r1.append([e1x,e1y,health1])
            t=time.time()
            t1=time.time()-t
            
        if t12>=num1:
            e2x=random.choice(e2p)
            e2y=random.choice(e2py)
            r2.append([e2x,e2y,health2])
            t2=time.time()
            t12=time.time()-t
            
        if t13>=num1:
            e3x=random.choice(e3p)
            e3y=random.choice(e3py)
            r3.append([e3x,e3y,health3])
            t3=time.time()
            t13=time.time()-t
            
        for i in r1:
            ene1rect=pygame.Rect(i[0],i[1],e1.get_width(),e1.get_height())
            i[1]+=vel-2
            if i[1]>=height+300:
                i[1]=random.randint(-800,-400)
                i[0]=random.randint(10,800)
            ###    collide check with playyyyer
            if ene1rect.colliderect(prect):
                    bc+=1
                    ################   vibrate
                    if bc==5:
                        bx+=50
                        bx2+=50
                    if bc==10:
                        bx-=50
                        bx2-=50
                    if bc==15:
                        bx+=50
                        bx2+=50
                    if bc==20:
                        bx-=50
                        bx2-=50
                        explo.play()
                        bc=0
                    addhealth=False
                    phealth-=1
            screen.blit(e1,(i[0],i[1]))
            pygame.draw.rect(screen,((255,0,0)),(i[0],i[1]+40,200,10),0,10,10,10,10)
            pygame.draw.rect(screen,((0,255,0)),(i[0],i[1]+40,i[2],10),0,10,10,10,10)
            ###  BULLET SHOOTING
            bt1=time.time()-ene1b
            if bt1 >=enereload:
                if i[1]+300>0:
                    eneshot.play()
                enebull1.append([i[0],i[1]])
                ene1b=time.time()
                bt1=time.time()-ene1b
        for b in enebull1:
            b[1]+=vel
            b1r=pygame.Rect(b[0]+85,b[1]+150,bull.get_width(),bull.get_height())
            ##COLLIDE
            if b1r.colliderect(prect):
                show1+=1
                if phealth<=minimum:
                    py+=shift
                addhealth=False
                phealth-=vel
                enebull1.pop(enebull1.index(b))
            ###BOMB
            screen.blit(enemybullet, (b1r[0],b1r[1]))
            if b[1]>= height+40:
                enebull1.pop(enebull1.index(b))
        if show1 >0:
            screen.blit(blow[4], (b1r.x-90,b1r.y-100))
            show1=0
                
        for i in r2:
            ene2rect=pygame.Rect(i[0],i[1],e2.get_width(),e2.get_height())
            i[1]+=vel-2
            if i[1]>=height+300:
                i[1]=random.randint(-800,-400)
                i[0]=random.randint(10,800)
            ###    collide check with playyyyer
            if ene2rect.colliderect(prect):
                    bc+=1
                    ################   vibrate
                    if bc==5:
                        bx+=50
                        bx2+=50
                    if bc==10:
                        bx-=50
                        bx2-=50
                    if bc==15:
                        bx+=50
                        bx2+=50
                    if bc==20:
                        bx-=50
                        bx2-=50
                        explo.play()
                        bc=0
                    addhealth=False
                    phealth-=1
            screen.blit(e2,(i[0],i[1]))
            pygame.draw.rect(screen,((255,0,0)),(i[0],i[1]+40,200,10),0,10,10,10,10)
            pygame.draw.rect(screen,((0,255,0)),(i[0],i[1]+40,i[2],10),0,10,10,10,10)
            ###  BULLET SHOOTING
            bt2=time.time()-ene2b
            if bt2 >=enereload:
                if i[1]+300>0:
                    eneshot2.play()
                enebull2.append([i[0],i[1]])
                ene2b=time.time()
                bt2=time.time()-ene2b
        for b in enebull2:
            b[1]+=vel
            b2r=pygame.Rect(b[0]+85,b[1]+150,bull.get_width(),bull.get_height())
            ##COLLIDE
            if b2r.colliderect(prect):
                show2+=1
                if phealth<=minimum:
                    py+=shift
                addhealth=False
                phealth-=vel
                enebull2.pop(enebull2.index(b))
            ###BOMB
            screen.blit(bomb, (b2r[0],b2r[1]))
            if b[1]>= height+40:
                enebull2.pop(enebull2.index(b))
        if show2 >0:
            screen.blit(blow[4], (b2r.x-90,b2r.y-100))
            show2=0
        for i in r3:
            ene3rect=pygame.Rect(i[0],i[1],e3.get_width(),e3.get_height())
            i[1]+=vel-2
            if i[1]>=height+300:
                i[1]=random.randint(-800,-400)
                i[0]=random.randint(10,800)
             ###    collide check with playyyyer
            if ene3rect.colliderect(prect):
                    bc+=1
                    ################   vibrate
                    if bc==5:
                        bx+=50
                        bx2+=50
                    if bc==10:
                        bx-=50
                        bx2-=50
                    if bc==15:
                        bx+=50
                        bx2+=50
                    if bc==20:
                        bx-=50
                        bx2-=50
                        explo.play()
                        bc=0
                    addhealth=False
                    phealth-=1
            screen.blit(e3,(i[0],i[1]))
            pygame.draw.rect(screen,((255,0,0)),(i[0],i[1]+40,200,10),0,10,10,10,10)
            pygame.draw.rect(screen,((0,255,0)),(i[0],i[1]+40,i[2],10),0,10,10,10,10)
            bt3=time.time()-ene3b
            if bt3 >=enereload:
                if i[1]+300>0:
                    eneshot3.play()
                enebull3.append([i[0],i[1]])
                ene3b=time.time()
                bt3=time.time()-ene3b
        for b in enebull3:
            b[1]+=vel
            b3r=pygame.Rect(b[0]+85,b[1]+150,bull.get_width(),bull.get_height())
            ##COLLIDE
            if b3r.colliderect(prect):
                show3+=1
                if phealth<=minimum:
                    py+=shift
                addhealth=False
                phealth-=vel
                enebull3.pop(enebull3.index(b))
            ###BOMB
            screen.blit(enemybullet2, (b3r[0],b3r[1]))
            if b[1]>= height+40:
                enebull3.pop(enebull3.index(b))
        if show3 >0:
            screen.blit(blow[4], (b3r.x-90,b3r.y-100))
            show3=0
        ##################################  PLAYER DEATH ########################################
        if phealth<=0:
            time.sleep(2)
            gameover()
        if phealth<=minimum:
            if key[pygame.K_UP]:
                py-=vel
            if key[pygame.K_DOWN]:
                py+=vel
            screen.blit(extrahealth,(lx,ly))
            lrect=pygame.Rect(lx,ly,extrahealth.get_width(),extrahealth.get_height())
            if prect.colliderect(lrect):
                ly=random.randint(-200,-100)
                powerup.play()
                addhealth=True
            ly+=vel-3
            if ly>height+20:
                lx,ly=random.randint(0,800),random.randint(-200,-100)
        if addhealth:
            py+=vel
            if py>=600:
                py=600
            phealth+=1
            if phealth>=200:
                addhealth=False
        ####   ENEMY     DIE
        for i in r1:
            if i[2]<=0:
                i[2]=0
                die1=True
                bc+=1
                ################   vibrate
                if bc==5:
                    bx+=50
                    bx2+=50
                if bc==10:
                    bx-=50
                    bx2-=50
                if bc==15:
                    bx+=50
                    bx2+=50
                if bc==20:
                    bx-=50
                    bx2-=50
                    bc=0
            if die1:
                screen.blit(fire, (i[0],i[1]))
                c1+=0.5
                if c1<0.6:
                    explo.play()
                if c1>=10:
                    r1.pop(r1.index(i))
                    die1=False
                    score+=5
                    killnumber+=1
                    c1=0
        ####  ENEMY      DIE
        for i in r2:
            if i[2]<=0:
                i[2]=0
                die2=True
                bc+=1
                ################   vibrate
                if bc==5:
                    bx+=50
                    bx2+=50
                if bc==10:
                    bx-=50
                    bx2-=50
                if bc==15:
                    bx+=50
                    bx2+=50
                if bc==20:
                    bx-=50
                    bx2-=50
                    bc=0
            if die2:
                screen.blit(fire, (i[0],i[1]))
                c2+=0.5
                if c2<0.6:
                    explo.play()
                if c2>=10:
                    r2.pop(r2.index(i))
                    die2=False
                    score+=5
                    killnumber+=1
                    c2=0
        ####  ENEMY      DIE
        for i in r3:
            if i[2]<=0:
                i[2]=0
                die3=True
                bc+=1
                ################   vibrate
                if bc==5:
                    bx+=50
                    bx2+=50
                if bc==10:
                    bx-=50
                    bx2-=50
                if bc==15:
                    bx+=50
                    bx2+=50
                if bc==20:
                    bx-=50
                    bx2-=50
                    bc=0
            if die3:
                screen.blit(fire, (i[0],i[1]))
                c3+=0.5
                if c3<0.6:
                    explo.play()
                if c3>=10:
                    r3.pop(r3.index(i))
                    die3=False
                    score+=5
                    killnumber+=1
                    c3=0
            
        mouse=pygame.mouse.get_pressed()
        moupos=pygame.mouse.get_pos()
        mx,my=moupos
        mouser=pygame.Rect(mx,my,20,20)
        ################################### MOUSE COLLISION ##########################
        if mouse[0]:
            if mouser.colliderect(pauser):
                pause(screen)
        if blife<=0:
            if key[pygame.K_UP]:
                py-=vel
            if key[pygame.K_DOWN]:
                py+=vel
            bul1=False
            bul2=False
            blife=0
            if random.randint(1,2)==1:
                onebullr.y+=vel-2
                if onebullr.y>=height:
                        onebullr.x=random.randint(10,900)
                        onebullr.y=random.randint(-800,-100)
                if onebullr.colliderect(prect):
                    powerup.play()
                    onebullr.x=random.randint(10,900)
                    onebullr.y=random.randint(-800,-100)
                    twobullr.x=random.randint(10,900)
                    twobullr.y=random.randint(-800,-100)
                    blife=200
                    bul1=True
                    bul2=False
                    back=True
                screen.blit(onebull,(onebullr.x,onebullr.y))
            elif random.randint(1,2)==2:
                twobullr.y+=vel-1
                if twobullr.y>=height:
                        twobullr.x=random.randint(10,900)
                        twobullr.y=random.randint(-800,-100)
                if twobullr.colliderect(prect):
                    powerup.play()
                    twobullr.x=random.randint(10,900)
                    twobullr.y=random.randint(-800,-100)
                    onebullr.x=random.randint(10,900)
                    onebullr.y=random.randint(-800,-100)
                    blife=200
                    bul2=True
                    bul1=True
                    back=True
                screen.blit(twobull,(twobullr.x,twobullr.y))
        if back==True:
            py+=vel
            if py>=600:
                back=False
        for i in r1:
            ene1rect=pygame.Rect(i[0],i[1],e1.get_width(),e1.get_height())
            for i in r2:
                ene2rect=pygame.Rect(i[0],i[1],e2.get_width(),e2.get_height())
                if ene1rect.colliderect(ene2rect):
                    if ene1rect.x<ene2rect.x:
                        ene1rect.right=ene2rect.left
                    else:
                        ene2rect.right=ene1rect.left
            for i in r3:
                ene3rect=pygame.Rect(i[0],i[1],e3.get_width(),e3.get_height())
                if ene1rect.colliderect(ene3rect):
                    if ene1rect.x<ene3rect.x:
                        ene1rect.right=ene3rect.left
                    else:
                        ene3rect.right=ene2rect.left
        for i in r2:
            ene2rect=pygame.Rect(i[0],i[1],e2.get_width(),e2.get_height())
            for i in r1:
                ene1rect=pygame.Rect(i[0],i[1],e1.get_width(),e1.get_height())
                if ene2rect.colliderect(ene1rect):
                    if ene2rect.x<ene1rect.x:
                        ene2rect.right=ene1rect.left
                    else:
                        ene1rect.right=ene2rect.left
            for i in r3:
                ene3rect=pygame.Rect(i[0],i[1],e3.get_width(),e3.get_height())
                if ene2rect.colliderect(ene3rect):
                    if ene2rect.x<ene3rect.x:
                        ene2rect.right=ene3rect.left
                    else:
                        ene3rect.right=ene2rect.left

        for i in r3:
            ene3rect=pygame.Rect(i[0],i[1],e3.get_width(),e3.get_height())
            for i in r1:
                ene1rect=pygame.Rect(i[0],i[1],e1.get_width(),e1.get_height())
                if ene3rect.colliderect(ene1rect):
                    if ene3rect.x<ene1rect.x:
                        ene3rect.right=ene1rect.left
                    else:
                        ene1rect.right=ene3rect.left
            for i in r2:
                ene2rect=pygame.Rect(i[0],i[1],e2.get_width(),e2.get_height())
                if ene3rect.colliderect(ene2rect):
                    
                    if ene3rect.x<ene2rect.x:
                        ene3rect.right=ene2rect.left
                    else:
                        ene2rect.right=ene3rect.left
        
        mousex,mousey=pygame.mouse.get_pos()
        
        angle=int(math.degrees(math.atan2(-(mousey-(px+100)),mousex-(py+50))))
        turretimg=pygame.transform.rotate(turret,angle-90)
        turretimgr=turretimg.get_rect(center=(px+100,py+50))
                
     ################################################################### BLITING TO SCREEN
        screen.blit(sf,(100,0))
        screen.blit(plane,(px,py))
        screen.blit(turretimg,turretimgr)
        screen.blit(pauses,pauser)
        screen.blit(killed,killedr)
        screen.blit(sectime,(10,90))
    
        screen.blit(scoreimg,scoreimgr)
        pygame.draw.rect(screen,((255,0,0)),(px,py+150,200,10),0,10,10,10,10)
        pygame.draw.rect(screen,((0,255,0)),(px,py+150,phealth,10),0,10,10,10,10)

        pygame.draw.rect(screen,((255,0,0)),(width-20,100,10,200),0,10,10,10,10)
        pygame.draw.rect(screen,((0,255,0)),(width-20,100,10,blife),0,10,10,10,10)

        pygame.draw.rect(screen,((255,0,0)),(width-20,400,10,100),0,10,10,10,10)
        pygame.draw.rect(screen,((0,255,0)),(width-20,400,10,b2len),0,10,10,10,10)

        pygame.draw.rect(screen,((255,0,0)),(width-50,400,10,100),0,10,10,10,10)
        pygame.draw.rect(screen,((0,255,0)),(width-50,400,10,b1len),0,10,10,10,10)

        screen.blit(s1,s1r)
        screen.blit(s2,s2r)
        screen.blit(killscore,(width-100,510))
        
        
        font(screen,"arial black",20,True,f"{percent} %",(255,255,0),True,px+110,py+80)
        pygame.display.update()
    pygame.quit()
########################################################################################################################################################################################
########################################################################################################################################################################################
########################################################################################################################################################################################
########################################################################################################################################################################################
########################################################################################################################################################################################
def sure2():
    pygame.init()
    pygame.font.init()
    sure=True
    pygame.display.set_caption("AEROSTORM")
    icon=[pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/1.png"),(50,100)),270)]
    pygame.display.set_icon(icon[0])
    imgs=pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height))
    while sure:
        screen.blit(imgs,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sure=False
        win=pygame.font.Font('asset/motter-tektura.ttf',100)
        mouses=pygame.mouse.get_pressed()
        mousespos=pygame.mouse.get_pos()
        
        sure1=win.render("WANT TO QUIT",True,(255,255,255))
        sure1rect=sure1.get_rect()
        sure1rect.x=width/2-sure1rect.width/2
        sure1rect.y=150
        screen.blit(sure1,(sure1rect.x,sure1rect.y))

        sure=win.render("ARE YOU SURE YOU",True,(255,255,255))
        surerect=sure.get_rect()
        surerect.x=width/2-surerect.width/2
        surerect.y=20
        screen.blit(sure,(surerect.x,surerect.y))

        win1=pygame.font.Font('asset/motter-tektura.ttf',70)
        yes=win1.render("YES",True,(255,255,255))
        yesr=yes.get_rect()
        yesr.x=width/2-yesr.width-150
        yesr.y=400
        pygame.draw.rect(screen,(0,0,0),yesr,0,10)
        screen.blit(yes,yesr)
        if mouses[0]:
            if yesr.collidepoint(mousespos):
                sure=False
                pygame.quit()
        pygame.init()
        pygame.font.init()
        no=win1.render("NO",1,(255,255,255))
        nor=no.get_rect()
        nor.x=width/2+yesr.width+100
        nor.y=400
        pygame.draw.rect(screen,(0,0,0),nor,0,10)
        screen.blit(no,nor)
        if mouses[0]:
            if nor.collidepoint(mousespos):
                sure=False
        pygame.display.update()
def menu1():
    pygame.init()
    bg1=pygame.transform.scale(pygame.image.load("asset/bg/darkbg.png"),(width+100,height))
    gmenu=pygame.transform.scale(pygame.image.load("asset/menu/menu.png"),(400,100))
    gmenur=gmenu.get_rect()
    gmenur.center=width/2,100
    splayer=pygame.transform.scale(pygame.image.load("asset/menu/singleplayer.png"),(300,100))
    splayerr=gmenu.get_rect()
    splayerr.center=width/2+50,300

    mplayer=pygame.transform.scale(pygame.image.load("asset/menu/multiplayer.png"),(300,100))
    mplayerr=gmenu.get_rect()
    mplayerr.center=width/2+50,500

    quitg=pygame.transform.scale(pygame.image.load("asset/menu/quit.png"),(300,100))
    quitgr=quitg.get_rect()
    quitgr.center=width/2,700
    pygame.display.set_caption("AEROSTORM")
    icon=[pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/1.png"),(50,100)),270)]
    pygame.display.set_icon(icon[0])
    menu1=True
    while menu1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                menu1=False
        mouse=pygame.mouse.get_pressed()
        moupos=pygame.mouse.get_pos()
        mx,my=moupos
        mouser=pygame.Rect(mx,my,20,20)
        if mouse[0]:
            if mouser.colliderect(splayerr):
                ready()
            if mouser.colliderect(mplayerr):
                username1()
            if mouser.colliderect(quitgr):
                sure2()
        screen.blit(bg1,(0,0))
        screen.blit(gmenu,gmenur)
        screen.blit(splayer,splayerr)
        screen.blit(mplayer,mplayerr)
        screen.blit(quitg,quitgr)
        pygame.display.update()
    pygame.quit()
def ready():
    pygame.init()
    pygame.font.init()
    menu=True
    if menu:
        count=0
        x=[]
        y=[]
        w=[]
        h=[]
        r=[]
        g=[]
        b=[]
        num=500
        for i in range(num):
            x.append(random.randint(0,width))
            y.append(random.randint(0,height))
            w.append(10)
            h.append(10)
            r.append(random.randint(0,255))
            g.append(random.randint(0,255))
            b.append(random.randint(0,255))
        count=0
        win=pygame.font.SysFont("arial",70,True)
        vs=win.render(f"ARE YOU READY ?",1,(0,255,0))
        VS=vs.get_rect()
        VS.x=width/2-VS.width/2
        VS.y=50
        pygame.display.set_caption("AEROSTORM")
        icon=[pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/1.png"),(50,100)),270)]
        pygame.display.set_icon(icon[0])
        while menu:
            screen.fill((0,0,0))
            count+=1
            key=pygame.key.get_pressed()
            for i in range(num):
                x[i]+=1
                if x[i]>=width:
                    x[i]=0
                if count>=5:
                    x[i]=random.randint(0,width)
                    y[i]=random.randint(0,height)
                    r[i]=random.randint(0,255)
                    g[i]=random.randint(0,255)
                    b[i]=random.randint(0,255)
                    w[i]=50
                    h[i]=50
                    count=0
                pygame.draw.rect(screen,(r[i],g[i],b[i]),(x[i],y[i],w[i],h[i]))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    menu=False
             
            moupos=pygame.mouse.get_pos()
            mou=pygame.mouse.get_pressed()
            color=(255,255,0)
            font5=win.render("START GAME",1,color)
            f5rect=font5.get_rect()
            f5rect.x=width/2-f5rect.width/2
            f5rect.y=height/2-200
            c=(0,200,0)
            if mou[0]:
                if f5rect.collidepoint(moupos):
                    game()
                    pygame.display.update()
            if f5rect.collidepoint(moupos):
                    c=(0,0,0)
            pygame.draw.rect(screen,c,f5rect,0,10)
            screen.blit(font5,(f5rect.x,f5rect.y))
            
            font6=win.render("QUIT GAME",1,color)
            f6rect=font6.get_rect()
            f6rect.x=width/2-f6rect.width/2
            f6rect.y=height/2+100
            c=(0,200,0)
            if mou[0]:
                if f6rect.collidepoint(moupos):
                    sure2()
                    pygame.display.update()
            if f6rect.collidepoint(moupos):
                    c=(0,0,0)
            pygame.draw.rect(screen,c,f6rect,0,10)
            screen.blit(font6,(f6rect.x,f6rect.y))
            
            pygame.draw.rect(screen,(255,255,255),VS,0,20)
            screen.blit(vs,VS)
            pygame.display.update()
    pygame.quit()
def pause(screen):
    pygame.init()
    pause=True
    bg1=pygame.transform.scale(pygame.image.load("asset/bg/bg1.png"),(width+100,height))
    global run
    global highscore
    read=open("asset/high.score","rb")
    highscore=pickle.load(read)
    pygame.mixer.music.pause()
    
    gmenu=pygame.transform.scale(pygame.image.load("asset/menu/menu.png"),(300,100))
    gmenur=gmenu.get_rect()
    gmenur.center=width/2,700
    
    paused=pygame.transform.scale(pygame.image.load("asset/menu/gpaused.png"),(400,100))
    pausedr=paused.get_rect()
    pausedr.center=width/2,100
    
    play=pygame.transform.scale(pygame.image.load("asset/menu/continue.png"),(300,100))
    playr=play.get_rect()
    playr.center=width/2,300
    
    scoreimg=pygame.transform.scale(pygame.image.load("asset/menu/score.png"),(300,100))
    scoreimgr=scoreimg.get_rect()
    scoreimgr.center=width/2,500
    pygame.display.set_caption("AEROSTORM")
    icon=[pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/1.png"),(50,100)),270)]
    pygame.display.set_icon(icon[0])
    while pause:
        screen.blit(bg1,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pause=False
                pygame.mixer.music.unpause()
        mouse=pygame.mouse.get_pressed()
        moupos=pygame.mouse.get_pos()
        mx,my=moupos
        mouser=pygame.Rect(mx,my,20,20)
        if mouse[0]:
            if mouser.colliderect(playr):
                pause=False
                pygame.mixer.music.unpause()
            if mouser.colliderect(gmenur):
                menu1()
                pygame.mixer.music.unpause()
        screen.blit(bg1,(0,0))
        screen.blit(gmenu,gmenur)
        screen.blit(play,playr)
        screen.blit(scoreimg,scoreimgr)
        screen.blit(paused,pausedr)
        font(screen,"comic sans",60,True,f":{highscore}",(255,255,255),True,scoreimgr.right+70,scoreimgr.top+50)
        pygame.display.update()
def gameover():
    pygame.init()
    global run
    global killnumber
    global sec
    bg1=pygame.transform.scale(pygame.image.load("asset/bg/darkbg.png"),(width+100,height))
    gameover=True
    over=pygame.transform.scale(pygame.image.load("asset/menu/over.png"),(400,100))
    overr=over.get_rect()
    overr.center=width/2,100
    pygame.mixer.music.load("asset/bgm.mp3")
    pygame.mixer.music.play(-1)
    reset=pygame.transform.scale(pygame.image.load("asset/menu/reset.png"),(200,50))
    resetr=reset.get_rect()
    resetr.center=100,30
    
    killed=pygame.transform.scale(pygame.image.load("asset/menu/killed.png"),(100,50))
    killedr=killed.get_rect()
    killedr.x=0
    killedr.y=180

    win=pygame.font.SysFont("comic sans",30,True)
    many=win.render(f"{killnumber} in {sec} Seconds",1,((255,255,255)))
    ok=pygame.transform.scale(pygame.image.load("asset/menu/okay.png"),(200,50))
    
    restart=pygame.transform.scale(pygame.image.load("asset/menu/restart.png"),(300,100))
    restartr=restart.get_rect()
    restartr.center=width/2,400
    quitg=pygame.transform.scale(pygame.image.load("asset/menu/quit.png"),(300,100))
    quitgr=quitg.get_rect()
    quitgr.center=width/2,700
    read=open("asset/high.score","rb")
    highscore=pickle.load(read)
    scoreimg=pygame.transform.scale(pygame.image.load("asset/menu/score.png"),(300,100))
    scoreimgr=quitg.get_rect()
    scoreimgr.center=width/2,550
    count=0
    pygame.display.set_caption("AEROSTORM")
    icon=[pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/1.png"),(50,100)),270)]
    pygame.display.set_icon(icon[0])
    show=False
    while gameover:
        screen.blit(bg1,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameover=False
                run=False
        mouse=pygame.mouse.get_pressed()
        moupos=pygame.mouse.get_pos()
        mx,my=moupos
        mouser=pygame.Rect(mx,my,20,20)
        if mouse[0]:
            if mouser.colliderect(restartr):
                game()
            if mouser.colliderect(quitgr):
                sure2()
            if mouser.colliderect(resetr):
                highs=open("asset/high.score","wb")
                pickle.dump(0,highs)
                show=True
        if show :
            count+=1
            if count>10:
                screen.blit(ok,(780,50))
            if count>50:
                show=False
                count=0
        screen.blit(killed,killedr)
        screen.blit(many,(killedr.x,killedr.bottom+10))
        screen.blit(reset,resetr)
        screen.blit(over,overr)
        screen.blit(restart,restartr)
        screen.blit(quitg,quitgr)
        screen.blit(scoreimg,scoreimgr)
        font(screen,"comic sans",60,True,f":{highscore}",(255,255,255),True,scoreimgr.right+70,scoreimgr.top+45)
        pygame.display.update()
    pygame.quit()
def font(screen,font,size,bold,text,color,centered,x,y):
    pygame.init()
    centers=centered
    winfont=pygame.font.SysFont(font,size,bold)
    rend=winfont.render(text,1,(color))
    if centers:
        font=rend.get_rect()
        font.center=x,y
    else:
        font=(x,y)
    screen.blit(rend,font)
    pygame.display.update()
pygame.init()
pygame.mixer.init()
pygame.font.init()
size=width,height=1000,800
screen=pygame.display.set_mode((size))
pygame.display.set_caption("AEROSTORM")
icon=[pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/1.png"),(50,100)),270)]
pygame.display.set_icon(icon[0])


def msg(px,color,text,x,y):
    pygame.font.init()
    win=pygame.font.Font("asset/motter-tektura.ttf",px)
    font=win.render(text,1,color)
    screen.blit(font,(x,y))
def username1():
    pygame.init()
    global player1
    p=[
        pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/1.png"),(300,350)),270),
        pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/2.png"),(300,350)),270),
        pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/3.png"),(300,350)),270)
        ]
    countp=0
    player=p[countp]
    p1=player.get_rect()
    p1.y=height/2-200
    p1.x=0
    gamebg=pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height))
    user=True
    player1=""
    win=pygame.font.Font("asset/motter-tektura.ttf",70)
    blink=0
    Next=win.render("NEXT",1,(0,0,0))
    NEXT=Next.get_rect()
    NEXT.x=width/2-NEXT.width/2
    NEXT.y=700
    ########
    sure=win.render("PLAYER 1 USERNAME",100,(255,255,255))
    surerect=sure.get_rect()
    surerect.x=width/2-surerect.width/2
    surerect.y=20    
    clock=pygame.time.Clock()
    while user:
        screen.blit(gamebg,(0,0))
        pygame.draw.rect(screen,(255,255,255),NEXT,0,20)
        p1.x+=4
        if p1.x>=width:
            p1.x=-270
        clock.tick(60)
        countp+=0.4
        if countp>=3:
            countp=0
        player=p[int(countp)]
        screen.blit(player,(p1.x,p1.y))
        blink+=1
        player1t=win.render(player1,1,((255,255,255)))
        player1r=player1t.get_rect()
        player1r.x=100
        player1r.y=600
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                user=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    if player1=="":
                        username1()
                        pygame.display.update()
                    else:
                        username2()
                player1+=event.unicode.strip().upper()
        key=pygame.key.get_pressed()
        if len(player1)>=10:
            player1=player1[:-1]
            
        if key[pygame.K_BACKSPACE]:
            if len(player1)>0:
                player1=player1[:-1]
        x,y=player1r.topright
        screen.blit(sure,(surerect.x,surerect.y))
        pygame.draw.rect(screen,(0,255,0),(player1r.x-20,player1r.y,player1r.x+700,player1r.height),0,50)
        if blink>=20:
            pygame.draw.rect(screen,((255,255,255)),(x,y+10,2,player1r.height-20))
        if blink==40:
            blink=0
        screen.blit(player1t,player1r)
        screen.blit(Next,NEXT)
        press=pygame.mouse.get_pressed()
        mou=pygame.mouse.get_pos()
        if press[0]:
            if NEXT.collidepoint(mou):
                if player1=="":
                    username1()
                    pygame.display.update()
                else:
                    username2()
        pygame.display.update()
    pygame.quit()
def preload():
    pygame.init()
    pygame.font.init()
    gamebg=pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height))
    user=True
    init=""
    win=pygame.font.SysFont("arial",70,True)
    blink=0
    sure=win.render("WELCOME TO AEROSTORM",100,(255,255,255))
    surerect=sure.get_rect()
    surerect.x=width/2-surerect.width/2
    surerect.y=100
    win=pygame.font.SysFont("arial",30,True)
    load=0
    p=[
        pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/1.png"),(300,350)),270),
        pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/2.png"),(300,350)),270),
        pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/3.png"),(300,350)),270)
        ]
    countp=0
    player=p[countp]
    p1=player.get_rect()
    p1.y=height/2-200
    p1.x=width/2-p1.width/2
    clock=pygame.time.Clock()
    while user:
        load+=1
        if load >=0:
            init="loading. . .".title()
        if load>=50:
            init="initializing user interface. . .".title()
        if load>=100:
            init="initializing engine. . .".title()
        if load>=150:
            init="almost done. . .".title()
        if load>=200:
            menu1()
        sure1=win.render(init,100,(255,255,255))
        sure1rect=sure1.get_rect()
        sure1rect.x=width/2-sure1rect.width/2
        sure1rect.y=600
        screen.blit(gamebg,(0,0))
        countp+=0.4
        if countp>=3:
            countp=0
        player=p[int(countp)]
        screen.blit(player,(p1.x,p1.y))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                user=False

        screen.blit(sure,(surerect.x,surerect.y))
        screen.blit(sure1,(sure1rect.x,sure1rect.y))
        msg(50,(255,255,255),"CREATED BY GODSPOWER",150,700)
        
        pygame.display.update()
    pygame.quit()
def username2():
        pygame.init()
        global player2nd
        p=[
            pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/1.png"),(300,350)),90),
            pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/2.png"),(300,350)),90),
            pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/3.png"),(300,350)),90)
            ]
        countp=0
        player=p[countp]
        p1=player.get_rect()
        p1.y=height/2-200
        p1.x=width-270
        gamebg=pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height))
        user=True
        win=pygame.font.Font("asset/motter-tektura.ttf",70)
        player2nd=""
        sure1=win.render("PLAYER 2 USERNAME",100,(255,255,255))
        sure1rect=sure1.get_rect()
        sure1rect.x=width/2-sure1rect.width/2
        sure1rect.y=20
        Next=win.render("NEXT",1,(0,0,0))
        NEXT=Next.get_rect()
        NEXT.x=width/2-NEXT.width/2
        NEXT.y=700
        blink=0
        clock=pygame.time.Clock()
        while user:
            blink+=1
            screen.blit(gamebg,(0,0))
            player2t=win.render(player2nd,1,(255,255,255))
            player2r=player2t.get_rect()
            player2r.x=100
            player2r.y=600
            p1.x-=4
            if p1.x<=-270:
                p1.x=width
            clock.tick(60)
            screen.blit(gamebg,(0,0))
            countp+=0.4
            if countp>=3:
                countp=0
            player=p[int(countp)]
            screen.blit(player,(p1.x,p1.y))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    user=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        if player2nd=="":
                            username2()
                            pygame.display.update()
                        else:
                            stage()
                    player2nd+=event.unicode.strip().upper()
            key=pygame.key.get_pressed()
            if key[pygame.K_BACKSPACE]:
                player2nd=player2nd[:-1]
            if len(player2nd)>=10:
                player2nd=player2nd[:-1]
            x,y=player2r.topright
            pygame.draw.rect(screen,(0,255,0),(player2r.x-20,player2r.y,player2r.x+700,player2r.height),0,50)
            if blink>=20:
                pygame.draw.rect(screen,((255,255,255)),(x,y+10,2,player2r.height-20))
            if blink==40:
                blink=0
            
            press=pygame.mouse.get_pressed()
            mou=pygame.mouse.get_pos()
            if press[0]:
                if NEXT.collidepoint(mou):
                    if player2nd=="":
                        username2()
                    else:
                        stage()
            pygame.draw.rect(screen,(255,255,255),NEXT,0,20)
            screen.blit(Next,NEXT)
            screen.blit(player2t,player2r)
            screen.blit(sure1,sure1rect)
            pygame.display.update()
        pygame.quit()
def stage():
    global text
    rounds=True
    gamebg=pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height))
    text=""
    win=pygame.font.Font("asset/motter-tektura.ttf",70)
    Next=win.render("NEXT",1,(0,0,0))
    NEXT=Next.get_rect()
    NEXT.x=width/2-NEXT.width/2
    NEXT.y=700
    blink=0
    
    while rounds:
        press=pygame.mouse.get_pressed()
        mou=pygame.mouse.get_pos()
        blink+=1
        screen.blit(gamebg,(0,0))
        pygame.draw.rect(screen,(255,255,255),NEXT,0,20)
        if text.isdigit():
            text=text
            
        else:
            text=text[:-1]
        rend=win.render(text,1,(255,255,255))
        rendr=rend.get_rect()
        rendr.x=width/2-rendr.width/2
        rendr.y=300
        msg(70,(255,255,255),"HOW MANY ROUNDS",140,50)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                rounds=False
            if event.type==pygame.KEYDOWN:
                text+=event.unicode.strip().upper()
        
        key=pygame.key.get_pressed()
        if key[pygame.K_BACKSPACE]:
            text=text[:-1]
        if len(text)>2:
            text=text[:-1]
        pygame.draw.rect(screen,((0,255,0)),(width/2-rendr.x/2,rendr.y,rendr.x,rendr.height),0,30)
        x,y=rendr.topright
        if blink>=50:
            pygame.draw.rect(screen,((255,255,255)),(x,y,10,rendr.height))
        if blink>=100:
            blink=0
        if press[0]:
            if NEXT.collidepoint(mou):
                if text=="":
                    stage()
                    pygame.display.update()
                else:
                    menu()
                    total=int(text)
        screen.blit(rend,rendr)
        screen.blit(Next,NEXT)
        pygame.display.update()
def over():
    pygame.init()
    pygame.font.init()
    gameover=True
    gamebg=pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height))
    r=[]
    g=[]
    b=[]
    rand=[]
    number=6
    for i in range(number):
        r.append(random.randint(0,255))
        g.append(random.randint(0,255))
        b.append(random.randint(0,255))
        rand.append(0)
    mesg=""
    ans=""
    while gameover:
        screen.blit(gamebg,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameover=False
                run=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_r:
                    main()
        ############# BUTTON #############
        win=pygame.font.Font("asset/motter-tektura.ttf",50)
        mou=pygame.mouse.get_pressed()
        moupos=pygame.mouse.get_pos()
        color=(255,255,255)
        color1=(255,255,255)
        player=pygame.font.SysFont("arial",60,True)
        
        for i in range(number):
            rand[i]+=1
            font=win.render("RESTART GAME",1,(r[3],g[3],b[3]))
            frect=font.get_rect()
            frect.x=width/2-frect.width/2
            frect.y=300
            if mou[0]:
                if frect.collidepoint(event.pos):
                    main()
            
            if frect.collidepoint(moupos):
                color=(0,0,0)
                
            pygame.draw.rect(screen,color,frect,0,10)
            screen.blit(font,(frect.x,frect.y))
            
            font1=win.render("QUIT GAME",1,(r[2],g[2],b[2]))
            f1rect=font1.get_rect()
            f1rect.x=width/2-f1rect.width/2
            f1rect.y=550
            if mou[0]:
                if f1rect.collidepoint(event.pos):
                    sure()
            if f1rect.collidepoint(moupos):
                color1=(0,0,0)
            pygame.draw.rect(screen,color1,f1rect,0,10)
            screen.blit(font1,(f1rect.x,f1rect.y))

            
            if score1>=total:
                ans=f"{player1} DEFEATED {player2nd}"
                mesg=f"{player1} IS LEADING THE GAME"
                
            if score2>=total:
                ans=f"{player2nd} DEFEATED {player1}"
                mesg=f"{player2nd} IS LEADING THE GAME"
                
            font9=win.render(mesg,1,(r[5],g[5],b[5]))
            f9rect=font9.get_rect()
            f9rect.x=width/2-f9rect.width/2
            f9rect.y=650
            pygame.draw.rect(screen,color,f9rect,0,10)
            screen.blit(font9,(f9rect.x,f9rect.y))
            
                
            font6=win.render("CHANGE USERS",1,(r[4],g[4],b[4]))
            f6rect=font6.get_rect()
            f6rect.x=width/2-f6rect.width/2
            f6rect.y=420
            c=(255,255,255)
            if mou[0]:
                if f6rect.collidepoint(moupos):
                    username1()
            if f6rect.collidepoint(moupos):
                    c=(0,0,0)
            pygame.draw.rect(screen,c,f6rect,0,10)
            screen.blit(font6,(f6rect.x,f6rect.y))
            
            font2=player.render(ans,1,(r[0],g[0],b[0]))
            f2rect=font2.get_rect()
            f2rect.x=width/2-f2rect.width/2
            f2rect.y=150
            screen.blit(font2,(f2rect.x,f2rect.y))
            msg(100,(r[1],g[1],b[1]),"GAME OVER",width/2-300,10)
            
            if rand[i]>=10:
                r[i]=random.randint(0,255)
                g[i]=random.randint(0,255)
                b[i]=random.randint(0,255)
                rand[i]=0
            
         
        pygame.display.update()
    pygame.quit()
def sure():
    pygame.init()
    pygame.font.init()
    sure=True
    imgs=pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height))
    while sure:
        screen.blit(imgs,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sure=False
        win=pygame.font.Font('asset/motter-tektura.ttf',100)
        mouses=pygame.mouse.get_pressed()
        mousespos=pygame.mouse.get_pos()
        
        sure1=win.render("WANT TO QUIT",True,(255,255,255))
        sure1rect=sure1.get_rect()
        sure1rect.x=width/2-sure1rect.width/2
        sure1rect.y=150
        screen.blit(sure1,(sure1rect.x,sure1rect.y))
        
        sure=win.render("ARE YOU SURE YOU",True,(255,255,255))
        surerect=sure.get_rect()
        surerect.x=width/2-surerect.width/2
        surerect.y=20
        screen.blit(sure,(surerect.x,surerect.y))

        win1=pygame.font.Font('asset/motter-tektura.ttf',70)
        yes=win1.render("YES",True,(255,255,255))
        yesr=yes.get_rect()
        yesr.x=width/2-yesr.width-150
        yesr.y=400
        pygame.draw.rect(screen,(0,0,0),yesr,0,10)
        screen.blit(yes,yesr)
        if mouses[0]:
            if yesr.collidepoint(mousespos):
                sure=False
                pygame.quit()
        pygame.init()
        pygame.font.init()
        no=win1.render("NO",1,(255,255,255))
        nor=no.get_rect()
        nor.x=width/2+yesr.width
        nor.y=400
        pygame.draw.rect(screen,(0,0,0),nor,0,10)
        screen.blit(no,nor)
        if mouses[0]:
            if nor.collidepoint(mousespos):
                sure=False
        pygame.display.update()

def main():
    global total,score1,score2
    bgm=pygame.mixer.Sound("asset/background.mp3")
    bgm.play(-1)
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    bgm.stop()
    bg=[pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height+100))]
    bg2=[pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height+100))]

    p=[
        pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/1.png"),(150,200)),270),
        pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/2.png"),(150,200)),270),
        pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/3.png"),(150,200)),270)
        ]
    pp=[
        pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated2/1.png"),(150,200)),90),
        pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated2/2.png"),(150,200)),90),
        pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated2/3.png"),(150,200)),90)
        ]
    bw=100
    bh=100
    bomb=[pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_1.png"),(bw,bh)),
        pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_2.png"),(bw,bh)),
        pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_3.png"),(bw,bh)),
        pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_4.png"),(bw,bh)),
        pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_5.png"),(bw,bh)),
        pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_6.png"),(bw,bh)),
        pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_7.png"),(bw,bh)),
        pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_8.png"),(bw,bh)),
        pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_9.png"),(bw,bh)),
        pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_10.png"),(bw,bh)),
        ]
    bomw=200
    bomh=200
    bomcount=0
    bomb1=[pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_1.png"),(bomw,bomh)),
        pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_2.png"),(bomw,bomh)),
        pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_3.png"),(bomw,bomh)),
        pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_4.png"),(bomw,bomh)),
        pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_5.png"),(bomw,bomh)),
        pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_6.png"),(bomw,bomh)),
        pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_7.png"),(bomw,bomh)),
        pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_8.png"),(bomw,bomh)),
        pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_9.png"),(bomw,bomh)),
        pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_10.png"),(bomw,bomh)),
        ]

    bcount=0
    count=0
    wait=0
    pause=False
    fire=0
    
    pygame.mixer.music.load("asset/bgm.mp3")
    pygame.mixer.music.play(-1)

    shoot=pygame.mixer.Sound("asset/explosion.wav")
    gun=pygame.mixer.Sound("asset/shoot.wav")
    clock=pygame.time.Clock()
    play=0

    fps=60
    shot=0

    #fastness 
    vel=20
    bvel=30

    shake=20
    vibration=0
    vibrate=False

    health1=200
    health2=200
    
    life=25
    score1=0
    score2=0
    center=70
    total=int(text)
    end=False
    stop=0
    player=p[count]
    p1=player.get_rect()
    p1.y=height/2
    p1.x=0

    player2=pp[count]
    p2=player2.get_rect()
    
    p2.x=width-100
    p2.y=height/2+10

    bullet=False
    bimg=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/shot.png"),(20,20)),360)
    b=bimg.get_rect()
    b.x=0
    b.y=0

    bullet1=False
    bimg1=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/shot.png"),(20,20)),180)
    b1=bimg.get_rect()
    b1.x=0
    b1.y=0
    
    bgx=0
    bgy=0

    bg2x=width
    bg2y=0
    run=True
    startmenu=True
    color=(255,0,255)
  
    #######################################################################
    #########   GAME   LOOP  ##############################################
    while run:
        colorr=(255,255,255)
        colorr1=(255,255,255)
        time=clock.tick(fps)/1000
        background=bg[0]
        screen.blit(background,(bgx,bgy))
        bgx-=9
        if bgx <= -width:
            bgx=width
            
        background2=bg2[0]
        screen.blit(background2,(bg2x,bg2y))
        bg2x-=9
        if bg2x <= -width:
            bg2x=width
        msg(30,(255,255,255),f"{total} ROUNDS",width/2-5,60)
        win=pygame.font.Font("asset/motter-tektura.ttf",30)

        text1=win.render(player1,1,(255,255,255))
        text2=win.render(player2nd,1,(255,255,255))
        tr=text2.get_rect()

        screen.blit(text1,(220,15))
        screen.blit(text2,(width-200- 30-tr.width,15))
        
        mou=pygame.mouse.get_pressed()
        moupos=pygame.mouse.get_pos()
        font3=win.render("PAUSE",1,color)
        f3rect=font3.get_rect()
        f3rect.x=width/2-(f3rect.width+20)
        f3rect.y=60
        if mou[0]:
            if f3rect.collidepoint(moupos):
                pauseme()
        if f3rect.collidepoint(moupos):
            colorr=(0,0,0)
        pygame.draw.rect(screen,colorr,f3rect,0,5)
        screen.blit(font3,(f3rect.x,f3rect.y))
        count+=0.4
        if count>=3:
            count=0
        player=p[int(count)]
        player2=pp[int(count)]
        
        if bullet==False:
            b.x=p1.x+center+35
            b.y=p1.y+center

        if bullet1==False:
            b1.x=p2.x+center
            b1.y=p2.y+center-10
        ################### FOR LOOP ###################
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pauseme()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                if event.key==pygame.K_p:
                    pauseme()
        key=pygame.key.get_pressed()
        #player1
        if key[pygame.K_LEFT]:
            p2.x-=vel
        if key[pygame.K_RIGHT]:
            p2.x+=vel
        if key[pygame.K_UP]:
            p2.y-=vel
        if key[pygame.K_DOWN]:
            p2.y+=vel
            
        #fire bullet
        if key[pygame.K_RCTRL]:
            bullet1=True
        if bullet1:
            b1.x-=bvel
        if b1.x<=p1.x:
            bullet1=False
            b1.x=p2.x+center
            b1.y=p2.y+center
            
       #player2
        if key[pygame.K_a]:
            p1.x-=vel
        if key[pygame.K_s]:
            p1.x+=vel
        if key[pygame.K_w]:
            p1.y-=vel
        if key[pygame.K_z]:
            p1.y+=vel
        
        #fire bullet
        if key[pygame.K_SPACE]:
            bullet=True        
            
        if bullet:
           b.x+=bvel
        if b.x>=p2.x+70:
            bullet=False
            b.x=p1.x+center+50
            b.y=p1.y+center
        #bullet and bullet collision
        if b.colliderect(b1):
            b.x=p1.x+center+50
            b.y=p1.y+center
            bom=bomb[4]
            screen.blit(bom,(b1.x,b1.y-50))
            
            b1.x=p2.x+center
            b1.y=p2.y+center
            bullet=False
            bullet1=False
            
        if b.colliderect(p2):
            vibrate=True
            shoot.play()
            bom=bomb[4]
            screen.blit(bom,(p2.x-10,p2.y+20))
            health2-=life
            b.x=p1.x+center+50
            b.y=p1.y+center
            bullet=False
        if vibrate:
            vibration+=1
            if vibration==5:
                bgy-=shake
                bg2y-=shake
            if vibration==10:
                bgy+=shake
                bg2y+=shake
            if vibration==15:
                bgy-=shake
                bg2y-=shake
            if vibration==20:
                bgy+=shake
                bg2y+=shake
                vibration=0
                vibrate=False
            
        if b1.colliderect(p1):
            shoot.play()
            vibrate=True
            bom=bomb[4]
            screen.blit(bom,(p1.x+center+35,p1.y+20))
            health1-=life
            b1.x=p2.x+center
            b1.y=p2.y+center
            bullet1=False
        if vibrate:
            vibration+=1
            if vibration==5:
                bgy-=shake
                bg2y-=shake
            if vibration==10:
                bgy+=shake
                bg2y+=shake
            if vibration==15:
                bgy-=shake
                bg2y-=shake
            if vibration==20:
                bgy+=shake
                bg2y+=shake
                vibration=0
                vibrate=False

        
        if p1.x >= width/2-150:
            p1.x=width/2-150
        if p1.x <=-50:
            p1.x=-50
        if p1.y >= height-70:
            p1.y=height-70
        if p1.y<= 20:
            p1.y=20

        if p2.x >= width-150:
            p2.x=width-150
        if p2.x <= width/2:
            p2.x=width/2
        if p2.y >= height-70:
            p2.y=height-70
        if p2.y <= 0:
            p2.y=0
        percent1=int(health1/200*100/1)
        percent2=int(health2/200*100/1)

        screen.blit(bimg1,(b1.x,b1.y))
        screen.blit(bimg,(b.x,b.y))
        screen.blit(player,(p1.x,p1.y))
        screen.blit(player2,(p2.x,p2.y))
        #1
        pygame.draw.rect(screen,(255,0,0),(10,15,200,30),0,20)
        pygame.draw.rect(screen,(0,255,0),(10,15,health1,30),0,20)
        
        #2
        pygame.draw.rect(screen,(255,0,0),(width-width/4.5,15,200,30),0,20)
        pygame.draw.rect(screen,(0,255,0),(width-width/4.5,15,health2,30),0,20)

        msg(25,(0,0,0),f"{percent1}%",230-230/2.2,15)
        msg(25,(0,0,0),f"{percent2}%",width-width/5,15)
       
        #life
        if health1 <= 0:
            score2+=1
            health1=200
            health2=200
            
        if score2>=total:
            wait+=1
            bomcount+=0.3
            if bomcount>=9:
                bomcount=9
            boom=bomb1[int(bomcount)]
            screen.blit(boom,(p1.x,p1.y+center-90))
        if wait>=40:
            over()
            
        if health2 <= 0:
            score1+=1
            health1=200
            health2=200
            
        if score1>=total:
            bomcount+=0.3
            if bomcount>=9:
                bomcount=9
            boom=bomb1[int(bomcount)]
            screen.blit(boom,(p2.x,p2.y+center-90))
            wait+=1  
        if wait>=40:
            over()
        if health2 <= 0 and health1 <= 0:
            score2=score2
            score1=score1
        
        msg(50,(255,255,255),f"{score1} : {score2}",width/2-50,10)     
        pygame.display.update()
    pygame.quit()
###########################################################
################ END OF LOOP ##############################
def pauseme():
    pygame.init()
    pygame.font.init()
    pau=pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height))
    screen=pygame.display.set_mode((size))
    pause=True
    clock=pygame.time.Clock()
    while pause:
        pygame.mixer.music.pause()
        clock.tick(60)
        screen.blit(pau,(0,0))
        msg(100,(255,255,255),"GAME PAUSED",200,50)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pause=False
        win=pygame.font.Font("asset/motter-tektura.ttf",50)
        mou=pygame.mouse.get_pressed()
        moupos=pygame.mouse.get_pos()
        color=(255,255,0)
        
        font5=win.render("CONTINUE",1,color)
        f5rect=font5.get_rect()
        f5rect.x=width/2-f5rect.width/2
        f5rect.y=200
        c=(0,200,0)
        if mou[0]:
            if f5rect.collidepoint(moupos):
                pause=False
                pygame.mixer.music.unpause()
        if f5rect.collidepoint(moupos):
                c=(0,0,0)
        pygame.draw.rect(screen,c,f5rect,0,10)
        screen.blit(font5,(f5rect.x,f5rect.y))

        font6=win.render("CHANGE USERS",1,color)
        f6rect=font6.get_rect()
        f6rect.x=width/2-f6rect.width/2
        f6rect.y=350
        c=(0,200,0)
        if mou[0]:
            if f6rect.collidepoint(moupos):
                username1()
        if f6rect.collidepoint(moupos):
                c=(0,0,0)
        pygame.draw.rect(screen,c,f6rect,0,10)
        screen.blit(font6,(f6rect.x,f6rect.y))

        font7=win.render("QUIT GAME",1,color)
        f7rect=font7.get_rect()
        f7rect.x=width/2-f7rect.width/2
        f7rect.y=500
        col=(0,200,0)
        if mou[0]:
            if f7rect.collidepoint(moupos):
                sure()
        if f7rect.collidepoint(moupos):
            col=(0,0,0)
        pygame.draw.rect(screen,col,f7rect,0,10)
        screen.blit(font7,(f7rect.x,f7rect.y))
        pygame.display.update()
def menu():
    pygame.init()
    pygame.font.init()
    menu=True
    if menu:
        count=0
        x=[]
        y=[]
        w=[]
        h=[]
        r=[]
        g=[]
        b=[]
        num=500
        for i in range(num):
            x.append(random.randint(0,width))
            y.append(random.randint(0,height))
            w.append(10)
            h.append(10)
            r.append(random.randint(0,255))
            g.append(random.randint(0,255))
            b.append(random.randint(0,255))
        count=0
        win=pygame.font.SysFont("arial",70,True)
        vs=win.render(f"{player1} VS {player2nd}",1,(0,255,0))
        VS=vs.get_rect()
        VS.x=width/2-VS.width/2
        VS.y=50
        while menu:
            screen.fill((0,0,0))
            count+=1
            key=pygame.key.get_pressed()
            for i in range(num):
                x[i]+=1
                if x[i]>=width:
                    x[i]=0
                if count>=5:
                    x[i]=random.randint(0,width)
                    y[i]=random.randint(0,height)
                    r[i]=random.randint(0,255)
                    g[i]=random.randint(0,255)
                    b[i]=random.randint(0,255)
                    w[i]=50
                    h[i]=50
                    count=0
                pygame.draw.rect(screen,(r[i],g[i],b[i]),(x[i],y[i],w[i],h[i]))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    menu=False
             
            moupos=pygame.mouse.get_pos()
            mou=pygame.mouse.get_pressed()
            color=(255,255,0)
            font5=win.render("START GAME",1,color)
            f5rect=font5.get_rect()
            f5rect.x=width/2-f5rect.width/2
            f5rect.y=height/2-100
            c=(0,200,0)
            if mou[0]:
                if f5rect.collidepoint(moupos):
                    main()
                    pygame.display.update()
            if f5rect.collidepoint(moupos):
                    c=(0,0,0)
            pygame.draw.rect(screen,c,f5rect,0,10)
            screen.blit(font5,(f5rect.x,f5rect.y))
            font6=win.render("QUIT GAME",1,color)
            f6rect=font6.get_rect()
            f6rect.x=width/2-f6rect.width/2
            f6rect.y=height/2+100
            c=(0,200,0)
            if mou[0]:
                if f6rect.collidepoint(moupos):
                    sure()
                    pygame.display.update()
            if f6rect.collidepoint(moupos):
                    c=(0,0,0)
            pygame.draw.rect(screen,c,f6rect,0,10)
            screen.blit(font6,(f6rect.x,f6rect.y))
            pygame.draw.rect(screen,(255,255,255),VS,0,20)
            screen.blit(vs,VS)
            pygame.display.update()
    pygame.quit()
pygame.init()
preload()
pygame.display.update()











import pygame, sys
import time
import random
import Animal

from pygame import mixer

pygame.init()

clock = pygame.time.Clock()

size = [900, 800]
screen = pygame.display.set_mode(size)

game = 0
daybackground = pygame.image.load("images/daybackground.jpg")
daybackground = pygame.transform.scale(daybackground, size)
nightbackground = pygame.image.load("images/nightbackground.jpg")
nightbackground = pygame.transform.scale(nightbackground, size)

nightmusic_sound = mixer.Sound('sounds/nightmusic.mp3')
nightmusic_sound.play(-1)
nightmusic_sound.set_volume(0.5)

gameover = pygame.image.load("images/gameover.jpg")
gameover = pygame.transform.scale(gameover, size)
youwin = pygame.image.load("images/youwin.png")
youwin = pygame.transform.scale(youwin, (700,400))
title = pygame.image.load("images/title.png")
title = pygame.transform.scale(title, (900,550))
titlerect = title.get_rect()
titlerect.center = [480, 500]
ufoimg = pygame.image.load("images/ufo.png")
ufoimg = pygame.transform.scale(ufoimg, (170,110))
ufo = ufoimg.get_rect()
pigincowleftimg = pygame.image.load("images/pigincow.png")
pigincowleftimg = pygame.transform.scale(pigincowleftimg, (120,70))
pigincowrightimg = pygame.transform.flip(pigincowleftimg, True, False)
dalmationleftimg = pygame.image.load("images/dalmation.png")
dalmationleftimg = pygame.transform.scale(dalmationleftimg, (150,100))
dalmationrightimg = pygame.transform.flip(dalmationleftimg, True, False)
beamimg = pygame.image.load("images/abductionbeam.png")
beamimg = pygame.transform.scale(beamimg, (100,500))
beam = beamimg.get_rect()
boomimg = pygame.image.load("images/boom.png")
boomimg = pygame.transform.scale(boomimg, (400, 300))
boom = boomimg.get_rect()
againimg = pygame.image.load("images/again.png")
againimg = pygame.transform.scale(againimg, (400, 200))
again = againimg.get_rect()

cowleftimg = pygame.image.load("images/cow.png")
cowleftimg = pygame.transform.scale(cowleftimg, (150,100))
cowrightimg = pygame.transform.flip(cowleftimg,True, False)
goldencowimg = pygame.image.load("images/goldencow.png")
goldencowimg = pygame.transform.scale(goldencowimg, (150,100))
goldencow = goldencowimg.get_rect()
playagainimg = pygame.image.load("images/playagain.png")
playagainimg = pygame.transform.scale(playagainimg, (400, 200))
playagain = playagainimg.get_rect()
playagain.center = [250,600]
instructionimg = pygame.image.load("images/instructions.png")
instructionimg = pygame.transform.scale(instructionimg, (350, 150))
instruction = instructionimg.get_rect()
instruction.center = [650, 590]
instructionpage = pygame.image.load("images/instructpage.png")
instructionpage = pygame.transform.scale(instructionpage, size)
exitimg = pygame.image.load("images/exit.png")
exitimg = pygame.transform.scale(exitimg, (50,50))
exit = exitimg.get_rect()
exit.topleft = [140,55]
ufo.center = [450,60]
#counter, text = 10, '10'.rjust(3)
#pygame.time.set_timer(pygame.USEREVENT, 1)
font = pygame.font.SysFont('Consolas', 30)
flyingAnimal = False
originalbottom = 700
spawncow = True
timer = 3000
score = 0
instructions = False
animals = []


animals = []
c1 = Animal.Animal("cow", 4, random.randint(600, 750), "left", cowleftimg.get_rect(), False, True)
c1.rect.center = [720, c1.position]
animals.append(c1)

c2 = Animal.Animal("cow", 6, random.randint(600, 750), "right", cowrightimg.get_rect(), False, True)
c2.rect.center = [300, c2.position]
animals.append(c2)

c3 = Animal.Animal("cow", 8, random.randint(600, 750), "right", cowrightimg.get_rect(), False, True)
c3.rect.center = [400, c3.position]
animals.append(c3)

c4 = Animal.Animal("golden cow", 12, random.randint(600, 750), "left", goldencow, False, True)
c4.rect.center = [750, c4.position]


p1 = Animal.Animal("pig", 6, random.randint(600, 750), "left", pigincowleftimg.get_rect(), False, True)
p1.rect.center = [400, p1.position]
animals.append(p1)

d1 = Animal.Animal("dalmation", 6, random.randint(600, 750), "right", dalmationrightimg.get_rect(), False, True)
d1.rect.center = [400, d1.position]
animals.append(d1)


move = True
pos = [0,0]
count = 0
randomnum = random.randint(1500,2500)


while True:
    if timer == randomnum:
        animals.append(c4)
    for event in pygame.event.get():
        #if event.type == pygame.USEREVENT: 
         #   counter -= 1
          #  text = str(counter).rjust(3) if counter > 0 else 'GAME OVER'
        if event.type == pygame.QUIT:
            pygame.quit()
        
    mouse_button = pygame.mouse.get_pressed()
    if mouse_button[0] == 1:
        pos = pygame.mouse.get_pos()
    if playagain.collidepoint(pos):
            game = 1
            pos = [0,0]
    if instruction.collidepoint(pos):
        instructions = True
        pos = [0,0]
    if exit.collidepoint(pos):
        instructions = False
        pos = [0,0]
    if again.collidepoint(pos) and game == 2:
        game = 1
    if game != 2:
        pos = [0,0]
        if game == 1:
            timer -= 1
        if timer < 0:
            timer = 0
            game = 2
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ufo = ufo.move(-5,0)
        if keys[pygame.K_RIGHT]:
            ufo = ufo.move(5,0)
        if keys[pygame.K_UP]:
            ufo = ufo.move(0,-5)
        if keys[pygame.K_DOWN]:
            ufo = ufo.move(0,5)
        if keys[pygame.K_SPACE]:
            spawnbeam = True
            if game == 1:
                beam_sound = mixer.Sound('sounds/laser.mp3')
                beam_sound.play()
                beam_sound.set_volume(0.1)
        else:
            spawnbeam = False
        
        if ufo.left < 0:
            ufo.left = 0

        if ufo.right > 900:
            ufo.right = 900
        
        if ufo.top < 0:
            ufo.top = 0

        if ufo.bottom > 300:
            ufo.bottom = 300

        for animal in animals:
            if animal.direction == "right" and animal.move:
                animal.rect.x += animal.speed
            elif animal.direction == "left" and animal.move:
                animal.rect.x -= animal.speed
            if animal.rect.left > 750 or animal.rect.right < 150 and animal.type != "golden cow":
                if animal.direction == "right":
                    animal.direction = "left"
                    #cow.rect = cowleftimg.get_rect()
                else:
                    animal.direction = "right"
                    #cow.rect = cowrightimg.get_rect()
            
            if spawnbeam and beam.colliderect(animal.rect) and beam.centerx + 15 > animal.rect.centerx and beam.centerx - 15 < animal.rect.centerx and beam.bottom - 150 < animal.rect.top and beam.bottom + 100 > animal.rect.bottom:
                animal.flying = True
            elif spawnbeam and animal.rect.bottom < animal.position and beam.colliderect(animal.rect) and beam.centerx + 15 > animal.rect.centerx and beam.centerx - 15 < animal.rect.centerx:
                animal.flying = True
            elif not spawnbeam or not beam.centerx + 15 > animal.rect.centerx or not beam.centerx - 15 < animal.rect.centerx:
                animal.rect.y += 5
                animal.flying = False
                if animal.rect.bottom > animal.position:
                    animal.rect.bottom = animal.position
                    animal.move = True
            
            #elif animal.rect.colliderect(beam) and beam.bottom - 50 < animal.rect.centerx and beam.bottom > animal.rect.centerx:
                #animal.flying = True
            if animal.flying and spawnbeam:
                animal.move = False
                if animal.type == "pig" or animal.type == "dalmation":
                    animal.rect.y -= 2.75
                elif animal.type == "cow":
                    animal.rect.y -= 2.5
                elif animal.type == "golden cow":
                    animal.rect.y -= 2
                if animal.rect.top < ufo.bottom:
                    spawncow = False
                    animals.remove(animal)
                    if animal.type == "golden cow":
                        score += 100
                    elif animal.type == "cow":
                        score += 10
                        count += 1
                        if count == 3:
                            game = 3
                    elif animal.type == "pig" or animal.type == "dalmation":
                        game = 2
                        
            #animal.flying = False
            #if not spawnbeam or not animal.rect.colliderect(beam):
            
                    
            

                
        time = font.render("Timer: " +  str(timer), True, "WHITE")
        scoretext = font.render("Score: " + str(score), True, "WHITE")
        beam.top = ufo.bottom
        beam.centerx = ufo.centerx+5
        if game == 0:
            screen.blit(daybackground, (0,0))
            screen.blit(playagainimg, playagain)
            screen.blit(title, titlerect) 
            screen.blit(instructionimg, instruction)
            if instructions:
                screen.blit(daybackground, (0,0))
                screen.blit(instructionpage,(75,0))
                screen.blit(exitimg, exit)
        if game == 1:
            screen.blit(nightbackground, (0,0))
            screen.blit(time, (20,20))
            screen.blit(scoretext, (720, 20))
            screen.blit(ufoimg, ufo)
                
                #screen.blit(pigincowimg, pigincow)
            if spawnbeam:
                screen.blit(beamimg, beam)

           #goldcow_sound_playing = False
            for animal in animals:
                if animal.type == "golden cow":
                    screen.blit(goldencowimg, animal.rect)

                    if animal.rect.right > 10:
                        goldcow_sound = mixer.Sound('sounds/glitter.mp3')
                        goldcow_sound.play()
                        #goldcow_sound_playing = True

                    #if animal.rect.right < 10:
                        #if goldcow_sound_playing:
                         #   goldcow_sound.stop()
                          #  goldcow_sound_playing = False

                elif animal.direction == "left" and animal.type == "cow":
                    screen.blit(cowleftimg, animal.rect)
                elif animal.direction == "right" and animal.type == "cow":
                    screen.blit(cowrightimg, animal.rect)
                elif animal.direction == "left" and animal.type == "pig":
                    screen.blit(pigincowleftimg, animal.rect)    
                elif animal.direction == "right" and animal.type == "pig":
                    screen.blit(pigincowrightimg, animal.rect)
                elif animal.direction == "left" and animal.type == "dalmation":
                    screen.blit(dalmationleftimg, animal.rect)    
                elif animal.direction == "right" and animal.type == "dalmation":
                    screen.blit(dalmationrightimg, animal.rect)
    boom.center = ufo.center
    if game == 2 or game == 3:
        if game == 2:
            screen.blit(gameover, (0,0))
            screen.blit(boomimg, boom)

            boom_sound = mixer.Sound("sounds/boom.mp3")
            boom_sound.play()
            boom_sound.set_volume(0.1)

            again.center = [450,450]


        if game == 3:
            screen.blit(daybackground, (0,0))
            screen.blit(youwin, (130,200))
            again.center = [450,600]
        screen.blit(againimg, again)
        score = 0
        count = 0
        timer = 3000
        animals = []
        c1 = Animal.Animal("cow", 4, random.randint(600, 750), "left", cowleftimg.get_rect(), False, True)
        c1.rect.center = [720, c1.position]
        animals.append(c1)

        c2 = Animal.Animal("cow", 6, random.randint(600, 750), "right", cowrightimg.get_rect(), False, True)
        c2.rect.center = [300, c2.position]
        animals.append(c2)

        c3 = Animal.Animal("cow", 8, random.randint(600, 750), "right", cowrightimg.get_rect(), False, True)
        c3.rect.center = [400, c3.position]
        animals.append(c3)

        c4 = Animal.Animal("golden cow", 12, random.randint(600, 750), "left", goldencow, False, True)
        c4.rect.center = [750, c4.position]


        p1 = Animal.Animal("pig", 6, random.randint(600, 750), "left", pigincowleftimg.get_rect(), False, True)
        p1.rect.center = [400, p1.position]
        animals.append(p1)

        d1 = Animal.Animal("dalmation", 6, random.randint(600, 750), "right", dalmationrightimg.get_rect(), False, True)
        d1.rect.center = [400, d1.position]
        animals.append(d1)


                
    pygame.display.flip()
    clock.tick(60)
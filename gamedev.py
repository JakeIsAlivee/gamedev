import pygame
import sys

import os #cum chalice opener


scriptdirfolder = os.path.dirname(os.path.realpath(__file__))

if scriptdirfolder.find('\\') != -1:
    slash = '\\'
else:
    slash = '/'


pygame.init()

window = pygame.display.set_mode((700,700))

pygame.display.set_caption('Game Dev test')

fps = pygame.time.Clock()

bigfont = pygame.font.SysFont('couriernew',64)

question_gamedev1 = bigfont.render('Do you want to',False,(0,0,0))
question_gamedev2 = bigfont.render('be a',False,(0,0,0))
question_gamedev3 = bigfont.render('Game Developer?',False,(0,0,0))

question_code1 = bigfont.render('Do you know how',False,(0,0,0))
question_code2 = bigfont.render('to write code?',False,(0,0,0))

question_ifstatements1 = bigfont.render('Is there many',False,(0,0,0))
question_ifstatements2 = bigfont.render('If Statements',False,(0,0,0))
question_ifstatements3 = bigfont.render('in your code?',False,(0,0,0))


urgood1 = bigfont.render("Okay you're",False,(0,0,0))
urgood2 = bigfont.render("good :p",False,(0,0,0))


gamedevq = 1

yestext = bigfont.render('Yes',False,(0,0,0))
notext =  bigfont.render('No' ,False,(0,0,0))

while True:

    window.fill((255,255,255))

    if gamedevq == 1:
        window.blit(question_gamedev1,(350 -  (question_gamedev1.get_width()/2),50))
        window.blit(question_gamedev2,(350 -  (question_gamedev2.get_width()/2),134))
        window.blit(question_gamedev3,(350 -  (question_gamedev3.get_width()/2),218))

    if gamedevq == 2:
        window.blit(question_code1,(350 -  (question_code1.get_width()/2),50))
        window.blit(question_code2,(350 -  (question_code2.get_width()/2),134))

    if gamedevq == 3:
        window.blit(question_ifstatements1,(350 -  (question_ifstatements1.get_width()/2),50))
        window.blit(question_ifstatements2,(350 -  (question_ifstatements2.get_width()/2),134))
        window.blit(question_ifstatements3,(350 -  (question_ifstatements3.get_width()/2),218))

    if gamedevq == 4:
        window.blit(urgood1,(350 -  (urgood1.get_width()/2),280))
        window.blit(urgood2,(350 -  (urgood2.get_width()/2),340))

    if gamedevq != 4:
        pygame.draw.lines(window,(0,0,0),False,[(40 ,500),(280,500),(280,600),(40 ,600),(40 ,500)],2)
        pygame.draw.lines(window,(0,0,0),False,[(660,500),(420,500),(420,600),(660,600),(660,500)],2)
        window.blit(yestext,(100,515))
        window.blit(notext, (505,515))

    pygame.display.update()

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.WINDOWCLOSE:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.pos[0] > 40  and event.pos[0] < 280 and event.pos[1] > 500 and event.pos[1] < 600: #yes
                if gamedevq == 1: #gamedev
                    gamedevq = 2
                    continue
                if gamedevq == 2: #write code
                    gamedevq = 3
                    continue
                if gamedevq == 3: #if statements
                    os.startfile(scriptdirfolder+slash+'bestgamedevever.mp4')
                    pygame.quit()
                    sys.exit()

            if event.pos[0] > 420 and event.pos[0] < 660 and event.pos[1] > 500 and event.pos[1] < 600: #no
                if gamedevq == 1: #gamedev
                    pygame.quit()
                    sys.exit()
                if gamedevq == 2: #write code
                    os.startfile(scriptdirfolder+slash+'bestgamedevever.mp4')
                    pygame.quit()
                    sys.exit()
                if gamedevq == 3: #if statements
                    gamedevq = 4
                    continue

            

    fps.tick(60)
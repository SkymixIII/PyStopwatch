from clock import Clock
import pygame
from pygame.locals import*
 


class Stopwatch:
    def __init__(self):
        self.c = Clock()
        self.screensize = [600,640]
        self.window=pygame.display.set_mode(self.screensize, pygame.RESIZABLE)
        pygame.display.set_caption("Stopwatch")
        

    def draw(self):
        BLANC = (255,255,255)
        self.window.fill((0,0,0))
        self.c.hide()
        txt = str(self.c.minutes) + ":"
        if len(txt)==2:
            txt = "0" + txt
        txt += str(self.c.seconds) + "," 
        if len(txt)==5:
            txt = txt[0:3]+ "0" + txt[3:]
        txt+= str(self.c.mil) 
        if len(txt)==7:
            txt = txt[0:6]+ "0" + txt[6:]
        self.base_font = pygame.font.SysFont(None,int(0.3*self.screensize[0]))
        self.window.blit(self.base_font.render(txt, True , BLANC),(0.08*self.screensize[0],25))

        #pygame.draw.circle(self.window, GREEN, [,], 40)



        pygame.display.flip()

        

    def run(self):
        start = False
        started = False
        stop = False
        open = True
        self.c.final = 0
        while open:
            self.screensize = pygame.display.get_surface().get_size()
            if start:
                self.c.start()
                start = False
            if started:
                self.c.update()
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    open = False
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    start = True
                    started = True



        pygame.quit()
    


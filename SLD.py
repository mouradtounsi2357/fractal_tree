import pygame, math

# initiation pygame --------------------------------------------$
pygame.init()

# class slider -------------------------------------------------$
# arguments : display  -> <class 'pygame.Surface'>
#           : position -> 2-uplet -> <class 'int'>
class Slider():
    def __init__(self,display,position):
        self.display=display
        self.out=0.0

        self.pos=position
        self.width=100
        self.height=40
        self.pd=(self.pos[0]+int(self.width/10),self.pos[1]+int(self.height/2))
        self.pf=(self.pos[0]+int((9*self.width)/10),self.pos[1]+int(self.height/2))
        self.CUR=self.pd

        self.etap=[0,0]

        self.image=pygame.image.load("images/im1_slider.png")
        self.image=pygame.transform.scale(self.image,(self.width,self.height))

    def draw(self):
        self.display.blit(self.image,self.pos)
        pygame.draw.circle(self.display,(0,0,0),self.CUR,7)
        
    def update(self):
        mouse_pos=pygame.mouse.get_pos()
        if math.sqrt((self.CUR[0]-mouse_pos[0])**2+(self.CUR[1]-mouse_pos[1])**2) <= 7 :
            if self.etap[0] == 0 or self.etap[0] == 1:
                self.etap[0]=1
            if self.etap[0] == 2 and self.etap[1] != 2:
                self.etap[1]=1
        else:
            if self.etap[0] == 1:
                self.etap[0]=0
            if self.etap[1] == 1:
                self.etap[1]=0
        
        if pygame.mouse.get_pressed()[0]:
            if self.etap[0] == 0:
                self.etap[0]=2
            if self.etap[0] == 1:
                self.etap[1]=2
        else:
            if self.etap[0] == 2:
                self.etap[0]=0
            if self.etap[1] == 2:
                self.etap[1]=0
        
        if self.etap == [1,2] or self.etap == [2,2]:
            self.CUR=(max(min(pygame.mouse.get_pos()[0],self.pf[0]),self.pd[0]),self.CUR[1])
        
        self.out=float((self.CUR[0]-self.pd[0])/(self.pf[0]-self.pd[0]))

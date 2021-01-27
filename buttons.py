import pygame

class Button:
    def __init__(self, x, y, text, drawSurface, img1="notpressed.png", img2="pressed.png"):
        self.x = x
        self.y = y
        self.text = text
        self.drawSurface = drawSurface

        # Button normal state
        self.img1 = pygame.image.load("assets/notpressed.png").convert()
        self.img1 = pygame.transform.scale2x(self.img1)
        # Button when pressed
        self.img2 = pygame.image.load("assets/pressed.png").convert()
        self.img2 = pygame.transform.scale2x(self.img2)
    
        self.isPressed = False
        
    def draw(self):
        
        if(not self.isPressed):
            self.drawSurface.blit(self.img1, (self.x, self.y))
        else:
            self.drawSurface.blit(self.img2, (self.x, self.y))
            

    def isOver(self, pos):
        
        width, height = self.img1.get_size() # button width height
        mx, my = pos # mouse x and mouse y
        
        flag1 = mx > self.x and mx < self.x + width # is pos inside x boundries
        flag2 = my > self.y and my < self.y + height # is pos inside y boundries
        
        return flag1 and flag2

    def reset(self):
        self.isPressed = False

    def trigger(self):
        self.isPressed = True
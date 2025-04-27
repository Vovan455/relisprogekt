import pygame


WIDTH = 1200
HEIGHT = 650
SIZE = (WIDTH, HEIGHT)
FPS = 60


window = pygame.display.set_mode(SIZE)
background = pygame.transform.scale(
    pygame.image.load("farm.jpg"),
    SIZE)
pygame.display.set_caption("Назва проекту. Автор: ....")
clock = pygame.time.Clock()

pygame.font.init()
medium_font = pygame.font.SysFont("Helvetica", 24)
big_font = pygame.font.SysFont("Impact", 50)

filds_pix = ["farm1.jpg","farm2.jpg","farm4.jpg","farm5.jpg"]

pygame.mixer.init()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename:str, size:tuple[int,int], coords: tuple[int,int], speed:int):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(filename), size)
        self.rect = self.image.get_rect(center=coords)
        self.speed = speed

    def reset(self, window:pygame.Surface):
        window.blit(self.image, self.rect)
class Field(GameSprite):
    def __init__(self, filename, size, coords, speed):
        super().__init__(filename, size, coords, speed)
        self.state = 1
    def update(self):
        if self.state<=len(filds_pix):     
            self.image = pygame.transform.scale(pygame.image.load(filds_pix[self.state-1]), self.rect.size) 
 #поля_________________________________________________________________________       
filds_nam = 27
filds:list[Field] = []
x,y=100,100
for i in range (3):
    for g in range(9):

        new_fild = Field("farm1.jpg",(100,100),(x,y),0)
        x += 120

        filds.append(new_fild)
    y+=160
    x=100
game = True
finish = False
restart = False
#____________________________________________________________________________________

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            for f in filds:
                if f.rect.collidepoint(event.pos):
                    f.state+=1
                    f.update()

    if not finish and not restart:
        window.blit(background, (0,0))
        for f in filds:
            f.reset(window)


    if restart:
        pass
    
    pygame.display.update()
    clock.tick(FPS)
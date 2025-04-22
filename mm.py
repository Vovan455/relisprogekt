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
        ...
        
filds_nam = 9
filds = []
x,y=10,10
for i in range (filds_nam):
    new_fild = Field("farm2.jpg",(100,100),(x,y),0)
    filds.append(new_fild)
game = True
finish = False
restart = False

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    if not finish and not restart:
        window.blit(background, (0,0))
        for f in filds:
            f.reset(window)


    if restart:
        pass
    
    pygame.display.update()
    clock.tick(FPS)
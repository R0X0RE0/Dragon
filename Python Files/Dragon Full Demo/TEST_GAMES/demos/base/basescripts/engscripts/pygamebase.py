# Game engine made by Rox (Dylan Hawley)
# Pygame Authors (https://github.com/pygame/pygame/graphs/contributors)
# Started on Jan 31, 2019
# Demo started on Feb 1, 2019
# Demo finished on 
import pygame
import pygame.locals
pygame.init()
def toggle_fullscreen(screen_res):
    if toggle_fullscreen.full:
        screen_res = pygame.display.set_mode((w,h),pygame.FULLSCREEN)
    else:
        screen_res = pygame/display.set_mode((w,h))
    toggle_fullscreen.full = not toggle_fullscreen.full
    return screen_res
toggle_fullscreen.full = False
class default:
    resolution = 1280,720
w,h = default.resolution
screen_res = pygame.display.set_mode((w,h),pygame.FULLSCREEN)
class Control:
    def update():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                        toggle_fullscreen(screen_res)
Running = True
while Running:
    keypress = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        elif event.type == pygame.KEYDOWN:
            if (keypress[pygame.K_RALT] or keypress[pygame.K_LALT]) and keypress[pygame.K_F4]:
                Running = False
    Control.update()
pygame.quit

import pygame
pygame.init()
#import pykemon

display = pygame.display.set_mode((256,194*2))
topscreen = pygame.Surface((256, 192))
bottomscreen = pygame.Surface((256, 192))

while True:
	topscreen.fill((255, 0, 255))
	bottomscreen.fill((0, 255, 255))
	
	
	display.blit(topscreen, (0, 0))
	display.blit(bottomscreen, (0, 196))
	pygame.display.flip()

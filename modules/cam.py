
import pygame
import pygame.camera
from pygame.locals import *
import time
pygame.init()
pygame.camera.init()

def snap():
	#avoir la liste des cameras connectees 
	camlist = pygame.camera.list_cameras()
	if False:
		#utiliser la camera numero 1
		cam = pygame.camera.Camera(camlist[0],(320,240))
		cam.start()
		#prendre photo,retourner la photo
		return cam.get_image()
	return None

import pygame
import math
#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		#print(self.rect.y)
		surface.blit(self.image, (self.rect.x, self.rect.y))
		print(self.rect)
		return action

	def scaling(self, old_screen_width , old_screen_height, new_screen_width, new_screen_height):
		x_scale = new_screen_width/old_screen_width
		y_scale = new_screen_height/old_screen_height
		old_x = self.rect.x
		old_y = self.rect.y
		#scaling image of the button
		self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * x_scale), int(self.image.get_height() * y_scale)))
		self.rect = self.image.get_rect()
		#scaling placement of the button
		self.rect.x = old_x * x_scale
		self.rect.y = old_y * y_scale

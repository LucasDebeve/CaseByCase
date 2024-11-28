import pygame
import numpy as np


class Map:
	"""
	Classe du terrain de jeu
	Le terrain de jeu est une matrice de 0, 1 et 2
	0: case vide
	1: case déja visitée
	2: case actuelle du joueur
	"""

	def __init__(self, width: int, height: int) -> None:
		self.width = width
		self.height = height
		self._map = np.zeros((width, height), dtype=int)

	@property
	def map(self) -> np.ndarray:
		return self._map

	def draw(self, screen: pygame.Surface) -> None:
		"""
		Dessine le terrain de jeu sur l'écran
		"""
		for x in range(self.width):
			for y in range(self.height):
				if self.map[x, y] == 1:
					color = (255, 255, 255)
				elif self.map[x, y] == 2:
					color = (255, 0, 0)
				else:
					color = (0, 0, 0)
				pygame.draw.rect(screen, color, (x * 10, y * 10, 10, 10))

	def updateCell(self, x: int, y: int, value: int) -> None:
		"""
		Met à jour la valeur d'une case du terrain
		"""
		self.map[x, y] = value

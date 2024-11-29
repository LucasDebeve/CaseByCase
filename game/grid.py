import numpy as np
import pygame


class Grid:
	VALUES = [0, 1]

	def __init__(self, width: int, height: int) -> None:
		self.__width = width
		self.__height = height
		self.__grid = np.zeros((width, height), dtype=int)
		self.__playerPos = None

	@property
	def width(self) -> int:
		return self.__width

	@property
	def height(self) -> int:
		return self.__height

	@property
	def grid(self) -> np.ndarray:
		return self.__grid

	@property
	def player(self):
		return self.__player

	@property
	def playerPos(self):
		return self.__playerPos

	@playerPos.setter
	def playerPos(self, value):
		self.__playerPos = value

	def toggle_cell(self, x: int, y: int) -> None:
		if x < 0 or x >= self.__width or y < 0 or y >= self.__height:
			raise IndexError("Cell out of bounds")
		self.__grid[x, y] = self.VALUES[
			(self.__grid[x, y] + 1) % len(self.VALUES)
		]

	def set_cell(self, x: int, y: int, value: int) -> None:
		if x < 0 or x >= self.__width or y < 0 or y >= self.__height:
			raise IndexError("Cell out of bounds")
		self.__grid[x, y] = value

	def clear(self) -> None:
		self.__grid = np.zeros((self.__width, self.__height), dtype=int)

	def randomize(self) -> None:
		self.__grid = np.random.randint(0, 2, (self.__width, self.__height))

	def display(self, screen: pygame.Surface) -> None:
		cell_size = min(
			screen.get_width() // self.__width,
			screen.get_height() // self.__height,
		)

		for x in range(self.__width):
			for y in range(self.__height):
				if self.__playerPos == (x, y):
					pygame.draw.rect(
						screen,
						(255, 255, 255),
						(y * cell_size, x * cell_size, cell_size, cell_size),
					)
				elif self.__grid[x, y] == 1:
					pygame.draw.rect(
						screen,
						(164, 164, 164),
						(y * cell_size, x * cell_size, cell_size, cell_size),
					)

	def __str__(self) -> str:
		return str(self.__grid)

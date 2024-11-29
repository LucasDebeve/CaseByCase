import asyncio
from game.grid import Grid


class Player:
	def __init__(self, x: int, y: int, grid: Grid) -> None:
		self.__x = x
		self.__y = y
		self.__grid = grid
		self.__grid.playerPos = (self.__x, self.__y)
		self.__readeyToMove = True

	@property
	def x(self) -> int:
		return self.__x

	@property
	def y(self) -> int:
		return self.__y

	async def move(self, dy: int, dx: int) -> None:
		if not self.__readeyToMove:
			return
		if (
			(self.__x + dx) < 0
			or (self.__y + dy) < 0
			or (self.__x + dx) >= self.__grid.width
			or (self.__y + dy) >= self.__grid.height
		):
			return
		self.__grid.toggle_cell(self.__x, self.__y)
		self.__x += dx
		self.__y += dy
		self.__grid.playerPos = (self.__x, self.__y)
		self.__readeyToMove = False
		# await asyncio.sleep(0.5)
		await asyncio.sleep(0.2)
		self.__readeyToMove = True

	def __str__(self) -> str:
		return f"Player at ({self.__x}, {self.__y})"

from game.grid import Grid


class Player:
	def __init__(self, x: int, y: int, grid: Grid) -> None:
		self.__x = x
		self.__y = y
		self.__grid = grid
		self.__grid.set_cell(self.__x, self.__y, 2)

	@property
	def x(self) -> int:
		return self.__x

	@property
	def y(self) -> int:
		return self.__y

	def move(self, dy: int, dx: int, grid: Grid) -> None:
		if (
			(self.__x + dx) < 0
			or (self.__y + dy) < 0
			or (self.__x + dx) >= grid.width
			or (self.__y + dy) >= grid.height
		):
			return
		self.__grid.set_cell(self.__x, self.__y, 1)
		self.__x += dx
		self.__y += dy
		self.__grid.set_cell(self.__x, self.__y, 2)

	def __str__(self) -> str:
		return f"Player at ({self.__x}, {self.__y})"

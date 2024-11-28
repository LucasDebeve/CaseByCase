# Example file showing a basic pygame "game loop"
import pygame
from pygame.locals import QUIT


class Game:
	def __init__(self, width: int, height: int) -> None:
		self.width = width
		self.height = height
		self.fps = 30

	def run(self) -> None:
		pygame.init()
		screen = pygame.display.set_mode((self.width, self.height))
		clock = pygame.time.Clock()

		running = True
		while running:
			for event in pygame.event.get():
				if event.type == QUIT:
					running = False

			screen.fill((0, 0, 0))
			pygame.display.flip()
			clock.tick(self.fps)

		pygame.quit()


if __name__ == "__main__":
	game = Game(800, 600)
	game.run()

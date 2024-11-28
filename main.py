import pygame
from settings import WINDOW_HEIGHT, WINDOW_WIDTH, GRID_SIZE, FPS
from game.grid import Grid

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Case By Case")
clock = pygame.time.Clock()

grid = Grid(GRID_SIZE, GRID_SIZE)
grid.randomize()


def main():
	running = True
	while running:
		# Gérer les événements
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# Affichage
		screen.fill((0, 0, 0))
		grid.display(screen)
		pygame.display.flip()

		# Limiter la vitesse de la boucle
		clock.tick(FPS)

	pygame.quit()


if __name__ == "__main__":
	main()

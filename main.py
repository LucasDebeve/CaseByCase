import pygame

from game.grid import Grid
from game.player import Player
from settings import FPS, GRID_SIZE, WINDOW_HEIGHT, WINDOW_WIDTH

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Case By Case")
clock = pygame.time.Clock()

grid = Grid(GRID_SIZE, GRID_SIZE)
player = Player(0, 0, grid)
grid.randomize()


def main():
	running = True
	while running:
		# Gérer les événements
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# Mise à jour
		# Key released
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player.move(0, -1, grid)
			elif event.key == pygame.K_DOWN:
				player.move(0, 1, grid)
			elif event.key == pygame.K_LEFT:
				player.move(-1, 0, grid)
			elif event.key == pygame.K_RIGHT:
				player.move(1, 0, grid)

		# Affichage
		screen.fill((0, 0, 0))
		grid.display(screen)
		pygame.display.flip()

		# Limiter la vitesse de la boucle
		clock.tick(FPS)

	pygame.quit()


if __name__ == "__main__":
	main()

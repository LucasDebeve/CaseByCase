import pytest
from game.grid import Grid
import pygame


class TestGrid:
	@pytest.fixture
	def grid(self):
		"""Fixture pour initialiser une grille de 6x6"""
		return Grid(6, 6)

	@pytest.fixture
	def screen(self):
		"""Fixture pour initialiser une surface Pygame pour les tests."""
		pygame.init()
		screen = pygame.Surface((500, 500))  # Surface de 500x500 pixels
		return screen

	def test_initial_grid(self, grid):
		"""Teste si la grille est bien initialisée avec des 0"""
		assert grid.grid.shape == (6, 6)
		assert grid.grid.sum() == 0

	def test_toggle_cell(self, grid):
		"""Teste le basculement d'une cellule"""
		grid.toggle_cell(0, 0)
		assert grid.grid[0, 0] == 1
		grid.toggle_cell(0, 0)
		assert grid.grid[0, 0] == 0

	def test_out_of_bounds_toggle(self, grid):
		"""Test qu'un basculement hors des limites soulève une exception."""
		with pytest.raises(IndexError):
			grid.toggle_cell(-1, 0)
		with pytest.raises(IndexError):
			grid.toggle_cell(6, 6)

	def test_clear(self, grid):
		"""Teste que la grille est bien vidée"""
		grid.toggle_cell(0, 0)
		grid.toggle_cell(1, 1)
		grid.clear()
		assert grid.grid.sum() == 0

	def test_display_output(self, grid: Grid, screen: pygame.Surface):
		"""Teste que la méthode display affiche bien les cellules"""
		# Activer certaines cases
		grid.toggle_cell(0, 0)  # Activer la case (0, 0)
		grid.toggle_cell(4, 4)  # Activer la case (4, 4)

		# Dessiner la grille sur la surface
		grid.display(screen)

		cell_size = 500 // 6  # Taille d'une case
		assert screen.get_at((cell_size // 2, cell_size // 2)) == pygame.Color(
			164, 164, 164
		), "La case (0, 0) doit être grise"
		assert screen.get_at(
			(4 * cell_size + cell_size // 2, 4 * cell_size + cell_size // 2)
		) == pygame.Color(164, 164, 164), "La case (4, 4) doit être grise"
		assert screen.get_at((2 * cell_size, 2 * cell_size)) == pygame.Color(
			0, 0, 0
		), "La case (2, 2) doit être noire"

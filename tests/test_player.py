import asyncio
import pytest
from game.player import Player


class TestPlayer:
	@pytest.fixture
	def player(self):
		return Player(2, 2)

	def test_initial_position(self, player):
		assert player.x == 2
		assert player.y == 2

	@pytest.mark.parametrize(
		"dx, dy, expected_x, expected_y",
		[
			(0, 1, 2, 3),
			(0, -1, 2, 1),
			(1, 0, 3, 2),
			(-1, 0, 1, 2),
		],
	)
	def test_player_move(self, player, dx, dy, expected_x, expected_y):
		asyncio.run(player.move(dy, dx))
		assert player.x == expected_x
		assert player.y == expected_y

	@pytest.mark.parametrize(
		"dx, dy",
		[
			(0, -1),
			(-1, 0),
			(0, 8),
			(8, 0),
		],
	)
	def test_player_dont_move_with_impossible_move(self, dx, dy):
		player = Player(0, 0)
		asyncio.run(player.move(dy, dx))
		assert player.x == 0
		assert player.y == 0

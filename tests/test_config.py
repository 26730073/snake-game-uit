"""Kiểm thử cơ bản, dùng để chắc chắn dự án import được.

Chạy toàn bộ test:  python -m pytest
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from snake import config


def test_window_size_matches_grid():
    assert config.WINDOW_WIDTH == config.CELL_SIZE * config.GRID_WIDTH
    assert config.WINDOW_HEIGHT == config.CELL_SIZE * config.GRID_HEIGHT


def test_difficulty_speeds_are_ordered():
    assert config.SPEED_EASY < config.SPEED_NORMAL < config.SPEED_HARD

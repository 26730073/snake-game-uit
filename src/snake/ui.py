"""Vẽ giao diện: lưới, chữ, menu, màn hình game over.

Người phụ trách: Đặng Đức Tín (26730073)
"""

from __future__ import annotations

import pygame

from . import config


def draw_grid(surface: pygame.Surface) -> None:
    """Vẽ nền và các đường kẻ lưới."""
    surface.fill(config.COLOR_BACKGROUND)
    for x in range(0, config.WINDOW_WIDTH, config.CELL_SIZE):
        pygame.draw.line(
            surface, config.COLOR_GRID, (x, 0), (x, config.WINDOW_HEIGHT)
        )
    for y in range(0, config.WINDOW_HEIGHT, config.CELL_SIZE):
        pygame.draw.line(
            surface, config.COLOR_GRID, (0, y), (config.WINDOW_WIDTH, y)
        )


def draw_text(
    surface: pygame.Surface,
    text: str,
    size: int,
    center: tuple[int, int],
    color: tuple[int, int, int] = config.COLOR_TEXT,
) -> None:
    """Vẽ một dòng chữ căn giữa tại toạ độ `center`."""
    font = pygame.font.Font(None, size)
    rendered = font.render(text, True, color)
    surface.blit(rendered, rendered.get_rect(center=center))


def draw_snake(surface: pygame.Surface, body: list[tuple[int, int]]) -> None:
    """Vẽ thân rắn lên màn hình."""
    # TODO(Tín): duyệt `body`, đốt đầu tiên tô COLOR_SNAKE_HEAD,
    # các đốt còn lại tô COLOR_SNAKE_BODY.
    raise NotImplementedError("Chưa cài đặt draw_snake")


def draw_food(surface: pygame.Surface, position: tuple[int, int]) -> None:
    """Vẽ miếng mồi lên màn hình."""
    # TODO(Tín)
    raise NotImplementedError("Chưa cài đặt draw_food")


def draw_score(surface: pygame.Surface, score: int, highscore: int) -> None:
    """Hiển thị điểm hiện tại và điểm cao nhất ở góc màn hình."""
    # TODO(Tín)
    raise NotImplementedError("Chưa cài đặt draw_score")


def draw_menu(surface: pygame.Surface) -> None:
    """Màn hình menu: tên game, hướng dẫn chọn độ khó, phím bắt đầu."""
    # TODO(Tín)
    raise NotImplementedError("Chưa cài đặt draw_menu")


def draw_game_over(surface: pygame.Surface, score: int) -> None:
    """Màn hình kết thúc: điểm đạt được, phím chơi lại, phím thoát."""
    # TODO(Tín)
    raise NotImplementedError("Chưa cài đặt draw_game_over")

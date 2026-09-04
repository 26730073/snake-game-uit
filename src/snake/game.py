"""Vòng lặp chính, trạng thái game, xử lý va chạm và tính điểm.

Người phụ trách: Hồ Văn Trọng (26730077)

Hiện tại lớp Game mới chỉ mở cửa sổ và vẽ lưới trống, dùng để cả nhóm
kiểm tra máy đã cài pygame đúng chưa. Phần chơi thật sẽ được viết dần
theo các TODO bên dưới.
"""

from __future__ import annotations

import pygame

from . import config, ui


class Game:
    """Điều phối toàn bộ game."""

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(
            (config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
        )
        pygame.display.set_caption(config.WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0

        # TODO(Trọng): khởi tạo self.snake = Snake(...) và self.food = Food(...)
        # TODO(Trọng): thêm self.state để phân biệt MENU / PLAYING / PAUSED / GAME_OVER

    def handle_events(self) -> None:
        """Đọc bàn phím và sự kiện đóng cửa sổ."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            # TODO(Trọng): map phím mũi tên và WASD sang snake.change_direction()
            # TODO(Trọng): phím P để tạm dừng, phím Space để bắt đầu / chơi lại

    def update(self) -> None:
        """Cập nhật trạng thái game sau mỗi bước."""
        # TODO(Trọng): cho rắn đi một bước
        # TODO(Trọng): nếu đầu rắn trùng vị trí mồi thì cộng điểm và sinh mồi mới
        # TODO(Trọng): kiểm tra va chạm tường và va chạm thân → chuyển sang GAME_OVER

    def draw(self) -> None:
        """Vẽ toàn bộ khung hình."""
        ui.draw_grid(self.screen)

        # Màn hình tạm để kiểm tra môi trường. Xoá khi game chạy thật.
        ui.draw_text(
            self.screen,
            "SNAKE GAME - NHOM 3 UIT",
            48,
            (config.WINDOW_WIDTH // 2, config.WINDOW_HEIGHT // 2 - 30),
        )
        ui.draw_text(
            self.screen,
            "Moi truong da san sang. Bat dau code thoi!",
            26,
            (config.WINDOW_WIDTH // 2, config.WINDOW_HEIGHT // 2 + 20),
            config.COLOR_TEXT_DIM,
        )
        ui.draw_text(
            self.screen,
            "Nhan ESC de thoat",
            22,
            (config.WINDOW_WIDTH // 2, config.WINDOW_HEIGHT // 2 + 55),
            config.COLOR_TEXT_DIM,
        )

        # TODO(Trọng): thay 3 dòng chữ trên bằng ui.draw_snake / draw_food /
        # draw_score, và vẽ menu hoặc game over tuỳ theo self.state.

        pygame.display.flip()

    def run(self) -> None:
        """Vòng lặp game."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(config.FPS)
        pygame.quit()

"""Các hằng số cấu hình của game.

Người phụ trách: Đặng Đức Tín (26730073)

Mọi con số "ma thuật" (magic number) đều nên đặt tên ở đây thay vì viết
thẳng trong code, để cả nhóm chỉnh một chỗ là toàn bộ game đổi theo.
"""

# --- Kích thước cửa sổ và lưới -------------------------------------------
CELL_SIZE = 20          # Kích thước một ô vuông (pixel)
GRID_WIDTH = 30         # Số ô theo chiều ngang
GRID_HEIGHT = 22        # Số ô theo chiều dọc

WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT

WINDOW_TITLE = "Snake Game - Nhom 3 - UIT"

# --- Tốc độ ---------------------------------------------------------------
FPS = 60                # Số khung hình mỗi giây

# Số bước rắn đi được trong 1 giây, ứng với từng mức độ khó
SPEED_EASY = 8
SPEED_NORMAL = 12
SPEED_HARD = 18

# --- Màu sắc (R, G, B) ----------------------------------------------------
COLOR_BACKGROUND = (18, 24, 32)
COLOR_GRID = (28, 36, 46)
COLOR_SNAKE_HEAD = (86, 214, 122)
COLOR_SNAKE_BODY = (58, 168, 96)
COLOR_FOOD = (232, 84, 84)
COLOR_TEXT = (236, 240, 244)
COLOR_TEXT_DIM = (140, 152, 166)

# --- Điểm số --------------------------------------------------------------
SCORE_PER_FOOD = 10
HIGHSCORE_FILE = "highscore.json"

# TODO(Tín): bổ sung đường dẫn tới file âm thanh và font chữ trong assets/

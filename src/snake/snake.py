"""Đối tượng con rắn.

Người phụ trách: Lê Kiều Diễm (26730010)
"""

from __future__ import annotations

# Hướng di chuyển biểu diễn bằng vector (dx, dy) trên lưới ô vuông
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    """Quản lý thân rắn và hành vi di chuyển.

    Thân rắn là một danh sách các toạ độ ô ``(x, y)``, phần tử đầu tiên
    ``body[0]`` chính là đầu rắn.
    """

    def __init__(self, start_x: int, start_y: int, length: int = 3) -> None:
        # TODO(Diễm): khởi tạo self.body gồm `length` đốt nằm ngang,
        # đầu rắn ở (start_x, start_y), các đốt sau nằm bên trái đầu.
        # TODO(Diễm): khởi tạo self.direction = RIGHT
        raise NotImplementedError("Chưa cài đặt Snake.__init__")

    @property
    def head(self) -> tuple[int, int]:
        """Toạ độ ô của đầu rắn."""
        return self.body[0]

    def change_direction(self, new_direction: tuple[int, int]) -> None:
        """Đổi hướng đi.

        Lưu ý: rắn không được quay ngược 180 độ. Ví dụ đang đi RIGHT thì
        bấm LEFT phải bị bỏ qua, nếu không rắn sẽ tự đâm vào thân mình.
        """
        # TODO(Diễm): chặn trường hợp quay ngược rồi mới gán self.direction
        raise NotImplementedError("Chưa cài đặt Snake.change_direction")

    def move(self, grow: bool = False) -> None:
        """Đi tới một ô theo hướng hiện tại.

        Args:
            grow: True nếu rắn vừa ăn mồi (dài thêm 1 đốt, không bỏ đuôi).
        """
        # TODO(Diễm): tính ô mới = head + direction, chèn vào đầu self.body.
        # Nếu grow là False thì xoá đốt cuối (self.body.pop()).
        raise NotImplementedError("Chưa cài đặt Snake.move")

    def hits_self(self) -> bool:
        """Trả về True nếu đầu rắn trùng với một đốt trên thân."""
        # TODO(Diễm)
        raise NotImplementedError("Chưa cài đặt Snake.hits_self")

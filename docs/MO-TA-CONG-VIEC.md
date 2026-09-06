# Bản mô tả công việc chi tiết

Đồ án Snake Game — Nhóm 3 — Trường Đại học Công nghệ Thông tin, ĐHQG TP.HCM
Cập nhật: 06/09/2026

---

## Mục lục

- [Nguyên tắc chung cho cả nhóm](#nguyên-tắc-chung-cho-cả-nhóm)
- [Phần I — Hồ Văn Trọng (26730077)](#phần-i--hồ-văn-trọng-26730077)
- [Phần II — Lê Kiều Diễm (26730010)](#phần-ii--lê-kiều-diễm-26730010)
- [Phần III — Đặng Đức Tín (26730073)](#phần-iii--đặng-đức-tín-26730073)
- [Việc chung của cả nhóm](#việc-chung-của-cả-nhóm)
- [Bảng tổng hợp khối lượng](#bảng-tổng-hợp-khối-lượng)
- [Lộ trình 6 tuần](#lộ-trình-6-tuần)

---

## Nguyên tắc chung cho cả nhóm

**Cách đọc tài liệu này.** Mỗi đầu việc đều có 5 mục: *Mục tiêu* nói làm cái gì,
*Đầu vào — đầu ra* nói hàm nhận gì và trả gì, *Gợi ý thực hiện* chỉ hướng đi mà
không đưa code sẵn, *Nghiệm thu* là điều kiện để coi việc đó đã xong, *Ước lượng*
là thời gian dự kiến cho người mới học.

**Tại sao chia việc theo file.** Git gộp code tự động rất tốt khi hai người sửa
hai file khác nhau, nhưng sẽ báo conflict khi hai người cùng sửa một dòng. Chia
theo file là cách đơn giản nhất để cả nhóm gần như không bao giờ gặp conflict.

**Ranh giới giữa các phần.** Ba người giao tiếp với nhau qua *interface* — tức là
tên hàm và kiểu dữ liệu đã thống nhất sẵn trong khung code. Diễm không cần biết
Trọng vẽ màn hình thế nào, chỉ cần `Snake.move()` chạy đúng. Trọng không cần biết
Tín tô màu gì, chỉ cần gọi `ui.draw_snake(screen, body)` là ra hình.

**Nếu muốn đổi interface** — ví dụ đổi tên hàm, thêm tham số — thì phải báo nhóm
trước, vì thay đổi đó ảnh hưởng tới code của người khác.

**Quy ước dữ liệu dùng chung:**

| Khái niệm | Kiểu dữ liệu | Ví dụ | Ghi chú |
|-----------|--------------|-------|---------|
| Toạ độ một ô | `tuple[int, int]` | `(5, 12)` | Đơn vị là **ô lưới**, không phải pixel |
| Thân rắn | `list[tuple[int, int]]` | `[(5,10), (4,10), (3,10)]` | Phần tử `[0]` luôn là đầu rắn |
| Hướng đi | `tuple[int, int]` | `(1, 0)` | Vector dịch chuyển, xem hằng số trong `snake.py` |
| Màu sắc | `tuple[int, int, int]` | `(86, 214, 122)` | RGB, khai báo trong `config.py` |

Gốc toạ độ `(0, 0)` nằm ở **góc trên bên trái**. Trục `y` tăng khi đi **xuống dưới**
— đây là quy ước của pygame, khác với toán học phổ thông, rất dễ nhầm.

---

## Phần I — Hồ Văn Trọng (26730077)

**Vai trò:** Nhóm trưởng, phụ trách phần lõi điều khiển game.
**File phụ trách:** `src/snake/game.py`
**Không được sửa:** `snake.py`, `food.py`, `ui.py`, `config.py` (báo chủ file nếu cần)

Phần của Trọng là "bộ não" của game: nhận phím từ người chơi, ra lệnh cho rắn đi,
kiểm tra thua chưa, cộng điểm, và quyết định mỗi khung hình vẽ cái gì lên màn hình.
Đây là phần khó nhất vì nó phụ thuộc vào code của cả hai bạn còn lại.

### T1. Quản lý trạng thái game

**Mục tiêu.** Game phải phân biệt được người chơi đang ở đâu: đang xem menu, đang
chơi, đang tạm dừng, hay đã thua. Nếu không có khái niệm trạng thái, code sẽ biến
thành một mớ `if` chồng chéo rất khó sửa.

**Đầu vào — đầu ra.** Thêm thuộc tính `self.state` vào lớp `Game`. Giá trị lấy từ
một lớp hằng số hoặc `enum.Enum` với 4 giá trị: `MENU`, `PLAYING`, `PAUSED`,
`GAME_OVER`.

**Gợi ý thực hiện.** Dùng `enum.Enum` cho gọn và tránh gõ nhầm chuỗi. Vẽ ra giấy
sơ đồ chuyển trạng thái trước khi code — hình này cũng dùng được luôn cho báo cáo:

```
MENU --[Space]--> PLAYING --[P]--> PAUSED --[P]--> PLAYING
                     |
                  [va chạm]
                     v
                 GAME_OVER --[Space]--> PLAYING
```

Cả `update()` và `draw()` đều bắt đầu bằng việc kiểm tra `self.state` rồi rẽ nhánh.
Khi ở `MENU`, `PAUSED` hay `GAME_OVER` thì `update()` không được cho rắn đi.

**Nghiệm thu.**
- [ ] Mở game lên thấy menu, không nhảy thẳng vào màn chơi
- [ ] Bấm `P` lúc đang chơi thì rắn đứng yên, bấm `P` lần nữa thì đi tiếp
- [ ] Thua rồi bấm `Space` thì ván mới bắt đầu với điểm 0 và rắn 3 đốt

**Ước lượng.** 2–3 giờ.

### T2. Nhận phím điều khiển

**Mục tiêu.** Người chơi lái rắn được bằng cả phím mũi tên lẫn WASD.

**Đầu vào — đầu ra.** Viết trong hàm `handle_events()`. Mỗi sự kiện
`pygame.KEYDOWN` được ánh xạ sang một lời gọi `self.snake.change_direction(...)`.

**Gợi ý thực hiện.** Đừng viết 8 câu `if` cho 8 phím. Tạo một `dict` ánh xạ mã phím
sang hướng:

```python
KEY_TO_DIRECTION = {
    pygame.K_UP: snake_module.UP,
    pygame.K_w: snake_module.UP,
    # ... 6 dòng còn lại
}
```

Rồi tra `dict` một lần. Cách này ngắn hơn, dễ thêm phím mới, và người review đọc
hiểu ngay.

**Cạm bẫy thường gặp.** Nếu người chơi bấm rất nhanh `LÊN` rồi `TRÁI` trong cùng
một bước đi của rắn, rắn đang đi `PHẢI` sẽ nhận `LÊN` (hợp lệ) rồi nhận `TRÁI`
(cũng hợp lệ so với `PHẢI` hiện tại vì rắn chưa kịp đi) — kết quả là rắn quay ngược
180 độ và tự cắn mình. Cách xử lý: lưu hướng người chơi bấm vào một biến chờ
`self.pending_direction`, và chỉ gọi `change_direction()` một lần ngay trước khi
rắn di chuyển trong `update()`.

**Nghiệm thu.**
- [ ] Cả 4 phím mũi tên và 4 phím WASD đều lái được rắn
- [ ] Bấm hai phím thật nhanh không làm rắn quay ngược tự cắn mình
- [ ] `ESC` thoát game, `P` tạm dừng, `Space` bắt đầu và chơi lại

**Ước lượng.** 2–3 giờ.

### T3. Điều khiển tốc độ rắn

**Mục tiêu.** Rắn đi đúng số bước mỗi giây theo mức độ khó, và tốc độ đó **không
phụ thuộc vào máy nhanh hay chậm**.

**Đầu vào — đầu ra.** Hằng số `SPEED_EASY = 8`, `SPEED_NORMAL = 12`,
`SPEED_HARD = 18` trong `config.py` nghĩa là 8, 12, 18 bước mỗi giây.

**Gợi ý thực hiện.** Vòng lặp game chạy 60 khung hình/giây (`config.FPS`), nhưng
rắn chỉ được đi 12 bước/giây. Vậy không phải khung hình nào cũng cho rắn đi. Cách
làm: cộng dồn thời gian trôi qua vào một biến tích luỹ, khi nào đủ `1 / speed`
giây thì mới cho rắn đi một bước và trừ ngược lại.

```python
self.move_timer += self.clock.get_time() / 1000  # đổi mili-giây sang giây
if self.move_timer >= 1 / self.speed:
    self.move_timer -= 1 / self.speed
    # cho rắn đi ở đây
```

**Vì sao không dùng `clock.tick(speed)`.** Cách đó cũng chạy được nhưng làm cả
game giật cục ở 12 khung hình/giây, hiệu ứng và chữ trên màn hình sẽ nhấp nháy khó
chịu. Tách riêng nhịp vẽ và nhịp đi là cách làm chuẩn.

**Nghiệm thu.**
- [ ] Đếm bằng đồng hồ: mức Thường, rắn đi khoảng 12 ô trong 1 giây
- [ ] Chuyển sang mức Khó thì rắn nhanh hơn thấy rõ
- [ ] Màn hình vẫn mượt, chữ không nhấp nháy

**Ước lượng.** 2 giờ. Đây là phần khó nhất về mặt tư duy, làm sớm và hỏi nếu kẹt.

### T4. Xử lý ăn mồi và va chạm

**Mục tiêu.** Ghép các mảnh của Diễm lại thành luật chơi hoàn chỉnh.

**Gợi ý thực hiện.** Thứ tự kiểm tra trong `update()` rất quan trọng:

1. Tính trước ô mà đầu rắn sắp tới
2. Ô đó có trùng vị trí mồi không? → nếu có thì `grow=True`
3. Gọi `self.snake.move(grow)`
4. Nếu vừa ăn: cộng `config.SCORE_PER_FOOD` điểm, gọi `self.food.respawn(self.snake.body)`
5. Kiểm tra đầu rắn có ra ngoài lưới không → thua
6. Kiểm tra `self.snake.hits_self()` → thua

**Cạm bẫy.** Phải gọi `respawn()` **sau khi** rắn đã dài ra, và truyền vào thân rắn
mới nhất. Nếu truyền thân cũ, mồi có thể sinh trúng ngay dưới bụng rắn.

**Nghiệm thu.**
- [ ] Ăn mồi thì rắn dài thêm đúng 1 đốt và điểm tăng 10
- [ ] Mồi mới không bao giờ nằm chồng lên thân rắn
- [ ] Đâm vào 4 cạnh màn hình đều thua
- [ ] Cho rắn dài ra rồi cố tình cắn thân, phải thua

**Ước lượng.** 3 giờ.

### T5. Lưu điểm cao nhất

**Mục tiêu.** Tắt game mở lại vẫn nhớ kỷ lục cũ.

**Gợi ý thực hiện.** Ghi ra file `highscore.json` bằng thư viện `json` có sẵn.
Bọc phần đọc file trong `try/except` — lần chạy đầu tiên file chưa tồn tại, và
file cũng có thể bị hỏng nếu tắt máy giữa chừng. Trường hợp lỗi thì trả về 0,
tuyệt đối không để game crash chỉ vì thiếu file điểm.

File `highscore.json` đã có trong `.gitignore` nên sẽ không bị commit lên — đúng
như mong muốn, vì điểm của mỗi máy là khác nhau.

**Nghiệm thu.**
- [ ] Chơi được 50 điểm, tắt game, mở lại vẫn thấy kỷ lục 50
- [ ] Xoá file `highscore.json` rồi mở game, không lỗi, kỷ lục về 0
- [ ] Sửa nội dung file thành chữ bậy bạ rồi mở game, không lỗi

**Ước lượng.** 1–2 giờ.

### T6. Trách nhiệm quản lý nhóm

Ngoài code, Trọng còn phụ trách:

- **Duyệt Pull Request.** Đọc code, chạy thử trên máy mình, góp ý cụ thể. Không để
  PR của bạn nào treo quá 2 ngày.
- **Cập nhật Issue.** Đóng issue khi việc đã xong, tạo issue mới khi phát sinh.
- **Nhắc tiến độ.** Mỗi tuần hỏi han một lần trong nhóm Zalo.
- **Gỡ rối kỹ thuật.** Là người đọc `docs/HUONG-DAN-GIT.md` kỹ nhất để hỗ trợ hai
  bạn khi kẹt Git.
- **Nộp bài.** Giữ liên lạc với giảng viên, nắm deadline, chịu trách nhiệm nộp đúng hạn.

**Ước lượng.** 1 giờ mỗi tuần, kéo dài suốt đồ án.

---

## Phần II — Lê Kiều Diễm (26730010)

**Vai trò:** Phụ trách logic đối tượng trong game.
**File phụ trách:** `src/snake/snake.py`, `src/snake/food.py`, và các file test tương ứng
**Không được sửa:** `game.py`, `ui.py`, `config.py`

Phần của Diễm là **thuần logic, không dính gì tới đồ hoạ**. Không cần mở cửa sổ
game vẫn kiểm tra được code đúng hay sai — chỉ cần chạy test. Đây là lợi thế lớn:
Diễm có thể làm xong và chứng minh code chạy đúng ngay cả khi phần của Trọng và
Tín chưa xong.

### D1. Khởi tạo con rắn — `Snake.__init__`

**Mục tiêu.** Tạo con rắn ban đầu gồm 3 đốt nằm ngang.

**Đầu vào — đầu ra.** Nhận `start_x`, `start_y` (toạ độ ô của đầu rắn) và `length`
(số đốt, mặc định 3). Sau khi chạy xong phải có `self.body` là danh sách toạ độ và
`self.direction` bằng `RIGHT`.

**Gợi ý thực hiện.** Rắn đi sang phải nên thân phải nằm bên trái đầu. Với đầu ở
`(10, 5)` và `length = 3`, kết quả đúng là:

```python
[(10, 5), (9, 5), (8, 5)]
```

Dùng list comprehension với `range(length)` để tạo, đừng viết cứng 3 phần tử.

**Nghiệm thu.**
- [ ] `len(snake.body) == length`
- [ ] `snake.body[0] == (start_x, start_y)`
- [ ] `snake.direction == RIGHT`
- [ ] Gọi với `length=5` vẫn ra đúng 5 đốt

**Ước lượng.** 1 giờ.

### D2. Đổi hướng — `Snake.change_direction`

**Mục tiêu.** Đổi hướng đi, nhưng chặn thao tác quay ngược 180 độ.

**Vì sao phải chặn.** Rắn đang đi sang phải, nếu cho quay ngay sang trái thì đầu
rắn sẽ lùi vào đúng ô của đốt thứ hai — tức là tự cắn mình và thua ngay lập tức.
Mọi bản Snake đều chặn thao tác này.

**Gợi ý thực hiện.** Hai hướng ngược nhau có tổng vector bằng `(0, 0)`. Ví dụ
`RIGHT = (1, 0)` và `LEFT = (-1, 0)`, cộng lại được `(0, 0)`. Dựa vào tính chất này
để viết điều kiện kiểm tra rất gọn, không cần liệt kê 4 trường hợp.

Nếu hướng mới bị chặn thì **bỏ qua im lặng**, giữ nguyên hướng cũ — đừng báo lỗi,
vì người chơi bấm nhầm là chuyện bình thường.

**Nghiệm thu.**
- [ ] Đang `RIGHT`, gọi `change_direction(LEFT)` → hướng vẫn là `RIGHT`
- [ ] Đang `RIGHT`, gọi `change_direction(UP)` → hướng đổi thành `UP`
- [ ] Thử đủ 4 cặp hướng ngược nhau, cặp nào cũng bị chặn

**Ước lượng.** 1 giờ.

### D3. Di chuyển — `Snake.move`

**Mục tiêu.** Cho rắn đi một ô, có thể dài ra nếu vừa ăn mồi.

**Đầu vào — đầu ra.** Nhận `grow: bool`. Không trả về gì, chỉ thay đổi `self.body`.

**Gợi ý thực hiện.** Mẹo kinh điển của game Snake: **rắn không "trượt" cả thân,
mà chỉ mọc thêm một đốt ở đầu và cắt bỏ một đốt ở đuôi.**

1. Tính ô mới: cộng từng thành phần của `self.head` với `self.direction`
2. `self.body.insert(0, ô_mới)`
3. Nếu `grow` là `False` thì `self.body.pop()` để bỏ đuôi

Khi `grow=True`, ta chỉ bỏ qua bước 3 — thế là rắn dài thêm đúng 1 đốt. Cách này
chạy nhanh vì không phải duyệt lại toàn bộ thân rắn.

**Nghiệm thu.**
- [ ] Đi 1 bước với `grow=False`: độ dài không đổi, đầu dịch đúng 1 ô
- [ ] Đi 1 bước với `grow=True`: độ dài tăng 1, đuôi giữ nguyên vị trí cũ
- [ ] Đi 10 bước liên tiếp, đầu rắn dịch đúng 10 ô

**Ước lượng.** 1–2 giờ.

### D4. Phát hiện tự cắn — `Snake.hits_self`

**Mục tiêu.** Trả về `True` khi đầu rắn nằm trùng lên một đốt thân.

**Gợi ý thực hiện.** Chỉ cần kiểm tra `self.head` có nằm trong `self.body[1:]` hay
không. Lưu ý phải cắt từ phần tử thứ 1 trở đi — nếu so với cả `self.body` thì đầu
rắn luôn trùng chính nó và hàm sẽ luôn trả về `True`.

**Nghiệm thu.**
- [ ] Rắn 3 đốt thẳng hàng → `False`
- [ ] Tự tạo một `body` có đầu trùng đốt thứ 4 → `True`
- [ ] Rắn dài 20 đốt cuộn tròn nhưng đầu chưa chạm thân → `False`

**Ước lượng.** 30 phút.

### D5. Sinh mồi — `Food.respawn`

**Mục tiêu.** Đặt mồi vào một ô trống ngẫu nhiên, **tuyệt đối không trùng thân rắn**.

**Đầu vào — đầu ra.** Nhận `occupied` là danh sách các ô đang bị rắn chiếm. Gán
kết quả vào `self.position`.

**Gợi ý thực hiện.** Có hai cách, hãy chọn cách thứ hai:

*Cách sai lầm phổ biến:* random đại một ô, nếu trùng thân rắn thì random lại, lặp
mãi tới khi được. Cách này chạy được lúc rắn ngắn, nhưng khi rắn dài chiếm gần hết
màn hình thì vòng lặp có thể quay hàng nghìn lần, thậm chí treo vĩnh viễn nếu bàn
cờ đã đầy.

*Cách nên dùng:* tạo danh sách **tất cả** ô hợp lệ, loại bỏ các ô trong `occupied`,
rồi `random.choice()` một lần duy nhất. Luôn chạy nhanh và không bao giờ treo.

```python
free = [(x, y)
        for x in range(config.GRID_WIDTH)
        for y in range(config.GRID_HEIGHT)
        if (x, y) not in occupied]
```

Nhớ xử lý trường hợp `free` rỗng — nghĩa là người chơi đã thắng tuyệt đối, phủ kín
màn hình. Hiếm nhưng nên có, và ghi vào báo cáo như một tình huống biên đã lường trước.

**Nghiệm thu.**
- [ ] Chạy 1000 lần với thân rắn cho trước, không lần nào mồi trùng thân
- [ ] Mồi luôn nằm trong lưới, không âm và không vượt `GRID_WIDTH/HEIGHT`
- [ ] Bàn cờ đầy thì không crash

**Ước lượng.** 1–2 giờ.

### D6. Viết test cho phần của mình

**Mục tiêu.** Chứng minh code chạy đúng bằng bằng chứng, không phải bằng lời nói.

**Đầu ra.** Hai file `tests/test_snake.py` và `tests/test_food.py`.

**Gợi ý thực hiện.** Xem `tests/test_config.py` làm mẫu về cách import. Mỗi hàm
test đặt tên bắt đầu bằng `test_`, mô tả rõ điều đang kiểm tra:

```python
def test_khong_cho_quay_nguoc_180_do():
    s = Snake(10, 5)
    s.change_direction(LEFT)
    assert s.direction == RIGHT
```

Chạy toàn bộ test bằng `python -m pytest -v`.

**Giá trị cho báo cáo.** Phần test này là điểm cộng rõ rệt khi chấm — rất ít nhóm
sinh viên viết test. Nhớ chụp màn hình kết quả pytest xanh hết để đưa vào báo cáo.

**Nghiệm thu.**
- [ ] Ít nhất 10 test, bao được cả 5 hàm ở trên
- [ ] Có test cho trường hợp biên: rắn dài 1 đốt, mồi khi bàn gần đầy
- [ ] `python -m pytest` pass hết, CI trên GitHub hiện dấu tích xanh

**Ước lượng.** 2–3 giờ.

---

## Phần III — Đặng Đức Tín (26730073)

**Vai trò:** Phụ trách toàn bộ phần nhìn và nghe của game.
**File phụ trách:** `src/snake/ui.py`, `src/snake/config.py`, thư mục `assets/`
**Không được sửa:** `game.py`, `snake.py`, `food.py`

Phần của Tín quyết định game **trông có ra dáng hay không**. Hai bạn kia lo game
chạy đúng, Tín lo game nhìn đẹp và chơi thấy đã. Khi chấm điểm, đây thường là phần
gây ấn tượng đầu tiên.

### N1. Vẽ rắn — `draw_snake`

**Mục tiêu.** Vẽ thân rắn lên màn hình, phân biệt được đầu và thân.

**Đầu vào — đầu ra.** Nhận `surface` (màn hình) và `body` (danh sách toạ độ ô).
Không trả về gì.

**Gợi ý thực hiện.** Toạ độ trong `body` là **ô lưới**, phải nhân với
`config.CELL_SIZE` mới ra pixel để vẽ:

```python
rect = pygame.Rect(x * config.CELL_SIZE, y * config.CELL_SIZE,
                   config.CELL_SIZE, config.CELL_SIZE)
```

Đốt `body[0]` tô `COLOR_SNAKE_HEAD`, các đốt còn lại tô `COLOR_SNAKE_BODY`.

**Làm đẹp thêm (không bắt buộc nhưng nên có).** Truyền `border_radius` vào
`pygame.draw.rect()` để bo góc cho mềm mại. Chừa 1 pixel giữa các đốt để nhìn rõ
từng khớp. Vẽ 2 chấm trắng nhỏ lên đầu rắn làm mắt — chi tiết nhỏ này khiến game
sinh động hẳn lên.

**Nghiệm thu.**
- [ ] Rắn hiện đúng vị trí, khớp với lưới, không lệch nửa ô
- [ ] Nhìn vào phân biệt được đâu là đầu rắn
- [ ] Rắn dài 30 đốt vẫn vẽ mượt, không giật

**Ước lượng.** 1–2 giờ.

### N2. Vẽ mồi — `draw_food`

**Mục tiêu.** Vẽ miếng mồi nổi bật trên nền.

**Gợi ý thực hiện.** Cách đơn giản nhất là `pygame.draw.circle()` với tâm ở giữa ô.
Nhớ cộng thêm `CELL_SIZE // 2` để tâm hình tròn nằm đúng giữa ô chứ không phải ở
góc trên trái.

**Làm đẹp thêm.** Cho miếng mồi phình to nhỏ nhè nhẹ theo thời gian bằng hàm
`math.sin()` — hiệu ứng "thở" này rất dễ làm mà nhìn chuyên nghiệp hẳn. Hoặc thay
hình tròn bằng ảnh quả táo đặt trong `assets/images/`.

**Nghiệm thu.**
- [ ] Mồi nằm gọn trong ô, không tràn sang ô bên cạnh
- [ ] Màu mồi tương phản rõ với nền và với màu rắn

**Ước lượng.** 1 giờ.

### N3. Hiển thị điểm số — `draw_score`

**Mục tiêu.** Người chơi luôn thấy điểm hiện tại và kỷ lục.

**Đầu vào — đầu ra.** Nhận `surface`, `score`, `highscore`.

**Gợi ý thực hiện.** Đặt ở góc trên, dùng hàm `draw_text` đã có sẵn trong file.
Vấn đề cần giải: chữ đặt trên nền có thể bị rắn bò qua che mất. Hai cách xử lý —
hoặc vẽ một dải nền mờ phía sau chữ, hoặc chừa hẳn một thanh trạng thái ở trên và
thu nhỏ vùng chơi lại. Chọn cách nào cũng được, miễn chữ luôn đọc được.

**Nghiệm thu.**
- [ ] Điểm cập nhật ngay khi ăn mồi
- [ ] Chữ đọc rõ kể cả khi rắn bò ngang qua
- [ ] Phá kỷ lục thì có dấu hiệu nhận biết, ví dụ đổi màu chữ

**Ước lượng.** 1–2 giờ.

### N4. Màn hình menu — `draw_menu`

**Mục tiêu.** Màn hình đầu tiên người chơi nhìn thấy.

**Nội dung cần có.**
- Tên game cỡ lớn
- Ba mức độ khó: `1` Dễ, `2` Thường, `3` Khó — có đánh dấu mức đang chọn
- Dòng hướng dẫn "Nhấn SPACE để bắt đầu"
- Dòng hướng dẫn phím điều khiển
- Tên 3 thành viên nhóm ở dưới cùng (giảng viên sẽ nhìn vào đây)

**Gợi ý thực hiện.** Căn giữa theo chiều ngang bằng `config.WINDOW_WIDTH // 2`.
Chia chiều dọc thành các mốc cách đều nhau. Đừng viết cứng toạ độ pixel kiểu
`(300, 250)` — nếu sau này đổi kích thước cửa sổ trong `config.py` thì toàn bộ chữ
sẽ lệch hết.

**Nghiệm thu.**
- [ ] Có đủ 5 nội dung trên
- [ ] Bấm `1`/`2`/`3` thấy mức khó được chọn đổi rõ ràng
- [ ] Đổi `GRID_WIDTH` trong `config.py` rồi chạy lại, chữ vẫn căn giữa đúng

**Ước lượng.** 2–3 giờ.

### N5. Màn hình game over — `draw_game_over`

**Mục tiêu.** Báo thua và mời chơi lại.

**Nội dung cần có.** Chữ "GAME OVER", điểm vừa đạt, kỷ lục hiện tại, thông báo
riêng nếu vừa phá kỷ lục, dòng "SPACE — chơi lại" và "ESC — thoát".

**Gợi ý thực hiện.** Nên vẽ đè lên màn chơi thay vì xoá sạch màn hình — người chơi
nhìn thấy xác con rắn ở đúng chỗ vừa chết sẽ hiểu ngay mình thua vì sao. Cách làm:
tạo một `Surface` cùng kích thước, `set_alpha(180)` cho mờ, tô đen rồi `blit` lên
trước khi vẽ chữ.

**Nghiệm thu.**
- [ ] Vẫn thấy mờ mờ con rắn phía sau
- [ ] Điểm hiển thị đúng với điểm vừa chơi
- [ ] Phá kỷ lục có thông báo riêng

**Ước lượng.** 2 giờ.

### N6. Bảng màu, font chữ và cấu hình

**Mục tiêu.** Game có phong cách thị giác thống nhất.

**Việc cần làm.**
- Rà soát toàn bộ hằng số trong `config.py`, tinh chỉnh cho hợp lý
- Chọn bảng màu hài hoà. Bảng mặc định trong repo là tông tối xanh lá, có thể đổi.
  Gợi ý nguồn tham khảo: [coolors.co](https://coolors.co)
- Tải một font chữ đẹp về `assets/fonts/`. Font mặc định của pygame khá xấu.
  Gợi ý: Press Start 2P (kiểu game 8-bit) hoặc Poppins từ Google Fonts
- Bổ sung vào `config.py` các hằng số đường dẫn tới font và file âm thanh

**Lưu ý bản quyền.** Chỉ dùng font và ảnh có giấy phép miễn phí. Ghi rõ nguồn vào
README — đây là thói quen chuyên nghiệp và cũng tránh rắc rối khi nộp bài.

**Nghiệm thu.**
- [ ] Không còn số cứng nào nằm rải rác trong `ui.py`
- [ ] Font đã thay, chữ nhìn đẹp hơn mặc định
- [ ] Nguồn font và ảnh đã ghi vào README

**Ước lượng.** 2 giờ.

### N7. Âm thanh

**Mục tiêu.** Có tiếng khi ăn mồi và khi thua.

**Gợi ý thực hiện.** Dùng `pygame.mixer`. Tải file `.wav` hoặc `.ogg` miễn phí từ
[freesound.org](https://freesound.org) hoặc [opengameart.org](https://opengameart.org),
đặt trong `assets/sounds/`.

Bọc phần nạp âm thanh trong `try/except` — một số máy không có thiết bị âm thanh,
hoặc driver lỗi, và game không nên crash chỉ vì thiếu tiếng. Thêm một cờ bật/tắt
âm thanh trong `config.py` để lúc code khỏi bị làm phiền.

**Nghiệm thu.**
- [ ] Ăn mồi có tiếng, thua có tiếng
- [ ] Xoá file âm thanh đi, game vẫn chạy bình thường, chỉ mất tiếng
- [ ] Tiếng không bị rè, không trễ so với hành động

**Ước lượng.** 1–2 giờ.

---

## Việc chung của cả nhóm

| Việc | Ai chủ trì | Ai hỗ trợ | Ghi chú |
|------|-----------|-----------|---------|
| Báo cáo đồ án | Diễm | Trọng, Tín | Giới thiệu, thiết kế, sơ đồ lớp, kết quả, phân công |
| Sơ đồ lớp và sơ đồ trạng thái | Trọng | | Vẽ bằng draw.io, xuất PNG để trong `docs/` |
| Quay video demo 2–3 phút | Tín | | OBS Studio hoặc Xbox Game Bar |
| Ảnh chụp màn hình cho README | Tín | | Chụp menu, lúc chơi, màn hình game over |
| Slide thuyết trình | Diễm | Tín | Nếu môn học yêu cầu bảo vệ |
| Kiểm thử chéo | Cả nhóm | | Mỗi người chơi thử phần của hai bạn kia, ghi lỗi vào Issues |

**Về việc kiểm thử chéo.** Người viết code luôn bị "mù" với lỗi của chính mình vì
họ chỉ thử theo đúng cách họ nghĩ ra. Trước khi nộp, mỗi người dành 30 phút chơi
game và cố tình phá: bấm loạn phím, tạm dừng rồi bấm hướng, thua ngay ở giây đầu
tiên, chơi tới khi rắn dài kín màn hình. Lỗi tìm được thì tạo Issue chứ đừng tự
sửa file của người khác.

---

## Bảng tổng hợp khối lượng

| Thành viên | Số đầu việc | Giờ code ước tính | Việc quản lý / tài liệu | Tổng |
|-----------|-------------|-------------------|------------------------|------|
| Hồ Văn Trọng | 5 + quản lý | 10–13 giờ | 6 giờ | ~17 giờ |
| Lê Kiều Diễm | 6 | 7–10 giờ | 6 giờ (báo cáo) | ~15 giờ |
| Đặng Đức Tín | 7 | 10–14 giờ | 4 giờ (demo, ảnh) | ~16 giờ |

Khối lượng chia khá đều. Con số trên tính cho người mới học, gồm cả thời gian tra
cứu và sửa lỗi — bạn nào đã quen Python sẽ nhanh hơn đáng kể.

**Nếu có ai xong sớm** thì nhận thêm việc mở rộng thay vì ngồi không: thêm chướng
ngại vật trên bản đồ, thêm loại mồi đặc biệt cộng nhiều điểm, chế độ hai người
chơi, hoặc bảng xếp hạng lưu nhiều lượt chơi.

---

## Lộ trình 6 tuần

| Tuần | Trọng | Diễm | Tín | Mốc kiểm tra |
|------|-------|------|-----|--------------|
| 1 | Cài môi trường, mời thành viên | Cài môi trường | Cài môi trường | Cả 3 chạy được `python main.py` |
| 2 | T1 trạng thái, T2 phím | D1, D2, D3 | N6 màu và font | Rắn di chuyển được trên màn hình |
| 3 | T3 tốc độ, T4 va chạm | D4, D5 | N1, N2 vẽ rắn và mồi | Chơi được ván đầu tiên |
| 4 | T5 điểm cao nhất | D6 viết test | N3, N4, N5 giao diện | Game hoàn chỉnh từ menu tới game over |
| 5 | Sửa lỗi, duyệt PR | Viết báo cáo | N7 âm thanh, làm đẹp | Kiểm thử chéo, đóng hết Issue |
| 6 | Kiểm tra lần cuối, nộp bài | Hoàn thiện báo cáo | Quay video, chụp ảnh | Nộp đúng hạn |

Nhóm trưởng điền ngày cụ thể cho từng tuần sau khi biết deadline chính thức.

---

## Tài liệu tham khảo

- Tài liệu pygame: https://www.pygame.org/docs/
- Danh sách mã phím pygame: https://www.pygame.org/docs/ref/key.html
- Hướng dẫn pytest: https://docs.pytest.org/en/stable/getting-started.html
- Hướng dẫn Git của nhóm: [HUONG-DAN-GIT.md](HUONG-DAN-GIT.md)
- Quy tắc đóng góp: [../CONTRIBUTING.md](../CONTRIBUTING.md)

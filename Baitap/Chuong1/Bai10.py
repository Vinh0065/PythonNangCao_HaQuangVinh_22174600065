import math
class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Elip(Diem):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a
        self.b = b
    def tinh_dien_tich(self):
        return math.pi * self.a * self.b
class DuongTron(Elip):
    def __init__(self, x, y, r):
        super().__init__(x, y, r, r)
x = float(input("Nhập tọa độ x: "))
y = float(input("Nhập tọa độ y: "))
a = float(input("Nhập chiều dài trục chính a: "))
b = float(input("Nhập chiều dài trục phụ b: "))
elip = Elip(x, y, a, b)
dien_tich_elip = elip.tinh_dien_tich()
print("Diện tích của elip:", dien_tich_elip)
import math

class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def chu_vi(self):
        return self.a + self.b + self.c

    def dien_tich(self):
        p = self.chu_vi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

class TamGiacVuong(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, math.sqrt(a**2 + b**2))

class TamGiacCan(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, b)

class TamGiacDeu(TamGiacCan):
    def __init__(self, a):
        super().__init__(a, a)

# Sử dụng ví dụ:
tam_giac_thuong = TamGiac(5, 7, 8)
print("Tam giác thường:")
print("Chu vi:", tam_giac_thuong.chu_vi())
print("Diện tích:", tam_giac_thuong.dien_tich())

tam_giac_vuong = TamGiacVuong(3, 4)
print("\nTam giác vuông:")
print("Chu vi:", tam_giac_vuong.chu_vi())
print("Diện tích:", tam_giac_vuong.dien_tich())

tam_giac_can = TamGiacCan(5, 5)
print("\nTam giác cân:")
print("Chu vi:", tam_giac_can.chu_vi())
print("Diện tích:", tam_giac_can.dien_tich())

tam_giac_deu = TamGiacDeu(6)
print("\nTam giác đều:")
print("Chu vi:", tam_giac_deu.chu_vi())
print("Diện tích:", tam_giac_deu.dien_tich())

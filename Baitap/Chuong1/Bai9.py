#Bai9
import math

class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh
        self.do_dai_canh = []

    def nhap_do_dai_canh(self):
        print("Nhập độ dài các cạnh:")
        for i in range(self.so_canh):
            canh = float(input(f"Cạnh {i+1}: "))
            self.do_dai_canh.append(canh)

    def tinh_chu_vi(self):
        return sum(self.do_dai_canh)

    def tinh_dien_tich(self):
        pass

class HinhBinhHanh(DaGiac):
    def __init__(self):
        super().__init__(4)

    def tinh_dien_tich(self):
        a, b = self.do_dai_canh
        return a * b

class HinhChuNhat(HinhBinhHanh):
    def __init__(self):
        super().__init__()

class HinhVuong(HinhChuNhat):
    def __init__(self):
        super().__init__()

    def tinh_dien_tich(self):
        a, _ = self.do_dai_canh
        return a * a
def tinh_chu_vi_va_dien_tich(hinh):
    hinh.nhap_do_dai_canh()
    chu_vi = hinh.tinh_chu_vi()
    dien_tich = hinh.tinh_dien_tich()
    return chu_vi, dien_tich
print("1. Hình Bình Hành")
print("2. Hình Chữ Nhật")
print("3. Hình Vuông")
choice = int(input("Chọn hình: "))
if choice == 1:
    hinh_binh_hanh = HinhBinhHanh()
    chu_vi, dien_tich = tinh_chu_vi_va_dien_tich(hinh_binh_hanh)
elif choice == 2:
    hinh_chu_nhat = HinhChuNhat()
    chu_vi, dien_tich = tinh_chu_vi_va_dien_tich(hinh_chu_nhat)
elif choice == 3:
    hinh_vuong = HinhVuong()
    chu_vi, dien_tich = tinh_chu_vi_va_dien_tich(hinh_vuong)
else:
    print("Lựa chọn không hợp lệ.")
print("Chu vi:", chu_vi)
print("Diện tích:", dien_tich)
    
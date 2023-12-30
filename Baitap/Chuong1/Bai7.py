#Bai7
class Date:
    def __init__(self, ngay, thang, nam):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def display(self):
        print(f"{self.ngay}/{self.thang}/{self.nam}")

    def next(self):
        so_ngay_trong_thang = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.nam % 400 == 0 or (self.nam % 100 != 0 and self.nam % 4 == 0):
            so_ngay_trong_thang[2] = 29
        self.ngay += 1
        if self.ngay > so_ngay_trong_thang[self.thang]:
            self.ngay = 1
            self.thang += 1
            if self.thang > 12:
                self.thang = 1
                self.nam += 1
ngay=int(input("Nhập số ngày: "))
thang=int(input("Nhập số tháng: "))
nam=int(input("Nhập số năm: "))
ngay_thang_mac_dinh = Date(ngay,thang,nam)
ngay_thang_mac_dinh.display() 
ngay_thang_mac_dinh.next()
print("Ngày tiếp theo:")
ngay_thang_mac_dinh.display()

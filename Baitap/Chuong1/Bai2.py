#Bai2
class TS:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

    def in_thong_tin(self):
        print("Họ và tên:", self.ho_ten)
        print("Điểm Toán:", self.diem_toan)
        print("Điểm Lý:", self.diem_ly)
        print("Điểm Hóa:", self.diem_hoa)
        print("Tổng điểm:", self.tinh_tong_diem())

def nhap_danh_sach_thisinh():
    danh_sach_thisinh = []
    so_luong_thisinh = int(input("Nhập số lượng thí sinh: "))

    for i in range(so_luong_thisinh):
        print(f"\nNhập thông tin cho thí sinh thứ {i+1}:")
        ho_ten = input("Nhập họ và tên: ")
        diem_toan = float(input("Nhập điểm môn Toán: "))
        diem_ly = float(input("Nhập điểm môn Lý: "))
        diem_hoa = float(input("Nhập điểm môn Hóa: "))

        thisinh = TS(ho_ten, diem_toan, diem_ly, diem_hoa)
        danh_sach_thisinh.append(thisinh)

    return danh_sach_thisinh

def tim_thi_sinh_trung_tuyen(danh_sach_thisinh):
    thi_sinh_trung_tuyen = []

    for thisinh in danh_sach_thisinh:
        if thisinh.tinh_tong_diem() >= 20:
            thi_sinh_trung_tuyen.append(thisinh)

    return thi_sinh_trung_tuyen
def sap_xep_theo_diem(danh_sach_thisinh):
    return sorted(danh_sach_thisinh, key=lambda x: x.tinh_tong_diem(), reverse=True)
danh_sach_thisinh = nhap_danh_sach_thisinh()

print("\nDanh sách thí sinh trúng tuyển:")
thi_sinh_trung_tuyen = tim_thi_sinh_trung_tuyen(danh_sach_thisinh)
if len(thi_sinh_trung_tuyen) == 0:
    print("Không có thí sinh nào trúng tuyển.")
else:
    danh_sach_sap_xep = sap_xep_theo_diem(thi_sinh_trung_tuyen)
    for thisinh in danh_sach_sap_xep:
        thisinh.in_thong_tin() 
class Date:
    def __init__(self, ngay, thang, nam):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def display(self):
        print(f"{self.ngay:02d}/{self.thang:02d}/{self.nam}")

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


class Employee:
    def __init__(self, ho_ten, ngay_sinh, ngay_vao_cong_ty):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.ngay_vao_cong_ty = ngay_vao_cong_ty

    def display(self):
        print("Thông tin nhân viên:")
        print(f"Họ tên: {self.ho_ten}")
        print("Ngày sinh:", end=" ")
        self.ngay_sinh.display()
        print("Ngày vào công ty:", end=" ")
        self.ngay_vao_cong_ty.display()

    def tinh_so_nam_lam_viec(self):
        return self.ngay_vao_cong_ty.nam - self.ngay_sinh.nam

# Sử dụng ví dụ:
ngay_sinh_nv = Date(31, 3, 2004)
ngay_vao_cong_ty_nv = Date(15, 9, 2023)

nhan_vien = Employee("Nguyen Van A", ngay_sinh_nv, ngay_vao_cong_ty_nv)

nhan_vien.display()

so_nam_lam_viec = nhan_vien.tinh_so_nam_lam_viec()
print(f"Số năm làm việc: {so_nam_lam_viec} năm.")

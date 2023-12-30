class NganXep:
    def __init__(self, kich_thuoc):
        self.kich_thuoc = kich_thuoc
        self.du_lieu = []

    def day(self, phan_tu):
        if len(self.du_lieu) < self.kich_thuoc:
            self.du_lieu.append(phan_tu)
            print(f"Đưa {phan_tu} vào ngăn xếp.")
        else:
            print("Ngăn xếp đầy. Khum thể đưa thêm phần tử.")

    def lay(self):
        if self.du_lieu:
            phan_tu_lay = self.du_lieu.pop()
            print(f"Lấy {phan_tu_lay} từ ngăn xếp.")
            return phan_tu_lay
        else:
            print("Ngăn xếp trống. Khum thể lấy phần tử.")
            return None

    def rong(self):
        return not self.du_lieu

    def day_du(self):
        return len(self.du_lieu) == self.kich_thuoc

    def count(self):
        return len(self.du_lieu)

    def print_stack(self):
        print("Nội dung của ngăn xếp:", self.du_lieu) if self.du_lieu else print("Ngăn xếp trống.")

    def __del__(self):
        print("Ngăn xếp bị hủy.")

# Sử dụng ví dụ:
kich_thuoc_ngan_xep = 3
ngan_xep_cua_toi = NganXep(kich_thuoc_ngan_xep)

print("Ngăn xếp có trống khum?", ngan_xep_cua_toi.rong())

ngan_xep_cua_toi.day(1.0)
ngan_xep_cua_toi.day(2.0)
ngan_xep_cua_toi.day(3.0)

print("Số phần tử trên ngăn xếp:", ngan_xep_cua_toi.count())

ngan_xep_cua_toi.print_stack()

print("Ngăn xếp có đầy khum?", ngan_xep_cua_toi.day_du())

phan_tu_lay = ngan_xep_cua_toi.lay()
print("Phần tử lấy ra:", phan_tu_lay)

ngan_xep_cua_toi.print_stack()

print("Ngăn xếp có trống khum?", ngan_xep_cua_toi.rong())

# Hủy ngăn xếp khi ko cần nữa
del ngan_xep_cua_toi

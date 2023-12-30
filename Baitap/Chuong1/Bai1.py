#Bai1
class hinh_chu_nhat :
    def __init__(self):
        self.chieu_dai = 0
        self.chieu_rong = 0
    def nhap_do_dai(self):
        self.chieu_dai = float(input("nhap chieu dai hinh chu nhat"))
        self.chieu_rong = float(input("nhap chieu rong hinh chu nhat"))
    def tinh_chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) * 2
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
    def in_thong_tin(self):
        tinh_chu_vi = self.tinh_chu_vi()
        tinh_dien_tich = self.tinh_dien_tich()
        print("chieu_dai: {}".format(self.chieu_dai))
        print("chieu_rong: {}".format(self.chieu_rong))
        print("tinh_chu_vi: {}".format(tinh_chu_vi))
        print("tinh_dien_tich: {}".format(tinh_dien_tich))

hcn = hinh_chu_nhat()
hcn.nhap_do_dai()
hcn.in_thong_tin() 
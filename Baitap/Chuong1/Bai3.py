#Bai3
class PS :
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def kiem_tra_tinh_hop_le(self):
        return self.mau_so != 0

    def in_phan_so(self):
        print(f"phan so: {self.tu_so}/{self.mau_so}")
tu_so = int(input("nhap tu so: "))
mau_so = int(input("nhap mau so: "))
phan_so = PS(tu_so,mau_so)
if phan_so.kiem_tra_tinh_hop_le():
    phan_so.in_phan_so()
else:
    print("phan so khong hop le")

    

    
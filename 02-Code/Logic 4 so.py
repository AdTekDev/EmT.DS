import random

solan = 0
KetQua = random.randint(1000,9999)
DoanChuaDung = True 

Nkq = int(KetQua / 1000) % 10
Tkq = int(KetQua / 100) % 10
Ckq = int(KetQua / 10) % 10
Dkq = KetQua  % 10

while (solan < 12 and DoanChuaDung):
    solan += 1
    x = int(input("Nhap vao so can doan(1000..9999): "))
    sodung = 0
    str = ""
    Nx = int(x / 1000) % 10
    Tx = int(x / 100) % 10
    Cx = int(x / 10) % 10
    Dx = x  % 10
    if (Nkq == Nx):
        str += "="
        sodung += 1
    elif ( Nx == Tkq or Nx == Ckq or Nx == Dkq ):
        str += "*"
    else:
        str += "_"
    
    
    if (Tkq == Tx):
        str += "="
        sodung += 1
    elif ( Tx == Nkq or Tx == Ckq or Tx == Dkq ):
        str += "*"
    else:
        str += "_"
    
    if (Ckq == Cx):
        str += "="
        sodung += 1
    elif ( Cx == Tkq or Cx == Nkq or Cx == Dkq ):
        str += "*"
    else:
        str += "_"
    
    if (Dkq == Dx):
        str += "="
        sodung += 1
    elif ( Dx == Tkq or Dx == Ckq or Dx == Nkq ):
        str += "*"
    else:
        str += "_"
        
    if sodung == 4:
        DoanChuaDung = False
    print(str)

if (DoanChuaDung):
    print("Nguoi choi da thua !!!", KetQua)
else:
    print("Ban da choi thang !!!")

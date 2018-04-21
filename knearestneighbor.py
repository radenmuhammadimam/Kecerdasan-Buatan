import xlrd
import math

file   = xlrd.open_workbook("Dataset Tugas 3 AI 1718.xlsx")
sheet  = file.sheet_by_index(0)
sheet2 = file.sheet_by_index(1)

x1          = []
x2          = []
y1          = []
y2          = []
k1          = []
k2          = []
c1          = []
c2          = []
n1          = []
n2          = []
Tempat_Hoax = []

def Mencari_Jarak(x1 , x2 , y1 , y2 , k1 , k2 , c1 , c2) :
    a = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (k1 - k2) ** 2 + (c1 - c2) ** 2
    Akar = math.sqrt(a)
    return Akar

#Untuk Data_Train
for i in range(1,sheet.nrows):
     x1.append(sheet.cell_value          (i , 1))
     y1.append(sheet.cell_value          (i , 2))
     k1.append(sheet.cell_value          (i , 3))
     c1.append(sheet.cell_value          (i , 4))
     n1.append(sheet.cell_value          (i , 5))

#Untuk Data_Test
for i in range(1 , sheet2.nrows):
     x2.append(sheet2.cell_value         (i , 1))
     y2.append(sheet2.cell_value         (i , 2))
     k2.append(sheet2.cell_value         (i , 3))
     c2.append(sheet2.cell_value         (i , 4))
     n2.append(sheet2.cell_value         (i , 5))
     Tempat_Hoax.append(sheet2.cell_value(i , 5))

Tempat_Keseluruhan = []
for i in range(len(x2)):
    z          = []
    a          = []
    e          = []
    g          = []
    Hoax       = 0
    Tidak_Hoax = 0

    for j in range(len(x1)):
        a = Mencari_Jarak(x1[j] , x2[i] , y1[j] , y2[i] , k1[j] , k2[i] , c1[j] , c2[i])
        z.append(a)
    best = sorted(z)[0:3]

    for k in best:
        if n1[z.index(k)] == 1.0:
            Hoax          = Hoax + 1
        else:
            Tidak_Hoax    = Tidak_Hoax + 1
    if Hoax > Tidak_Hoax:
        n2 = 1.0
    else:
        n2 = 0.0
    Tempat_Keseluruhan.append(n2)
    print(n2)
count = 0

for i in range(len(x2)):
     if(Tempat_Keseluruhan[i] == Tempat_Hoax[i]):
         count                = count + 1

akurasi  = (count / len(x2)) * 100
print("Akurasi : " , akurasi , "%")

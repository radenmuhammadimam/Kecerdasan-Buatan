def naik(a , b , x):
    return (x - a) / (b - a)

def turun(a , b , x):
    return (b - x) / (b - a)

#Emosi

def miu_emosi(x):
    if(x >= 90):
        miu_emosi = [[1 , 'SangatTinggi'] , [0 , 'Tinggi']]
    elif(x > 80 and x < 90):
        miu_emosi = [[naik(80 , 90 , x) , 'SangatTinggi'] , [turun(80 , 90 , x) , 'Tinggi']]
    elif(x >= 70 and x <= 80):
        miu_emosi = [[1 , 'Tinggi'] , [0 , 'SangatTinggi']]
    elif(x > 60 and x < 70):
        miu_emosi = [[naik(60 , 70 , x) , 'Tinggi'] , [turun(60 , 70 , x) , 'Sedang']]
    elif(x >= 50 and x <= 60):
        miu_emosi = [[1 , 'Sedang'] , [0 , 'Tinggi']]
    elif(x > 40 and x < 50):
        miu_emosi = [[naik(40 , 50 , x) , 'Sedang'] , [turun(40 , 50 , x) , 'Kecil']]
    elif(x >= 30 and x <= 40):
        miu_emosi = [[1 , 'Kecil'] , [0 , 'Sedang']]
    elif(x > 20 and x < 30):
        miu_emosi = [[naik(20 , 30 , x) , 'Kecil'] , [turun(20 , 30 , x) , 'SangatKecil']]
    elif(x <= 20):
        miu_emosi = [[1 , 'SangatKecil'] , [0 , 'Kecil']]
    return miu_emosi

#PengecekanSugeno

def pengecekan_sugeno (a , b):
    if(a[0][0] == 1 and b[0][0] == 1):
        a = a[0]
        b = b[0]
        temp = berita_hoax(a , b)
        return [sugeno0(temp),]

    elif(a[0][0]== 1 and b[0][0] !=1):
        bcek = b[0]
        cek1 = berita_hoax(a , bcek)
        bcek1 = b[1]
        cek2 = berita_hoax(a , bcek1)
        return (sugeno1(cek1 , cek2))

    elif (a[0][0] != 1 and b[0][0] == 1):
        b = b[0]
        acek = a[0]
        cek1 = berita_hoax(acek , b)
        acek1 = a[1]
        cek2 = berita_hoax(acek1 , b)
        return (sugeno1(cek1 , cek2))

    elif(a[0][0] != 1 and b[0][0] != 1):
        a1 = a[0]
        a2 = a[1]
        b1 = b[0]
        b2 = b[1]
        h1 = berita_hoax(a1 , b1)
        h2 = berita_hoax(a1 , b2)
        h3 = berita_hoax(a2 , b1)
        h4 = berita_hoax(a2 , b2)
        return sugeno3(h1 , h2 , h3 , h4)

def sugeno0(a):#ketika hanya bilangan inputnya satu
    if(a[1] == 'Hoax'):
        a = a[0]
        return [a * 40 / a , 'Hoax']
    elif(a[1] == 'Tidak Hoax'):
        a = a[0]
        return [a * 20 / a , 'Tidak Hoax']

def sugeno1(a , b):
    if(a[1] == 'Hoax' and b[1] == 'Hoax'):
        if(a[0] > b[0]):
            return [a[0] * 100 / a[0] , 'Hoax']
        else:
            return [b[0] * 0 / b[0] , 'Hoax']

    elif(a[1] == 'Tidak Hoax' and b[1] == 'Tidak Hoax'):
        if(a[0] > b[0]):
            return [a[0] * 0 / a[0] , 'Tidak Hoax']
        else:
            return [b[0] * 0 / a[0] , 'Tidak Hoax']

    elif(a[1] == 'Hoax' and b[1] == 'Tidak Hoax'):
        hasil = ((a[0] * 100) + (b[0] * 0)) / a[0] + b[0]
        if(hasil < 70):
            return[hasil , 'Tidak Hoax']
        else:
            return [hasil , 'Hoax']

    elif(a[1] == 'Tidak Hoax' and b[1] == 'Hoax'):
        hasil = ((a[0] * 0) + (b[0] * 100)) / a[0] + b[0]
        if (hasil < 70):
            return [hasil, 'Tidak Hoax']
        else:
            return [hasil, 'Hoax']

def sugeno3(a , b , c , d):
    if(a[1] == 'Tidak Hoax' and b[1] == c[1] == d[1] == 'Tidak Hoax'):
        if(a[0]>=b[0] and a[0]>= c[0] and a[0]>=d[0]):
            return [a[0] * 0 / a[0],'Tidak Hoax']
        elif (b[0] >= a[0] and b[0] >= c[0] and b[0] >= d[0]):
            return [b[0] * 0 / b[0] , 'Tidak Hoax']
        elif (c[0] >= b[0] and c[0] >= a[0] and c[0] >= d[0]):
            return [c[0] * 0 / c[0] , 'Tidak Hoax']
        elif (d[0] >= b[0] and d[0] >= a[0] and d[0] >= c[0]):
            return [d[0] * 0 / d[0] , 'Tidak Hoax']

    elif (a[1] == b[1] == c[1] == d[1] == 'Tidak Hoax'):
        if (a[0] >= b[0] and a[0] >= c[0] and a[0] >= d[0]):
            return [a[0] * 0 / a[0] , 'Tidak Hoax']
        elif (b[0] >= a[0] and b[0] >= c[0] and b[0] >= d[0]):
            return [b[0] * 0 / b[0] , 'Tidak Hoax']
        elif (c[0] >= b[0] and c[0] >= a[0] and c[0] >= d[0]):
            return [c[0] * 0 / c[0] , 'Tidak Hoax']
        elif (d[0] >= b[0] and d[0] >= a[0] and d[0] >= c[0]):
            return [d[0] * 0 / d[0] , 'Tidak Hoax']

#Provokasi

def miu_provokasi(y):
    if(y >= 90):
        miu_provokasi = [[1 , 'SangatTinggi'] , [0 , 'Tinggi']]
    elif(y > 80 and y < 90):
        miu_provokasi = [[naik(80 , 90 , y) , 'SangatTinggi'] , [turun(80 , 90 , y) , 'Tinggi']]
    elif(y >= 70 and y <= 80):
        miu_provokasi = [[1 , 'Tinggi'] , [0 , 'SangatTinggi']]
    elif(y > 60 and y < 70):
        miu_provokasi = [[naik(60 , 70 , y) , 'Tinggi'] , [turun(60 , 70 , y) , 'Sedang']]
    elif(y >= 50 and y <= 60):
        miu_provokasi = [[1 , 'Sedang'] , [0 , 'Tinggi']]
    elif(y > 40 and y < 50):
        miu_provokasi = [[naik(40 , 50 , y) , 'Sedang'] , [turun(40 , 50 , y) , 'Kecil']]
    elif(y >= 30 and y <= 40):
        miu_provokasi = [[1 , 'Kecil'] , [0 , 'Sedang']]
    elif(y > 20 and y < 30):
        miu_provokasi = [[naik(20 , 30 , y) , 'Kecil'] , [turun(20 , 30 , y) , 'SangatKecil']]
    elif(y <= 20):
        miu_provokasi = [[1 , 'SangatKecil'] , [0 , 'Kecil']]
    return miu_provokasi

def berita_hoax(miu_emosi , miu_provokasi):
    hoax=[]
    if(miu_emosi[1] == 'SangatKecil' and miu_provokasi[1] == 'SangatKecil'):
        hoax = [1 ,'Tidak Hoax']

    elif(miu_emosi[1] == 'SangatKecil' and miu_provokasi[1] == 'Kecil'):
        if(miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Tidak Hoax']
        else:
            hoax = [miu_emosi[0] , 'Tidak Hoax']

    elif(miu_emosi[1] == 'SangatKecil' and miu_provokasi[1] == 'Sedang'):
        if(miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Tidak Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Tidak Hoax']

    elif(miu_emosi[1] == 'SangatKecil' and miu_provokasi[1] == 'Tinggi'):
        if(miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Tidak Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Tidak Hoax']

    elif(miu_emosi[1] == 'SangatKecil' and miu_provokasi[1] == 'SangatTinggi'):
        if(miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Hoax']

    elif(miu_emosi[1] == 'Kecil' and miu_provokasi[1] == 'SangatKecil'):
        if(miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Tidak Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Tidak Hoax']

    elif(miu_emosi[1] == 'Kecil' and miu_provokasi[1] == 'Kecil'):
        hoax = [1 , 'Tidak Hoax']

    elif(miu_emosi[1] == 'Kecil' and miu_provokasi[1] == 'Sedang'):
        if(miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Tidak Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Tidak Hoax']

    elif(miu_emosi[1] == 'Kecil' and miu_provokasi[1] == 'Tinggi'):
        if(miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Tidak Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Tidak Hoax']

    elif(miu_emosi[1] == 'Kecil' and miu_provokasi[1] == 'SangatTinggi'):
        if(miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Hoax']

    elif(miu_emosi[1] == 'Sedang' and miu_provokasi[1] == 'SangatKecil'):
        if(miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Tidak Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Tidak Hoax']

    elif (miu_emosi[1] == 'Sedang' and miu_provokasi[1] == 'Kecil'):
        if (miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Tidak Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Tidak Hoax']

    elif(miu_emosi[1] == 'Sedang' and miu_provokasi[1] == 'Sedang'):
        if(miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Tidak Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Tidak Hoax']

    elif(miu_emosi[1] == 'Sedang' and miu_provokasi[1] == 'Tinggi'):
        if(miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Hoax']

    elif(miu_emosi[1] == 'Sedang' and miu_provokasi[1] == 'SangatTinggi'):
        if(miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Hoax']

    elif(miu_emosi[1] == 'Tinggi' and miu_provokasi[1] == 'SangatKecil'):
        if(miu_emosi[1][0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Tidak Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Tidak Hoax']

    elif(miu_emosi[1] == 'Tinggi' and miu_provokasi[1] == 'Kecil'):
        if(miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Tidak Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Tidak Hoax']

    elif(miu_emosi[1] == 'Tinggi' and miu_provokasi[1] == 'Sedang'):
        if(miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Tidak Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Tidak Hoax']

    elif(miu_emosi[1] == 'Tinggi' and miu_provokasi[1] == 'Tinggi'):
        if(miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Hoax']

    elif (miu_emosi[1] == 'Tinggi' and miu_provokasi[1] == 'SangatTinggi'):
        if (miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Hoax']

    elif (miu_emosi[1] == 'SangatTinggi' and miu_provokasi[1] == 'SangatKecil'):
        if (miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Tidak Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Tidak Hoax']

    elif (miu_emosi[1] == 'SangatTinggi' and miu_provokasi[1] == 'Kecil'):
        if (miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Tidak Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Tidak Hoax']

    elif (miu_emosi[1] == 'SangatTinggi' and miu_provokasi[1] == 'Sedang'):
        if (miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Hoax']

    elif (miu_emosi[1] == 'SangatTinggi' and miu_provokasi[1] == 'Tinggi'):
        if (miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0] , 'Hoax']
        else:
            hoax = [miu_provokasi[0] , 'Hoax']

    elif (miu_emosi[1] == 'SangatTinggi' and miu_provokasi[1] == 'SangatTinggi'):
        if (miu_emosi[0] < miu_provokasi[0]):
            hoax = [miu_emosi[0], 'Hoax']
        else:
            hoax = [miu_provokasi[0], 'Hoax']
    return hoax

n = int(input("Masukkan Banyaknya Bilangan : "))

for i in range(n):
    emosi = float(input("Masukkan Nilai Emosi : "))
    provokasi = float(input("Masukkan Nilai Provokasi : "))
    hasilemosi = miu_emosi(emosi)
    hasilprovokasi = miu_provokasi(provokasi)
    print(hasilemosi)
    print(hasilprovokasi)
    hasil_pengecekan = pengecekan_sugeno(hasilemosi , hasilprovokasi)
    print(hasil_pengecekan)

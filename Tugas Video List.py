#71200632 Abraham David Hartanto
#List
#Menampilkan urutan luas terbesar dari  inputan user (dapat berupa segitiga,lingkaran,persegi panjang dan persegi)
#Urutan ditampilkan dalam bentuk list dari terbesar ke yang terkecil 
#Jumlah maksimal input tidak ditentukan

bangun = ""
tanya = ""
daftar = []
luas = 0
while True : 
    masuk = str(input("Masukkan bentuk bangun datar :"))
    if masuk == "segitiga" : 
        alas = int(input("Masukkan alas :"))
        tinggi = int(input("Masukkan tinggi :"))
        luas = alas *  tinggi * 1/2
        daftar.append(luas)
    elif masuk == "lingkaran" : 
        jari = int(input("Masukkan jari-jari :"))
        luas = 22/7 * (jari)**2
        daftar.append(luas)
    elif masuk == "persegi" :
        sisi = int(input("Masukkan sisi : "))
        luas = sisi * sisi 
        daftar.append(luas)
    elif masuk == "persegi panjang" :
        panjang = int(input("Masukkan panjang : "))
        lebar = int(input("Masukkan lebar : "))
        luas = panjang * lebar
        daftar.append(luas)
    else : 
        print("Bangun datar yang dimasukkan tidak terdaftar !")
        break
    daftar.sort()
    daftar.reverse()
    tanya = str(input("Apakah ada lagi bangun datar yang ingin dimasukkan ?(ya/tidak)  "))
    if tanya == "ya" :
        continue
    elif tanya == "tidak" :
        print("Terdapat " + str(len(daftar)) + " macam bangun datar dengan urutan luas " + str(daftar))
        break
    else : 
        print("Error !")
        break

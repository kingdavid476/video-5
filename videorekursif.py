#Abraham David Hartanto
#71200632
#Fungsi Rekursif 

'''
Budi adalah seorang manajer pada salah satu perusahaan besar. Di perusahaan cabang tempatnya bekerja,para karyawan mengeluh karena kursi yang disediakan terlalu sedikit
Budi ingin memperbaiki hal tersebut,kemudian ia mengunjungi salah satu toko mebel milik temannya
Setiap kursi dijual seharga Rp 50.000 
Pembelian pertama mendapat diskon 1% dan bertambah 1% setiap penambahan pembelian kursi lainnya
Keesokan harinya ia mendapat data perbandingan jumlah karyawan dan kursi yang telah ada
Hitunglah jumlah total pembayarannya agar jumlah kursi sesuai dengan jumlah karyawan yang ada
Perhitungan dilakukan dengan menggunakan fungsi rekursif dengan jumlah maksimal 3 parameter
'''
def hitungkursi(kursi,karyawan,harga) : 
    if karyawan > kursi : 
        kekurangan = karyawan - kursi
        bayar = int(harga * 99 / 100)
        return bayar + hitungkursi(kursi+1,karyawan,bayar)
    else : 
        return 0

print(hitungkursi(10,50,50000))
print(hitungkursi(100,50,50000))
print(hitungkursi(10,110,50000))
print(hitungkursi(10,500,50000))

def hitungkursi(kursi,karyawan,diskon) : 
    harga = 50000
    if diskon >= 100 : 
        return 0
    elif karyawan > kursi : 
        kekurangan = karyawan - kursi
        bayar = int(harga * (100-diskon) / 100)
        return bayar + hitungkursi(kursi+1,karyawan,diskon+1)
    else : 
        return 0

print(hitungkursi(10,50,1))
print(hitungkursi(100,50,1))
print(hitungkursi(10,110,1))
print(hitungkursi(10,500,1))
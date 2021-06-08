#Abraham David Hartanto
#71200632
#Regular Expression
'''
Buatlah sebuah program untuk mendeteksi angka barcode dari input dengan ketentuan 
1. Angka dan huruf barcode haruslah terdiri dari 7 angka dan 6 huruf berurutan seperti nomer 2 
2. Susunan angka barcode haruslah seperti susunan berikut (1-111111-Aaaaaa) 
3. Susunan huruf di barcode haruslah memiliki minimal 1 pasang huruf yang sama berurutan
4. Output | Produk : [produk], Barcode : barcode
'''

import re 
kosong = []
kosong2 = []
index = []
masuk = "halo nama saya David dengan nomor handphone 0812345678901 berikut adalah barcode beberapa produk saya. Susu 1-234567-aaBCde , Lemon 1-21134-123444 , Jeruk 1-811123-adEfdhi"
while True : 
    cek1 = re.findall(r'\d-+[\d]{6}-+[a-zA-Z]{6}',masuk)
    jumlah = len(cek1)
    if jumlah == 0 : 
        print("Tidak ada barcode")
        break
    else : 
        nama = re.findall(r'[a-zA-Z]* [0-9]{1}-',masuk)
        for i in range(0,len(nama)) :
            simpan2 = nama[i]
            cekpr = re.findall(r'[a-zA-Z]* ',simpan2)
            kosong.append(cekpr)
        for i in range(0,jumlah) : 
            simpan = cek1[i]
            cek2 = re.findall(r'([a-zA-Z])\1',simpan)
            jumlah2 = len(cek2)
            if jumlah2 > 0 : 
                index.append(i)
                kosong2.append(cek2)
        if len(kosong2) == 0 : 
            print("Tidak ada yang memenuhi syarat")
            break
        else : 
            panjanghasil = len(index)
            for j in range(0,panjanghasil) :
                hasil = index[j]
                print("Produk :",kosong[hasil],",Barcode :",cek1[hasil])
            break
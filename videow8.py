#Abraham David Hartanto 71200632
#Files
''' Membuat program untuk menampilkan jumlah keuntungan per minggu dari hasil penjualan saham ke dalam file txt'''
cetak = ""
total_sisa = ""
total_untung = 0
data = ""
while True :
    file_ = open("untung.txt","w")
    print("===== Selamat datang di program penghitung keuntungan saham =====")
    minggu = int(input("Minggu keberapa ? :"))
    jumlah_tipe_saham = int(input("Masukkan jumlah tipe saham yang diperjualbelikan :"))
    for i in range(1,jumlah_tipe_saham+1) :
        nama = str(input("Masukkan nama saham :"))
        jumlah_beli = int(input("Masukkan jumlah saham "+nama+" yang dibeli :"))
        harga_beli = int(input("Masukkan harga beli saham "+nama+"  :"))
        jumlah_jual = int(input("Masukkan jumlah saham "+nama+" yang dijual :"))
        harga_jual = int(input("Masukkan harga jual saham "+nama+"  :"))
        keuntungan = (jumlah_jual * harga_jual) - (jumlah_jual * harga_beli)
        hitung_sisa = str(jumlah_beli - jumlah_jual)
        sisa = hitung_sisa + " " + nama + "," + " "
        total_sisa = total_sisa + sisa 
        total_untung = total_untung + keuntungan
    info = str("Keuntungan minggu ke " + str(minggu) +" adalah Rp. " + str(total_untung)+ " dengan sisa " + total_sisa)
    data = data + info + "\n"
    file_.write(data)
    file_.close()
    tanya = str(input("Apakah masih mau menghitung keuntungan minggu lainnya ? (Ya/Tidak)"))
    tanya_besar = tanya.upper()
    if tanya_besar == "YA" : 
        continue
    elif tanya_besar == "TIDAK" :
        break
    else : 
        print("Error")
        break
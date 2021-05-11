#Abraham David Hartanto / 71200632
#Set
'''
Membuat program untuk petugas bandara yang akan digunakan untuk mendata jumlah pendatang yang bebas maupun terjangkit virus corona
Pendatang dibedakan menjadi imigran dan turis 
Pendatang dapat merupakan keduanya (dalam artian imigran sementara (misal satu tahun))
Mungkin terdapat pendatang ilegal
'''

print("======= Selamat Datang di Program Pendataan Pendatang =======")
data = set()
data_turis = set()
data_imigran = set()
data_terjangkit = set()
#input
jumlah = int(input("Masukkan jumlah pendatang : "))
for i in range(0,jumlah) : 
    nama = str(input("Masukkan nama pendatang : "))
    data.add(nama)
jumlah_turis = int(input("Masukkan jumlah turis :"))
for i in range(0,jumlah_turis) : 
    nama_turis = str(input("Masukkan nama turis : "))
    data_turis.add(nama_turis)
jumlah_imigran = int(input("Masukkan jumlah imigran :"))
for i in range(0,jumlah_imigran) : 
    nama_imigran = str(input("Masukkan nama imigran : "))
    data_imigran.add(nama_imigran)
jumlah_terjangkit = int(input("Masukkan jumlah pendatang yang terjangkit virus :"))
for i in range(0,jumlah_terjangkit) : 
    nama_terjangkit = str(input("Masukkan nama pendatang yang terjangkit : "))
    data_terjangkit.add(nama_terjangkit)
hitung = len(data_turis) + len(data_imigran)
#Proses + Output
while True : 
    print("Pilihan :")
    print("1. Jumlah pendatang,turis dan imigran " + "\n" + "2. Pendatang yang termasuk imigran dan turis" + "\n" + "3. Imigran dan turis yang bebas dari virus" + "\n" + "4. Pendatang Ilegal" + "\n" + "5. Keluar")
    pilih = int(input("Masukkan nomor pilihan :"))
    if pilih == 1 : 
        print(" Jumlah pendatang = " + str(len(data)) + "\n Jumlah turis = " + str(len(data_turis)) + "\n Jumlah Imigran = " + str(len(data_imigran)))
        if len(data) != hitung : 
            print("Kemungkinan terdapat pendatang ilegal")
    elif pilih == 2 : 
        print("Pendatang yang termasuk imigran dan turis adalah : ",data_imigran.intersection(data_turis))
    elif pilih == 3 : 
        print("Imigran yang bebas dari virus adalah : ",data_imigran - data_terjangkit)
        print("Turis yang bebas dari virus adalah : ",data_turis - data_terjangkit)
    elif pilih == 4 : 
        gabungan = data_turis.union(data_imigran)
        ilegal = data - gabungan 
        if len(ilegal) == 0 : 
            print("Tidak ada pendatang ilegal")
        else : 
            print(ilegal)
    elif pilih == 5 :
        print("Terimakasih telah menggunakan program ini") 
        break
    else : 
        print("Pilihan tidak ada ! ")
        break
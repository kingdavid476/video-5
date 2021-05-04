#Abraham David H 71200632
#Tuple
'''
Membuat sebuah program untuk mendata nama,gaji,dan nomor induk pekerja
Data dimasukkan di source code,wajib menggunakan fungsi def,dan source code didalam fungsi def maksimal 5 baris
'''

def program(data) :
    template = "        Nama                    Gaji              NIP" + "\n"
    simpan = "" 
    nama = str(data[0])
    gaji = "     Rp." + str(data[1])
    nip = "         " + str(data[2])
    simpan = simpan + template + nama + gaji + nip
    return simpan

data = ("Abraham David Hartanto", 10000000, 71200632)
print(program(data))

def pogram(data) : 
    template = "        Nama                    Gaji              NIP" + "\n"
    simpan = "" 
    nama,gaji,nip = data 
    simpan = simpan + template + str(nama) + "     Rp." + str(gaji) + "         "+ str(nip)
    return simpan
data = ("Abraham David Hartanto", 10000000, 71200632)
print(pogram(data))
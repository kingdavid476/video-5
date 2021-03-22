#Abraham David Hartanto 71200632
#Pengolahan string
#Buatlah sebuah program untuk mengubah 3 input berupa satu kata di setiap inputnya dengan ketentuan
'''
Syarat : 
Apabila input pertama > 5 huruf maka tampilkan semua input secara berurutan
Apabila input kedua diawali dengan huruf a maka tampilkan jumlah total dari ketiga input tersebut
Apabila input ketiga memiliki suku kata "ku" maka tampilkan "error"
Apabila ada 2 atau lebih ketentuan terpenuhi maka  minta sebuah input lagi dari user dan tampilkan input 
tersebut dengan huruf kapital secara terbalik kecuali huruf pertama
'''
x = 0 
satu = str(input("Masukkan kata pertama :"))
dua = str(input("Masukkan kata kedua :"))
tiga = str(input("Masukkan kata ketiga :"))
y = "ku" in tiga
spertama = len(satu)
if spertama > 5 :
    print(satu,dua,tiga)
    x = x + 1
if dua[0]  == "a" :
    print(len(satu) + len(dua) + len(tiga))
    x = x + 1
if y == True :
    print("error")
    x = x + 1 
if x > 0 :
    empat = str(input("Masukkan kata keempat :"))
    empat_1 = len(empat) - 1 
    empat_kapital = empat[(empat_1):0:-1].upper()
    print(empat_kapital)

#pembelian saham dengan budget sebesar masukan user
#Setiap membeli saham satuannya adalah lot. 1 lot  = 100 lembar
#Buatlah program yang dapat membantu user untuk penghitungan dalam membeli saham"
#Jumlah varian saham yang dapat dibeli maksimal adalah 5
varian = 0
modal = int(input("Masukkan jumlah modal :")) #input 1
while modal > 0 :
    while varian <= 5 : 
        varian = varian + 1
        saham = str(input("Masukkan nama saham yang akan dibeli :"))#input 2
        harga = int(input("Masukkan harga per lembar saham tersebut :"))#input 3
        jumlah = int(input("Masukkan jumlah lot saham yang akan dibeli :"))#input 4
        cost = harga*jumlah*100
        modal = modal - cost
        if modal > 0 :
            print("Anda membeli",saham,"sebanyak",jumlah,"lot")#output
            print("Sisa modal anda adalah sebanyak :",modal) #output
            tanya = str(input("Apakah masih ingin membeli saham lainnya ?"))
            if tanya == "ya" :
                continue
            elif tanya == "tidak" :
                print("Terima kasih telah menggunakan program ini")
                break
        elif modal < 0 :
            print("Modal anda tidak cukup untuk membeli saham sejumlah yang anda masukkan") #output 
            break
        elif modal == 0 :   
            print("Modal anda telah habis,terima kasih telah menggunakan program ini") #output
            break
    break
if modal <= 0 :
    print("Tambahkan lagi modal anda !") #output
elif varian > 5 :
    print("Varian saham anda telah mencapai batas maksimum") #output
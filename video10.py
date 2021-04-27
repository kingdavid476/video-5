#Abraham David Hartanto 71200632
#Dictionaries 
"""
Buatlah sebuah program yang dapat menampilkan senyawa yang mengandung ikatan unsur tertentu (misal hidrogen) dari senyawa yang ada
"""
Senyawa = {"Air" : "H2O" , "Etanol" : "C2H5OH" , "Glukosa" : "C6H12O6" , "Kalium Sulfat" : "K2SO4" , "Kalsium Karbonat" : "CaCO3" , "Karbon Dioksida" : "CO2"}
masuk = str(input("Masukkan unsur dalam senyawa  : "))
lokasi = []
senyawa_key = list(Senyawa.keys())
senyawa_value = list(Senyawa.values())
jumlah = len(senyawa_key) 
for i in range(0,jumlah-1) :
    simpan = senyawa_value[i]
    unsur = list(simpan)
    if masuk == "hidrogen" : 
        for x in unsur : 
            if x == "H" : 
                lokasi.append(i)
    elif masuk == "oksigen" : 
        for x in unsur : 
            if x == "O" : 
                lokasi.append(i)
    elif masuk == "karbon" :
        for x in unsur : 
            if x == "C" : 
                lokasi.append(i)
    elif masuk == "kalium" : 
        for x in unsur : 
            if x == "K" : 
                lokasi.append(i)
    elif masuk == "kalsium" : 
        panjang = len(unsur)
        for y in range(0,panjang-2) : 
            pertama = unsur[y]
            kedua = unsur[y+1]
            gabungan = pertama + kedua 
            if  gabungan == "Ca" : 
                lokasi.append(i)
lokasi = list(set(lokasi))
print("Senyawa yang mengandung unsur",masuk,"adalah : ")
for z in lokasi : 
    print(senyawa_key[z])
            
        


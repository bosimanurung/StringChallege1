#It Works! Membaca file txt (bila dibuka lewat program excel yg nan muncul di baris 9 dan 14, tapi dibuka dgn notepad/txt ternyata ada datanya)
#tapi kalau dibaca lewat file txt, setiap baris diakhiri \n jadi harus dicek agar \n tdk masuk hitungan karakter
#lalu hasilnya disimpan ke file txt baru (sesuaikanlah foldernya)

filetext = open("c:/xampp/htdocs/python/tes-acak100.txt", "r") #backup terlebih dulu filenya dgn nama file lain
filetext2 = open("c:/xampp/htdocs/python/tes-acak100f.txt", "w") #hasilnya akan disimpan ke file txt ini

#coba menyaring data tiap baris dgn mengambil char 7sd12 saja lalu save ke file lain (utk perbandingan)
for line in filetext:
    #print('here')
    eight2twelve = thirdteen = ""
    lessthan8 = eight = ""
    lessthan8 = line[:7]
    eight = line[7:8] #ambil char ke-8 utk memastikan apakah itu \n
    eight2twelve = line[7:12]
    thirdteen = line[12:13] #ambil char ke-13 utk memastikan apakah itu \n karena tampilan di txt file ada 12char tapi karena ada \n di tiap baris, jadi terhitung 13
    if (thirdteen != '' and thirdteen != '\n') or (lessthan8 != '' and eight=='\n'):
        continue
    elif eight2twelve != '' or thirdteen=='\n': #tiap baris file txt nya mengandung \n, bila hanya isi itu, jgn simpan
        filetext2.write(line) #bila ada mengandung \n (biasanya di akhir text), simpan datanya
        continue
            
filetext2.close()


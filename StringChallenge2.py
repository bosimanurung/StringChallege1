#It Works! Membaca file txt (yg nan bila dibuka lewat program excel, tapi dibuka dgn notepad ternyata ada datanya)
#lalu hasilnya disimpan ke file txt baru (sesuaikanlah foldernya)

filetext = open("c:/xampp/htdocs/python/tes-acak100.txt", "r") #backup terlebih dulu filenya dgn nama file lain
filetext2 = open("c:/xampp/htdocs/python/tes-acak100d.txt", "w") #hasilnya akan disimpan ke file txt ini

#coba menyaring data tiap baris dgn mengambil char 7sd12 saja lalu save ke file lain (utk perbandingan)
for line in filetext:
    print('here')
    each_line = line
    print(each_line)
    each_line = each_line[7:12]
    if each_line != '' and each_line != '\n': #tiap baris file txt nya mengandung \n, bila hanya isi itu, jgn simpan
        ada = False
        for i in each_line:
            if i == '\n':
                ada = True       
                filetext2.write(each_line) #bila ada mengandung \n (biasanya di akhir text), simpan datanya
                continue
        if ada == False:
            each_line += '\n' #bila tdk ada \n di datanya, tambahkan \n (biasanya di akhir text tsb)
            filetext2.write(each_line) #simpan ke file txt baru tsb
            
filetext2.close()


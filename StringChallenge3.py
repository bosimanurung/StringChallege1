#it works! Membaca file txt (yg nan di excel, tapi disini ternyata bukan, tapi text)
#lalu hasilnya disimpan ke file excel baru. File aslinya dlm bentuk txt sebesar 15GB, file sample hanya 100 baris
#menyaring data tiap baris dgn mengambil char 7sd12 saja lalu save ke file lain (xls), lbh cepat save ke txt

import pandas as pd 

filetext = open("c:/xampp/htdocs/python/tes-acak100.txt", "r")

df = pd.DataFrame([[""]], columns=['Result'])
list_data = []
for line in filetext:
    each_line = line
    each_line = each_line[7:12]
    if each_line != '' and each_line != '\n': #tiap baris file txt nya mengandung \n
        list_data.append(each_line) #menyimpan hasilnya ke list
filetext.close()

#simpan ke file baru
df=pd.DataFrame(list_data, columns=['Result']) #menyimpan list ke dataFrame
df.to_excel('c:/xampp/htdocs/python/tes-acak100hsl.xlsx', index=False) #lalu simpan ke file excel

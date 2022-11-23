#pakai regex tdk ketemu (tdk berhasil, hasilnya Nan semua), jadi coba cara manual (with function) -> msh error
#df_participant['city'] = df_participant['address'].str.extract(r'(?<=\n)(\w,+)(?=,)') -> tdk berhasil

import pandas as pd
import numpy as np

bsdf = pd.read_csv('c:/xampp/htdocs/python/bs-participants.csv')

#buat dataFrame baru kosong kolom hasilnya (city)
df = pd.DataFrame([[""]], columns=['city'])

#list baru utk diisi data lalu utk disimpan di DataFrame tsb
list_data = []

#speacial char yg ada di ujung nama kota sbg tanda stop ambil char
specialChar = [',']

#looping row/record column/field address
for i in bsdf['address']:
    #variabel utk menyimpan hasil character2 yg membentuk nama kota
    result = ''
 
    firstchar = 'No'   
    #looping char yg ada di dlm row/record address
    for j in i:
        if j == '\n':  #nama kota ada stlh enter atau \n
            firstchar = 'Yes'
            continue
        else:          
            if firstchar == 'No': #bila char ada sblm enter atau \n
                continue
            else:   #char ada stlh enter atau \n
                if j not in specialChar: #bila char nya bukan koma, ambil/tampung char nya
                    result += j
                    continue
                else:
                    break #bila char nya adalah koma, sudahi/akhiri ambil/tampung char nya, pindah ke next alamat

    #tampung hasil result (kota) ke dlm list
    list_data.append(result)
    
#bsdf['city'] = bsdf.apply(StringChallenge, axis=1) #tdk berhasil dgn function krn ada looping di dlm
bsdf['city'] = np.array(list_data) #buat kolom baru di file yg sama, menggunakan numpy
bsdf.to_csv('c:/xampp/htdocs/python/bs-participants.csv', index=False) #simpan ke file yg sama
    
#simpan list ke dlm DataFrame, lalu ke file csv yg baru
df = pd.DataFrame(list_data, columns=['city'])
df.to_csv('c:/xampp/htdocs/python/bs-participants-city.csv', index=False)

                
        
    

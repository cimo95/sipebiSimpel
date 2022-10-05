import json, re

#muat data baku-takbaku
with open('baku.json','r') as fileBaku:
  dftBaku = json.loads(fileBaku.read())
  fileBaku.close()
  
#muat file dokumen yang akan diproses
with open('sampel0.txt','r') as fileTeks:
  isiTeks = fileTeks.read()
  fileTeks.close()
  
#buat dan urutkan daftar kata dari dokumen yang dimuat
sampelKata = re.sub('[^A-Za-z0-9 ]+', '', isiTeks)
sampelKata = list(dict.fromkeys(sampelKata.split()))
sampelKata.sort(key=len,reverse=True)

#proses setiap kata dalam daftar kata
for itemKata in sampelKata:
  try:
    #jika kata terdeteksi ambigu, beri keterangan
    ketAmbigu = ' (ambigu: '+itemKata+')' if dftBaku[itemKata]['ambi'] == 1 else ''
    
    #jika kata terdeteksi tak baku, maka ganti kata tersebut dengan yang baku
    if ' '+itemKata in isiTeks:
      isiTeks = isiTeks.replace(' '+itemKata,' '+dftBaku[itemKata]['baku']+ketAmbigu)
    else:
      isiTeks = isiTeks.replace(itemKata+' ',dftBaku[itemKata]['baku']+ketAmbigu+' ')
    
    #print hanya untuk referensi  
    print(itemKata+' -> '+dftBaku[itemKata]['baku']+ketAmbigu)
  except:
    pass
    
#simpan hasil proses
with open('sampel0_hasil.txt','w') as fileHasil:
  fileHasil.write(isiTeks)
  fileHasil.close()

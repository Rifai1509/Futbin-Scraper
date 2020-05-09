class Matematika():
    def pangkat(pertama, kedua):
        hasil = f'hasil dari operasi matematika tersebut adalah {int(pertama)**int(kedua)}'
        return hasil
    def jumlah(pertama,kedua):
        return int(pertama)+int(kedua)
    
def print_menu():
        menu ='''
silakan pilih(isi dengan angka)
1. Fungsi kuadrat
2. Penjumlahan
'''
        return print(menu)

while True:
    print_menu()    
    pilih = input('saya pilih nomor :')
    while True:
        if pilih == '1':
            print('ketikkan Y untuk melakukan operasi ini, K untukkembali')
            pilih2 = input('jawab :')
            if pilih2 == 'Y' or 'y': 
                try:
                    print(Matematika.pangkat(input('masukkanangka pertama :'),input('masukkan angka ke2 :')))
                except:
                    print('salah, sistem kembali')
                    break
            elif pilih2 == 'K' or 'k':
                break
            else:
                print('Anda macam-macam, sistem akan otomatis kembai, byee')
                break
                
        elif pilih == '2':
            try:
                print(Matematika.jumlah(input('masukkanangka pertama :'),input('masukkan angka ke2 :')))
                print("ketikkan huruf untuk kembali ke menu")
            except:
                print('oke, kembali ke menu')
                break
        else:
            print('Anda macam-macam, sistem akan otomatis kembai, byee')
            break    

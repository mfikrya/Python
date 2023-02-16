import os

# Muhammad Fikry Adiansyah - JCDSOL-009-031

data_siswa = [
    {
        'id siswa' : 'S01',
        'nama siswa' : 'Muhammad Fikry',
        'jenis kelamin' : 'Pria',
        'nilai akhir' : 85,
        'status' : 'Lulus',
    },
    {
        'id siswa' : 'S02',
        'nama siswa' : 'Alya Putri',
        'jenis kelamin' : 'Wanita',
        'nilai akhir' : 70,
        'status' : 'Tidak Lulus',
    }
]
data_baru = []

def osclear():
    sistem_operasi = os.name
    if sistem_operasi == "nt":
        os.name = os.system("cls")
    elif sistem_operasi == "posix":
        os.name = os.system("clear")
    return sistem_operasi

def list_menu():
    print("=== DATA NILAI SISWA ===")
    print("-"*85)
    print("1. Laporan Data Siswa")
    print("2. Tambah Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Keluar Program")
    print("-"*85)
    
def read():
    while (True): 
        print("--- Menu Laporan Data Siswa ---")
        print("-"*80) 
        print("1. Tampilkan Semua Data Siswa")
        print("2. Cari Data Siswa")
        print("3. Kembali Ke Menu Utama")
        print("-"*85)
        pilih = int(input("Silahkan Pilih Menu (1-3) : "))
        print("\n")
        if pilih == 1:
            show_data()
        elif pilih == 2:
            id_siswa = input("Masukan Id Siswa : ").upper()
            if len(search_data(id_siswa)):
                print("--- Berikut Data Yang Anda Cari ---")
                show_list(search_data(id_siswa))
            else:
                print("Data Tidak Ditemukan !")
        elif pilih == 3:
            main_menu()
            break
        else:
            print("Menu Tidak Ditemukan !")
            print("-"*85)

def add():
     while (True): 
        print("--- Menu Tambah Data Siswa ---")
        print("-"*80) 
        print("1. Tambah Data Siswa")
        print("2. Kembali Ke Menu Utama")
        print("-"*85)
        pilih = int(input("Silahkan Pilih Menu (1-2) : "))
        print("\n")
        if pilih == 1:
            
            id_siswa = input("Id Siswa : ").upper()
            cek_id = list(map(lambda a:a['id siswa'],data_siswa))
            if id_siswa in cek_id:
                print("Id Sudah Ada !")
            else:
                nama_siswa = input("Nama Siswa : ").capitalize()
                jenis_kelamin = input("Jenis Kelamin : ").capitalize()
                nilai = int(input("Nilai : "))
                if nilai > 80:
                    status = 'Lulus'
                else:
                    status = 'Tidak Lulus'
                create(id_siswa,nama_siswa,jenis_kelamin,nilai,status)
                print("--- Berikut Data Baru Anda ---")
                show_list(data_baru)
                save = input("Apakah Ingin Disimpan ? (y/n) : ")
                if save == "Y" or save == "y":
                    print("Data Berhasil Disimpan !")
                    data_siswa.extend(data_baru)
                    data_baru.clear()
                else:
                    print("Data Batal Disimpan !")
                    data_baru.clear()
                show_data()
        elif pilih == 2:
            main_menu()
            break
        else:
            print("Menu Tidak Ditemukan !")
            print("-"*85)
    
def update():
     while (True): 
        print("--- Menu Ubah Data Siswa ---")
        print("-"*80) 
        print("1. Ubah Data Siswa")
        print("2. Kembali Ke Menu Utama")
        print("-"*85)
        pilih = int(input("Silahkan Pilih Menu (1-2) : "))
        print("\n")
        if pilih == 1:
            show_data()
            Data = input("Silahkan Pilih Data ID Yang Ingin Diubah : ").upper()
            if len(search_data(Data)):
                show_list(search_data(Data))
                lanjut = input("Apakah Ingin Lanjut Ubah Data ? (y/n) : ")
                if lanjut == "Y" or lanjut == "y":
                    pilih_kolom = input("Pilih Kolom : ").lower()
                    if pilih_kolom == 'id siswa':
                        DataBaru = input("Id Baru : ").upper()
                        updateData(search_data(Data),'id siswa',DataBaru)
                    elif pilih_kolom == 'nama siswa':
                        DataBaru = input("Nama Siswa : ").capitalize()
                        updateData(search_data(Data),'nama siswa',DataBaru)
                    elif pilih_kolom == 'jenis kelamin':
                        DataBaru = input("Jenis Kelamin : ").capitalize()
                        updateData(search_data(Data),'jenis kelamin',DataBaru)
                    elif pilih_kolom == 'nilai akhir':
                        print("=============== WARNING !!! ===============")
                        print("Jika Nilai Akhir Berubah, Mungkin Status Juga Akan Berubah")
                        DataBaru = int(input("Nilai Siswa : "))
                        updateData(search_data(Data),'nilai akhir',DataBaru)
                        if  DataBaru > 80:
                            DataBaru = 'Lulus'
                            updateDataStatus(search_data(Data),'status',DataBaru)
                        else:
                            DataBaru = 'Tidak Lulus'
                            updateDataStatus(search_data(Data),'status',DataBaru)
                    elif pilih_kolom == 'status':
                        print("Kolom Otomatis Update Dari Nilai Akhir !")
                    else:
                        print("Kolom Tidak Ditemukan !")
                else:
                    print("Ubah Data Tidak Dilanjutkan !")              
            else:
                print("Data Tidak Ditemukan !")
        elif pilih == 2:
            main_menu()
            break
        else:
            print("Menu Tidak Ditemukan !")
            print("-"*85)

def delete():
    while(True):
        print("--- Menu Hapus Data Siswa ---")
        print("-"*80) 
        print("1. Hapus Data Siswa")
        print("2. Kembali Ke Menu Utama")
        print("-"*85)
        pilih_menu = int(input("Silahkan Pilih Menu (1-2) : "))
        if pilih_menu ==  1:
            show_data()
            Data = input("Silahkan Pilih ID Yang Ingin Dihapus : ").upper()
            if len(search_data(Data)):
                print("--- Data Yang Akan Dihapus ---")
                show_list(search_data(Data))
                deleteData(search_data(Data))
            else:
                print("Id Tidak Ditemukan !")
        elif pilih_menu == 2:
            main_menu()
            break
        else:
            print("Menu Tidak Ditemukan !")      

def main_menu():
    while (True):
        list_menu()
        menu = int(input("Silahkan Pilih Menu (1-5) : "))
        print("\n")
        if menu == 1:
            read()
            break
        elif menu == 2:
            add()
            break
        elif menu == 3:
            update()
            break
        elif menu == 4:
            delete()
            break
        elif menu == 5:
            print("Program Selesai, Terimakasih !")
            break
        else:
            print("Menu Tidak Ditemukan !")
            print("-"*60)
     
def show_data():
    id_siswa = 'ID Siswa'
    nama_siswa = 'Nama Siswa'
    jenis_kelamin = 'Jenis Kelamin'
    nilai_akhir = 'Nilai Akhir'
    status = 'Status'
    print("--- Data Siswa ---")
    print("-"*85)
    print(f"{id_siswa:5} | {nama_siswa:25} | {jenis_kelamin:15} | {nilai_akhir:3} | {status:12} |")
    print("-"*85)
    for id_siswa,data in enumerate(data_siswa):
        id_siswa =  data['id siswa']
        nama_siswa = data['nama siswa']
        jenis_kelamin = data['jenis kelamin']
        nilai_akhir = data['nilai akhir']
        status = data['status']
        print(f"{id_siswa:<8} | {nama_siswa:<25} | {jenis_kelamin:<15} | {nilai_akhir:<11} | {status:<12} |")
    print("-"*85)       

def search_data(id_siswa):
    output = list(filter(lambda data: data['id siswa'] in str(id_siswa),data_siswa))
    return output

def show_list(data):
    id_siswa = 'ID Siswa'
    nama_siswa = 'Nama Siswa'
    jenis_kelamin = 'Jenis Kelamin'
    nilai_akhir = 'Nilai Akhir'
    status = 'Status'
    print("-"*85)
    print(f"{id_siswa:5} | {nama_siswa:25} | {jenis_kelamin:15} | {nilai_akhir:3} | {status:12} |")
    print("-"*85)
    for id_siswa,data in enumerate(data):
        id_siswa =  data['id siswa']
        nama_siswa = data['nama siswa']
        jenis_kelamin = data['jenis kelamin']
        nilai_akhir = data['nilai akhir']
        status = data['status']
        print(f"{id_siswa:<8} | {nama_siswa:<25} | {jenis_kelamin:<15} | {nilai_akhir:<11} | {status:<12} |")
    print("-"*85)        

def create(id_siswa,nama_siswa,jenis_kelamin,nilai,status):
    data_baru.append(
        {
            'id siswa' : id_siswa,
            'nama siswa' : nama_siswa,
            'jenis kelamin' : jenis_kelamin,
            'nilai akhir' : nilai,
            'status' : status
        }
        
    )

def updateDataStatus(Data,pilih_kolom,DataBaru):
    Data[0][pilih_kolom] = DataBaru

def updateData(Data,pilih_kolom,DataBaru):
    simpan = input("Apakah Ingin Disimpan ? (y/n) : ")
    if simpan == "Y" or simpan == "y":
        Data[0][pilih_kolom] = DataBaru  
        print("Data Berhasil Disimpan !")   
    else:
        print("Data Batal Disimpan !")

def deleteData(Data):
    hapus = input("Apakah Ingin Dihapus ? (y/n) : ")
    if hapus == "Y" or hapus == "y":
        for a,val in enumerate(data_siswa):
            if val == Data[0]:
                del data_siswa[a]
                break
        print("Data Berhasil Dihapus !")   
    else:
        print("Data Batal Dihapus !")
                
    
while (True):
    osclear()
    main_menu()
    break

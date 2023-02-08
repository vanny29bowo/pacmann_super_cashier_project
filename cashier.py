
from tabulate import tabulate #Import library tabulate untuk proses pembuatan tabel pada display item belanja
import pandas as pd           #Import library pandas untuk membantu proses pembuatan tabel 


class Transaction():
    def __init__(self):
        """
        Fungsi inisialisasi transaksi Customer pada class Transaction
        self.dicts = Inisiasi instance dalam dictionary sebagai keranjang belanja bagi Customer

        """ 
        self.dicts={}

    
    def add_item(self,nama_item,jumlah_item,harga_item):

        """
        Fungsi menambahkan item ke directory

        Paremeter:
        nama_item(string) = nama item, key dari dictionary
        jumlah_item(int) = jumlah item, value dari dictionary pada indeks ke-0
        harga_item(int) = harga item, value dari dictionary pada indeks ke-1

        Return:
        Jika format data sudah sesuai mengembalikan informasi detail barang belanja yang berhasil ditambahkan,
        Jika belum akan menampilkan notifikasi kepada Customer untuk memasukkan format yang sesuai

        """ 

        #pengecekan tipe data yang diinput apakah sudah sesuai dengan tipe data yang ditentukan
        if type(nama_item)!=str:
            return print(f"Mohon masukkan nama item dengan format yang sesuai")

        elif type(jumlah_item)!=int:
            return print(f"Mohon masukkan jumlah item dengan format yang sesuai")

        elif type(harga_item)!=int:
            return print(f"Mohon masukkan harga item dengan format yang sesuai")

        else: 
            """jika tipe data semua parameter sudah sesuai maka akan dilakukan penambahan data, 
            sekaligus menambahkan value total harga setiap barang(jumlah_item*harga_item) pada 
            dari dictionary pada indeks ke-2"""

            self.dicts.update({nama_item:[jumlah_item,harga_item,jumlah_item*harga_item]}) #menggunakan method update dictionary
            return print(f"Berhasil menambahkan {nama_item} sejumlah {jumlah_item} item dengan harga per item Rp {harga_item}")

    
    def update_item_name(self,nama_item,nama_baru):
        
        """
        Fungsi merubah nama item lama menjadi nama item baru

        Paremeter:
        nama_item(string) = nama item lama
        nama_baru(string) = nama item baru

        Return:
        Jika format data sudah sesuai akan mengembalikan informasi nama barang berhasil diperbarui,
        Jika belum akan menampilkan notifikasi kepada Customer untuk memasukkan format yang sesuai
        
        """ 
        #melakukan pengecekan tipe data sebelum dilakukan perubahan nama item
        for i,j in list(self.dicts.items()):

            if i==nama_item:

                if type(nama_baru)!=str: #memvalidasi tipe data yang diinput apakah sudah sesuai
                    return print(f"Mohon masukkan nama item dengan format yang sesuai")
                        
                else:
                    self.dicts[nama_baru]=j #mengassign nama value dari item lama ke nama item yang baru
                    self.dicts.pop(i) #menghapus item lama sebelumnya menggunakan method pop()
                    return print(f"Berhasil memperbaharui nama item {nama_item} menjadi {nama_baru}")
                  
            elif i!=nama_item: 
                continue
              
        if nama_item not in self.dicts.keys(): #memvalidasi jika item yang diinput tidak ada di daftar belanja
            return print(f"Mohon cek kembali, item {nama_item} tidak ada di daftar belanja")

    
    def update_item_qty(self,nama_item,jumlah_baru):

        """
        Fungsi merubah jumlah quantity pada suatu item

        Paremeter:
        nama_item(string) = nama item
        jumlah_baru(int) = jumlah barang pada item yang dipilih

        Return:
        Jika format data sudah sesuai akan mengembalikan informasi jumlah barang berhasil diperbarui,
        Jika belum akan menampilkan notifikasi kepada Customer untuk memasukkan format yang sesuai
        
        """ 

        #melakukan pengecekan tipe data sebelum dilakukan perubahan jumlah item
        for i,j in list(self.dicts.items()):

            if i==nama_item:

                if type(jumlah_baru)!=int: #memvalidasi tipe data yang diinput apakah sudah sesuai
                    return print(f"Mohon masukkan jumlah item dengan format yang sesuai")
                    
                else:
                    j[0] = jumlah_baru #update quantity item

                    """memperbaharui value total harga setiap barang(jumlah_item*harga_item) 
                                  pada dari dictionary pada indeks ke-2"""
                    j[2]=j[0]*j[1] 
                    return print(f"Berhasil memperbaharui jumlah item pada {nama_item} menjadi {jumlah_baru} item")

            elif i!=nama_item: 
                continue
              
        if nama_item not in self.dicts.keys(): #memvalidasi jika item yang diinput tidak ada di daftar belanja
            return print(f"Mohon cek kembali, item {nama_item} tidak ada di daftar belanja")

    
    def update_item_price(self,nama_item,harga_baru):

        """
        Fungsi merubah harga barang pada suatu item

        Paremeter:
        nama_item(string) = nama item
        harga_item(int) = harga baru pada item yang dipilih

        Return:
        Jika format data sudah sesuai akan mengembalikan informasi harga barang berhasil diperbarui,
        Jika belum akan menampilkan notifikasi kepada Customer untuk memasukkan format yang sesuai

        """ 

        #melakukan pengecekan tipe data sebelum dilakukan pergantian nilai harga item
        for i,j in list(self.dicts.items()):

            if i==nama_item:

                if type(harga_baru)!=int: #memvalidasi tipe data yang diinput apakah sudah sesuai
                    return print(f"Mohon masukkan harga item dengan format yang sesuai")
                    
                else:
                    j[1] = harga_baru #update harga item
                    
                    """memperbaharui value total harga setiap barang(jumlah_item*harga_item) 
                                  pada dari dictionary pada indeks ke-2"""
                    j[2]=j[0]*j[1]
                    return print(f"Berhasil memperbaharui harga item pada {nama_item} menjadi {harga_baru} item")
            
            elif i!=nama_item: 
                continue
              
        if nama_item not in self.dicts.keys(): #memvalidasi jika item yang diinput tidak ada di daftar belanja
            return print(f"Mohon cek kembali, item {nama_item} tidak ada di daftar belanja")


    def delete_item(self,nama_item):

        """
        Fungsi menghapus salah satu item tertentu sesuai yang diinput oleh Customer

        Paremeter:
        nama_item(string) = jumlah item yang dihapus

        Menggunakan try-except untuk pengecekan kondisi jika Customer menginput nama barang yang tidak
        ada dalam daftar keranjang, maka Customer akan memeriksa kembali nama item yang akan diinput
       
        """ 
        try:
            self.dicts.pop(nama_item) #menggunakan method pop otomatis akan menghapus key+value pada dictionary
        except:
            print(f"Mohon cek kembali, item {nama_item} yang akan dihapus tidak ada di daftar belanja")
        else:
            print(f"Item {nama_item} telah berhasil dihapus")


    def reset_transaction(self):

        """
        Fungsi menghapus seluruh daftar belanja dari keranjang belanja

        Menggunakan try-except untuk pengecekan apakah sebelumnya telah terdapat daftar item

        Paremeter:
        self -> merujuk pada Instance dictionary/keranjang belanja
   
        """
        try:
            """"operasi penghapusan item belanja menggunakan method popitem() hanya untuk 
                  memastikan apakah sudah ada atau belum barang belanja pada item"""
            y=self.dicts.copy()
            y.popitem()
            self.dicts.clear()
            print(f"Semua daftar belanja telah dihapus")

        except:
            print(f"Tidak ada barang terhapus, Anda belum memasukkan daftar belanjar")


    def check_order(self):

        """
        Fungsi melakukan pengecekan daftar belanja apakah semua item yang ada dikeranjang sudah
        memiliki format tipe data yang sesuai atau mengecek apakah ada komponen belanja yang kosong/Null,
        jika iya maka akan sarankan Customer untuk melakukan pengecekan kembali/belanja terlebih dahulu.

        Paremeter:
        self -> merujuk pada Instance dictionary/keranjang belanja

        Menggunakan try-except untuk pengecekan kondisi tipe data

        Return:
        Daftar belanja secara keseluruhan menggunakan fungsi display
       
        """
        try:

            """"operasi penghapusan item belanja menggunakan method popitem() hanya untuk 
                  memastikan apakah sudah ada atau belum barang belanja pada item"""
            x = self.dicts.copy()
            x.popitem()

            try:
                for i,j in self.dicts.items():

                  """"operasi method pada string ini hanya untuk memastikan apakah tipe data pada value (nama_item) sudah bertipe string,
                              jika selain string maka akan error dan akan masuk ke kondisi except"""
                  i.split()

                  """"operasi pembagian ini hanya untuk memastikan apakah tipe data pada value (jumlah_item&harga_item) sudah bertipe integer,
                              jika selain integer maka akan error dan akan masuk ke kondisi except"""
                  a=j[0]/j[1]
            except:
                print(f"Terdapat kesalahan input data pada item, Mohon masukkan item dengan format yang sesuai")
                print(f"="*100)
                return self.display() #memangil method display untuk menampilkan daftar belanja keseluruhan

        except:
            print(f"Belum ada daftar item, mohon masukkan daftar item terlebih dahulu")
            
        else:
            print(f"Pemesanan sudah benar")
            print(f"="*100)
            return self.display() #memangil method display untuk menampilkan daftar belanja keseluruhan


    def display(self):

        """
        Fungsi untuk menampilkan total belanja secara keseluruhan

        Paremeter:
        self -> merujuk pada Instance dictionary/keranjang belanja

        Menggunakan library pandas untuk membuat tabel, kemudian dikonversi ke
        format tabel menggunakan library tabulate

        """
        header = ["No","Nama Item","Jumlah Item", "Harga/Item","Total Harga"]
        df1 = pd.DataFrame(data=self.dicts).T.reset_index() #menggunakan method Transpose dan reset_index untuk nilai pada kolom No
        df1.index+=1 #agar index mulai dari no 1
        print("Berikut daftar belanja Andi secara keseluruhan :\n")
        print(tabulate(df1, stralign="center", headers=header, tablefmt="github"))


    def total_price(self):

        """
        Fungsi untuk menjumlahkan total belanja secara keseluruhan dalam nilai Rupiah
        baik mendapat atau tidak mendapat diskon

        Paremeter:
        self -> merujuk pada Instance dictionary/keranjang belanja

        Menggunakan library pandas untuk membuat tabel, kemudian dikonversi ke
        format tabel menggunakan library tabulate
        
        """
        try:
            total_no_diskon = 0
            for i,j in self.dicts.items():

                """mengecek apakah format tipe data pada nama item(string) apakah sudah sesuai, jika belum masuk ke kondisi except"""
                i.split() 
                total_no_diskon+=j[2] #total belanja
        except:
            print(f"Terdapat kesalahan input data pada item, Tidak bisa melakukan penjumlahan Total item keseluruhan")

        #jika format data sudah sesuai maka akan masuk ke proses pengecekan apakah Customer eligible untuk mendapat diskon
        else: 

            if total_no_diskon>200_000: #belanja>200_000, Customer eligible mendapat diskon 5%
                print(f"Total belanja setelah mendapat diskon 5% adalah senilai Rp {total_no_diskon - (total_no_diskon*0.05):,.0f}")

            elif total_no_diskon>300_000: #belanja>300_000, Customer eligible mendapat diskon 8%
                print(f"Total belanja setelah mendapat diskon 8% adalah senilai Rp {total_no_diskon - (total_no_diskon*0.08):,.0f}")

            elif total_no_diskon>500_000: #belanja>500_000, Customer eligible mendapat diskon 10%
                print(f"Total belanja setelah mendapat diskon 10% adalah senilai Rp {total_no_diskon - (total_no_diskon*0.1):,.0f}")

            else:
                print(f"Total belanja adalah sebesar Rp {total_no_diskon} tanpa mendapat diskon")

# Studi_Kasus_5_Naufa-Fauza-Eky
nama: naufa fauza eky
nim: 2609116060
kelas: B

Penjelasan Singkat mengenai Studi Kasus 5 DDP
1. Fungsi
def hitung_biaya_parkir(jenis_kendaraan, durasi_parkir):
memasukkan parameter jenis kendaraan dan durasi parkir untuk menerima nilai dari masing-masing parameter yang akan didata sesuai dengan pengendara

2. if elif else dan return
if jenis_kendaraan == "motor":
        harga = 3000
    elif jenis_kendaraan == "mobil":
        harga = 5000
    elif jenis_kendaraan == "sepeda":
        harga = 2000
    elif jenis_kendaraan == "bus":
        harga = 10000
    else:
        return 0
   kode if elif else digunakan untuk menentukan biaya parkir per jam berdasarkan jenis kendaraan, jika jenis kendaraan yang dimasukkan tidak terdaftar maka harga 0

3. perhitungan dan return
   jumlah_pembayaran = harga * durasi_parkir
    return jumlah_pembayaran
   untuk menghitung jumlah pembayaran, harga dikali durasi parkir
   return jumlah pembayaran digunakan untuk mengembalikan jumlah nilai yang dibayar

4. Fungsi dan perhitungan
   def jumlah_pembayaran():
    jenis_kendaraan = input("masukkan jenis kendaraan anda: ")
    print("silahkan memasukkan jam masuk dan jam keluar (0-23), ")
    print("catatan: jika jam masuk/keluar menunjukkan lebih beberapa menit maka gunakan pembulatan ke atas. ")
    print("contoh: masuk jam 14.30 masukkan angka 14, keluar jam 19.40 masukkan angka 20. ")
    jam_masuk = int(input("masukkan jam masuk: "))
    jam_keluar = int(input("masukkan jam keluar: "))
   memasukkan kode agar pengguna bisa menginput jenis kendaraan, jam masuk dan keluar lalu menambahkan keterangan tambahan

    durasi_parkir = jam_keluar - jam_masuk
   menggunakan perhitungan diatas untuk memperoleh durasi parkir
   
    hasil = hitung_biaya_parkir(jenis_kendaraan, durasi_parkir)
   untuk mengirim data yang diinput ke fungsi pertama untuk dihitung

   5. Cetak struk
     print("===== STRUK PARKIR =====")
    print("jenis kendaraan: ", jenis_kendaraan)
    print("jam masuk: ", jam_masuk)
    print("jam keluar: ", jam_keluar)
    print("lama parkir: ", durasi_parkir, "jam")
    print("biaya parkir anda: Rp", hasil)
    print("Terimakasih telah menggunakan layanan kami!")
    untuk menampilkan informasi mengenai pembayaran biaya parkir dengan detail

    6. Pemanggilan fungsi
       jumlah_pembayaran()
       fungsinya dipanggil agar program dapat berjalan dari awal hingga selesai

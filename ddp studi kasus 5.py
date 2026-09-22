def hitung_biaya_parkir(jenis_kendaraan, durasi_parkir):
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

    jumlah_pembayaran = harga * durasi_parkir
    return jumlah_pembayaran

def jumlah_pembayaran():
    jenis_kendaraan = input("masukkan jenis kendaraan anda: ")
    print("silahkan memasukkan jam masuk dan jam keluar (0-23), ")
    print("catatan: jika jam masuk/keluar menunjukkan lebih beberapa menit maka gunakan pembulatan ke atas. ")
    print("contoh: masuk jam 14.30 masukkan angka 14, keluar jam 19.40 masukkan angka 20. ")
    jam_masuk = int(input("masukkan jam masuk: "))
    jam_keluar = int(input("masukkan jam keluar: "))

    durasi_parkir = jam_keluar - jam_masuk
    hasil = hitung_biaya_parkir(jenis_kendaraan, durasi_parkir)

    print("===== STRUK PARKIR =====")
    print("jenis kendaraan: ", jenis_kendaraan)
    print("jam masuk: ", jam_masuk)
    print("jam keluar: ", jam_keluar)
    print("lama parkir: ", durasi_parkir, "jam")
    print("biaya parkir anda: Rp", hasil)
    print("Terimakasih telah menggunakan layanan kami!")

jumlah_pembayaran()
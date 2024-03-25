import datetime

def main():
    # Dapatkan tahun saat ini dan jumlah hari dalam tahun tersebut
    tahun_sekarang = datetime.datetime.now().year
    jumlah_hari_dalam_tahun = 366 if tahun_sekarang % 4 == 0 and (tahun_sekarang % 100 != 0 or tahun_sekarang % 400 == 0) else 365

    # Baca sebuah bilangan bulat dari pengguna
    bilangan_bulat = int(input("Masukkan sebuah bilangan bulat: "))

    # Hitung hasilnya
    hasil = bilangan_bulat / jumlah_hari_dalam_tahun

    # Tampilkan hasil dengan hingga sebelas angka desimal
    hasil_terformat = "{:.11f}".format(hasil)
    print("Hasil:", hasil_terformat)

if __name__ == "__main__":
    main()

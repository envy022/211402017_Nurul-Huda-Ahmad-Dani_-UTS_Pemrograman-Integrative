import datetime

def main():
    # Mendapatkan tanggal hari ini
    tanggal_hari_ini = datetime.date.today()
    
    # Mengambil bilangan dari tanggal hari ini
    bilangan = tanggal_hari_ini.day

    # Menginisialisasi produk sebagai 1
    produk = 1

    # Menghitung hasil perkalian dari 1 hingga bilangan tersebut
    for i in range(1, bilangan + 1):
        produk *= i

    # Mencetak hasil
    print("Tanggal hari ini:", tanggal_hari_ini)
    print("Hasil perkalian dari 1 hingga bilangan (tanggal hari ini)", bilangan, "adalah:", produk)

if __name__ == "__main__":
    main()

from datetime import datetime, timedelta

def print_future_date(days):
    # Dapatkan tanggal saat ini
    current_date = datetime.now()
    
    # Hitung tanggal di masa depan
    future_date = current_date + timedelta(days=days)
    
    # Format output tanggal 
    formatted_date = future_date.strftime("%A, %d %B %Y")
    
    print("Tanggal " + str(days) + " hari dari sekarang adalah:", formatted_date)

print("Program Menghitung dan Mencetak Tanggal di Masa Depan")

while True:
    try:
        days = int(input("Masukkan jumlah hari dari sekarang: "))
        print_future_date(days)
        break  # keluar dari loop setelah berhasil mendapatkan input yang valid
    except ValueError:
        print("Masukkan jumlah hari dalam bentuk bilangan bulat.")

from koneksi import buat_koneksi
from koneksi import Error

def delete_data():
    koneksi = buat_koneksi()
    cursor = koneksi.cursor()

    id = int(input("Masukkan ID data yang ingin dihapus: "))
    read = "SELECT * FROM users WHERE id = %s"
    cursor.execute(read, (id,))
    results = cursor.fetchone()

    if results:
        print("Data yang akan dihapus:", results)
        konfirmasi = input("Apakah Anda ingin menghapus data ini? (y/n): ")
        
        if konfirmasi.lower() == 'y':
            sql = "DELETE FROM users WHERE id = %s"
            cursor.execute(sql, (id,))
            koneksi.commit()
            print("Data berhasil dihapus")
        else:
            print("Penghapusan data dibatalkan")
    else:
        print(f"Tidak ada data dengan ID {id}")

    cursor.close()
    koneksi.close()

# Contoh pemanggilan fungsi delete_data
if __name__ == "__main__":
    delete_data()

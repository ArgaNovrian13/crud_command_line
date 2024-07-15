from koneksi import buat_koneksi
from koneksi import Error

def update_data(id, nama, email):
    """Update data dalam tabel users berdasarkan id"""
    koneksi = buat_koneksi()
    if koneksi is not None:
        cursor = koneksi.cursor()
        # Membaca data berdasarkan id
        read = "SELECT * FROM users WHERE id = %s"
        cursor.execute(read, (id,))
        result = cursor.fetchone()
        if result:
            print("Data sebelum diupdate:", result)
            # Query untuk melakukan update
            sql = "UPDATE users SET nama = %s, email = %s WHERE id = %s"
            data = (nama, email, id)
            try:
                cursor.execute(sql, data)
                koneksi.commit()
                print("Data berhasil diupdate")
                # Menampilkan data setelah diupdate
                cursor.execute(read, (id,))
                updated_result = cursor.fetchone()
                print("Data setelah diupdate:", updated_result)
            except Error as e:
                print(f"Error: {e}")
        else:
            print(f"Tidak ada data dengan ID {id}")
        cursor.close()
        koneksi.close()
    else:
        print("Koneksi gagal")
if __name__ == "__main__":
    id = int(input("Masukkan ID data yang ingin diupdate: "))
    nama = input("Masukkan nama baru: ")
    email = input("Masukkan email baru: ")
    update_data(id, nama, email)

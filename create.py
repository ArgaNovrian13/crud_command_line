from koneksi import buat_koneksi
from koneksi import Error

def create_data(nama,email):
  """Memasukan Data Ke Dalam Database"""
  koneksi = buat_koneksi()
  if koneksi is not None:
    sql = "INSERT INTO users (id,nama,email) VALUES (NULL,%s,%s)"
    data = (nama,email)
    cursor = koneksi.cursor()
    try:
      cursor.execute(sql,data)
      koneksi.commit()
      print("Data Berhasil Di Masukan")
    except Error as e:
      print(f"Error : {e}")
    finally:
      cursor.close()
      koneksi.close()
      # print("Koneksi di tutup")
  # else:
  #   print("Koneksi Database Gagal")
if __name__ == "__main__":
  nama = input("Masukan Nama   :")
  email = input("Masukan Email :")
  create_data(nama,email)
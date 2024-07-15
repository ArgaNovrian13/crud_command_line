from koneksi import buat_koneksi
from koneksi import Error

def read_data():
  koneksi = buat_koneksi()
  if koneksi is not None:
    sql = 'SELECT * FROM users'
    cursor = koneksi.cursor()
    try:
      cursor.execute(sql)
      resutls = cursor.fetchall()
      print("Data Users")
      for row in resutls:
        print(row)
    except Error as e:
      print(f"Data Gagal di Tampilkan : {e}")
    finally:
      koneksi.close()
      cursor.close()
  else:
    print("Koneksi Gagal")

if __name__ == "__main__":
  read_data()
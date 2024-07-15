import mysql.connector
from mysql.connector import Error

def buat_koneksi():
  """ Membuat Koneksi ke Database Mysql"""
  koneksi = None
  try:
    koneksi = mysql.connector.connect(
      host="localhost",
      user="root",
      password='',
      database='python'
    )
    # if koneksi.is_connected():
    #   print("Koneksi Berhasil")
  except Error as e:
    print(f"Error : {e}")
  return koneksi
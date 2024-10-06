import rsa
import uuid
import psycopg2

from datetime import date

import common.util as util

publicKey, privateKey = rsa.newkeys(512)
conn = []

CONN_DBASE = "railway"
CONN_USER = "postgres"
CONN_HOST = "monorail.proxy.rlwy.net"
CONN_PASSWORD = "pReclBrMnyyzzEzmWvOUYKaPoXjJxXjK"
CONN_PORT = 21467

def get_node():
  return hex(uuid.getnode())

def encrypt(data):
  return rsa.encrypt(data.encode(), publicKey)

def decrypt(data):
  return rsa.decrypt(data, privateKey).decode()

def get_id():
  uuid = get_node()
  e_uuid = str(encrypt(uuid))

  return e_uuid

def open_connection():
  global conn
  conn = psycopg2.connect(
    database = CONN_DBASE,
    user = CONN_USER,
    host = CONN_HOST,
    password = CONN_PASSWORD,
    port = CONN_PORT
  )

def close_connection():
  conn.commit()
  conn.close()

def get_user_data():
  open_connection()
  val_uuid = get_node()

  cur = conn.cursor()
  sql = "SELECT level, expiration, account FROM jtool WHERE uuid=%(val)s;"
  cur.execute(sql, {"val": val_uuid})

  rows = cur.fetchall()

  cur.close()
  close_connection()

  return rows

def get_user_value():
  raw_data = get_user_data()
  raw_data_count = len(raw_data)
  val_uuid = get_node()

  if raw_data_count == util.STATE_ZERO:
    insert_user_value(val_uuid)
    raw_data = get_user_data()

  user_exp = raw_data[0][1]
  user_access = raw_data[0][0]
  today = date.today()

  if user_exp != None:
    if user_exp < today and user_access != util.ACCESS_FREE:
      update_user_free(val_uuid)
      raw_data = get_user_data()

  return raw_data[0]

def insert_user_value(id):
  open_connection()

  cur = conn.cursor()
  sql = "INSERT INTO jtool(uuid) VALUES(%(val)s);"
  cur.execute(sql, {"val": id})

  cur.close()
  close_connection()

def update_user_free(id):
  open_connection()

  cur = conn.cursor()
  sql = "UPDATE jtool SET level='Free' WHERE uuid=%(val)s;"
  cur.execute(sql, {"val": id})

  cur.close()
  close_connection()

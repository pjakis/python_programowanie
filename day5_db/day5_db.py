import psycopg2
import random

from my_functions import bulkInsert, deleteData, updateTable

from psycopg2 import Error

# create user janusz with encrypted password 'janusz';
# grant all privileges on database sample_db to user_name;

#\du+

# \create database test3;


#Polacz sie z baza danych
# conn_data = {
#     'user': 'postgres',
#     'host': '127.0.0.1',
#     'port':"5432",
#     'database': 'postgres',
#     'password': 'pawel123',
# }


conn_data = {
    'user': 'jan',
    'host': '127.0.0.1',
    'port':"5432",
    'database': 'test22',
    'password': 'jan',
}


connection = psycopg2.connect(**conn_data)

#
#create table(C)
cursor = connection.cursor()
# create_table_query = '''CREATE TABLE IF NOT EXISTS mobile4
#           (ID INT PRIMARY KEY     NOT NULL,
#           MODEL           TEXT    NOT NULL,
#           PRICE         FLOAT); '''
# # # Execute a command: this creates a new table
# cursor.execute(create_table_query)
# connection.commit()
#
# print("Potwierdzenie, ze prawidlowo polaczylismy sie z baza danych", connection)
# print("Table created successfully in PostgreSQL ")

#\dt - podejrzenie jaka stworzylismy tabele
#
#
# # # Executing a SQL query to insert data into  table mobile2
# model_list = ["Xiaomi", "Iphone", "Motorola", "Nokia"]
#
#
# #insert one line

# insert_query = """ INSERT INTO mobile2 (ID, MODEL, PRICE) VALUES (1, 'Iphone12', 1100)"""
# cursor.execute(insert_query)
# connection.commit()

# insert_query = """ INSERT INTO mobile2 (ID, MODEL, PRICE) VALUES (2, 'Iphone1333', 99999)"""
# cursor.execute(insert_query)
# connection.commit()


#select * from mobile2; --> sprawdzic w tabeli mobile2

#
#
# insert many lines

# list of rows to be inserted
# values = [(99, 'szajomi', 67), (109, 'szajsung', 79), (180, 'majphone1', 95)]
#
# # executing the sql statement
# cursor.executemany("INSERT INTO mobile2 (ID, MODEL, PRICE) VALUES(%s,%s,%s)", values)
# connection.commit()
#
#
# #by function
#
# values = [(17, 'szajomi', 67), (18, 'szajsung', 79), (19, 'majphone', 95)]
#
# bulkInsert(values, connection)
#
#
#
# #generate new_lines
#
# # for i in range(1,5):
# #     id, model, price = i, random.choice(model_list), random.randint(2000,5000)
# #     insert_query = """INSERT INTO mobile2 (ID, MODEL, PRICE) VALUES ({}, '{}', {})""".format(id, str(model), price)
# #     cursor.execute(insert_query)
# #     connection.commit()
# #     print(insert_query)
#
#
#

#
#
#
#
#
#update line

# update_query = """Update mobile2 set price = 2133333 where id = 1"""
# cursor.execute(update_query)
# connection.commit()


#delete table

# drop table mobile5; # usun tabele o nazwie mobile5


# mobileId = 1
# deleteData(mobileId, connection)

# mobileId = 2
# deleteData(mobileId, connection)








# select * from mobile2 order by id; wyswietlenie w kolejnosci rosnacej po id


#
#
# #by function
#
# connection = psycopg2.connect(**conn_data)
# updateTable(19, 9999, connection)
#
#
# #update from list
#
#
# #deleltion by id
#
# # connection = psycopg2.connect(**conn_data)
# # deleteData(17, connection)
#


# #zrzuc rezultat do listy
# cursor.execute("SELECT * FROM mobile2")
#
# przechwyc_dane = cursor.fetchall()
#
# print("Result ", przechwyc_dane)


#zadania bojowe

#wygerowac liste  krotek o nazwie telefony_lista, w ktorej bedzie piec wierszy
#w kazdym wierszu(krotce) maja sie znalezc 3 elementy - id, model, rocznik


#nastepnie telefony_lista zapisac to tabeli moje_telefony(pamietamy o tym, ze tabele
# telefony nalezy utworzyc w bazie test22

telefony_lista = []
for i in range(5):
    krotka = [(i+1, 'ajfon'+str(i), 2010 + i) ]
    telefony_lista.extend(krotka)

create_table_query = '''CREATE TABLE IF NOT EXISTS moje_telefony
          (ID INT PRIMARY KEY     NOT NULL,
          MODEL           TEXT    NOT NULL,
          ROK         INT); '''
# # Execute a command: this creates a new table
cursor.execute(create_table_query)
connection.commit()

values1 = telefony_lista

cursor.executemany("INSERT INTO moje_telefony (ID, MODEL, ROK) VALUES(%s,%s,%s)", values1)
connection.commit()


#w druga strone,

#pobrac wszystkie dane z tabeli moje_telefony, do otrzymanej listy krotek
#podac kolejny element tzn cena
# i zapisac rezulat  do pliku txt o nazwie output_db.txt
#kazda krotka ma byc w nowej linii
#(1, 'ajfon', 2020, 30000)
#(2, 'ajfon', 2020, 50000)


# tuple(list(krotka).append(20000))

import mysql_setup as ms

pw = "yuqwert55"
connection = ms.create_server_connection("localhost", "root", pw)

create_database_query = "CREATE DATABASE school"
ms.create_database(connection, create_database_query)
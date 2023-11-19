import pandas as pd

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    database="moviehub",
    user="root",
    password="mysqlpassword"
)
c = mydb.cursor()

def view_movies():
	c.execute('SELECT title, release_year, runtime FROM movie')
	data = c.fetchall()
	return data

def filterbyyear(year):
    c.execute('SELECT title, release_year, runtime FROM movie WHERE release_year = %s', (year,))
    data = c.fetchall()
    return data
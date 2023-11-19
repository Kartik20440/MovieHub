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
    c.execute('SELECT title, overview, runtime FROM movie WHERE release_year = %s', (year,))
    data = c.fetchall()
    return data

def filterbyrating(rating):
    if(rating == "Increasing"):
        c.execute('''SELECT 
    m.title AS Title,
    m.release_year AS Release_Year,
    ROUND(
        (
            COALESCE(r.tmdb_rating * 2, 0) + COALESCE(r.imdb_rating, 0) + COALESCE(r.mldb_rating * 2, 0)
        ) / 
        NULLIF(
            (
                CASE WHEN r.tmdb_rating IS NOT NULL THEN 1 ELSE 0 END +
                CASE WHEN r.imdb_rating IS NOT NULL THEN 1 ELSE 0 END +
                CASE WHEN r.mldb_rating IS NOT NULL THEN 1 ELSE 0 END
            ), 0
        ), 2) AS Rating,
    m.overview AS Overview
FROM Movie m
LEFT JOIN Ratings r ON m.imdb_link = r.id
ORDER BY Rating ASC''')
        data = c.fetchall()
        return data
    
    else:
        c.execute('''SELECT 
    m.title AS Title,
    m.release_year AS Release_Year,
    ROUND(
        (
            COALESCE(r.tmdb_rating * 2, 0) + COALESCE(r.imdb_rating, 0) + COALESCE(r.mldb_rating * 2, 0)
        ) / 
        NULLIF(
            (
                CASE WHEN r.tmdb_rating IS NOT NULL THEN 1 ELSE 0 END +
                CASE WHEN r.imdb_rating IS NOT NULL THEN 1 ELSE 0 END +
                CASE WHEN r.mldb_rating IS NOT NULL THEN 1 ELSE 0 END
            ), 0
        ), 2) AS Rating,
    m.overview AS Overview
FROM Movie m
LEFT JOIN Ratings r ON m.imdb_link = r.id
ORDER BY Rating DESC''')
        data = c.fetchall()
        return data
    

def filterbyruntime(runtime):
    if(runtime == "Short"):
        c.execute('Select title, release_year, runtime, overview From movie Where runtime <= 100')
        data = c.fetchall()
        return data
    else:
        c.execute('Select title, release_year, runtime, overview From movie Where runtime > 100')
        data = c.fetchall()
        return data

def filterbyearning(earn):
    if(earn == "Profit"):
        c.execute('Select title, release_year, overview, revenue-budget as earning From movie Where revenue-budget>0 and revenue!=0 and budget!=0')
        data = c.fetchall()
        return data
    else:
        c.execute('Select title, release_year, overview, revenue-budget as earning From movie Where revenue-budget<0 and revenue!=0 and budget!=0')
        data = c.fetchall()
        return data
     
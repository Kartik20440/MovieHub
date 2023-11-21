import pandas as pd

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    database="moviehub",
    user="root",
    password="mysqlpassword"
)
c = mydb.cursor()

# ###############################################################################################################################################################
def view_movies():
	c.execute('SELECT title, release_year, runtime FROM movie')
	data = c.fetchall()
	return data

def filterbyyear(year):
    c.execute('SELECT title, overview, runtime FROM movie WHERE release_year = %s', (year,))
    data = c.fetchall()
    return data

def filterbyrating(rating):
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
    Having Rating >= %s''', (rating,))
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

def filterbyrelease_rating(release, rate):
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
WHERE m.release_year = %s
Having Rating >= %s''',(release,rate,))
    data = c.fetchall()
    return data

def filterbyrelease_length(release, length):
    if(length == "Short"):
        c.execute('Select title, release_year, runtime, overview From movie Where runtime <= 100 and release_year = %s', (release,))
        data = c.fetchall()
        return data
    else:
        c.execute('Select title, release_year, runtime, overview From movie Where runtime > 100 and release_year = %s', (release,))
        data = c.fetchall()
        return data

def filterbyrelease_earning(release, earn):
    if(earn == "Profit"):
        c.execute('Select title, release_year, overview, revenue-budget as earning From movie Where revenue-budget>0 and revenue!=0 and budget!=0 and release_year = %s', (release,))
        data = c.fetchall()
        return data
    else:
        c.execute('Select title, release_year, overview, revenue-budget as earning From movie Where revenue-budget<0 and revenue!=0 and budget!=0 and release_year = %s', (release,))
        data = c.fetchall()
        return data

def filterbyrating_length(rate, length):
    if(length == "Short"):
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
m.runtime as Runtime
FROM Movie m
LEFT JOIN Ratings r ON m.imdb_link = r.id
WHERE m.Runtime <= 100
Having Rating >= %s''',(rate,))
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
m.runtime as Runtime
FROM Movie m
LEFT JOIN Ratings r ON m.imdb_link = r.id
WHERE m.Runtime > 100
Having Rating >= %s''',(rate,))
        data = c.fetchall()
        return data
    
def filterbyrating_earning(rate,earn):
    if(earn == "Profit"):
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
m.revenue-m.budget as earning
FROM Movie m
LEFT JOIN Ratings r ON m.imdb_link = r.id
WHERE m.revenue-m.budget>0 and m.revenue!=0 and m.budget!=0
Having Rating >= %s''',(rate,))
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
m.revenue-m.budget as earning
FROM Movie m
LEFT JOIN Ratings r ON m.imdb_link = r.id
WHERE m.revenue-m.budget<0 and m.revenue!=0 and m.budget!=0
Having Rating >= %s''',(rate,))
        data = c.fetchall()
        return data
    
def filterbylength_earning(length, earn):
    if(earn == "Profit"):
        if(length == "Short"):
            c.execute('''Select title, release_year, runtime, revenue-budget as earning From movie Where revenue-budget>0 and revenue!=0 and budget!=0 and runtime <= 100''')
            data = c.fetchall()
            return data
        else:
            c.execute('''Select title, release_year, runtime, revenue-budget as earning From movie Where revenue-budget>0 and revenue!=0 and budget!=0 and runtime > 100''')
            data = c.fetchall()
            return data
    else:
        if(length == "Short"):
            c.execute('''Select title, release_year, runtime, revenue-budget as earning From movie Where revenue-budget<0 and revenue!=0 and budget!=0 and runtime <= 100''')
            data = c.fetchall()
            return data
        else:
            c.execute('''Select title, release_year, runtime, revenue-budget as earning From movie Where revenue-budget<0 and revenue!=0 and budget!=0 and runtime > 100''')
            data = c.fetchall()
            return data

def filterbyrelease_rating_length(release, rate, length):
    if(length == "Short Film"):
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
m.runtime as Runtime
FROM Movie m
LEFT JOIN Ratings r ON m.imdb_link = r.id
WHERE m.Runtime <= 100 and m.release_year = %s
Having Rating >= %s''',(release,rate,))
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
m.runtime as Runtime
FROM Movie m
LEFT JOIN Ratings r ON m.imdb_link = r.id
WHERE m.Runtime > 100 and m.release_year = %s
Having Rating >= %s''',(release,rate,))
        data = c.fetchall()
        return data
    
def filterbyrelease_rating_earning(release, rate, earn):
    if(earn == "Profit"):
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
m.revenue-m.budget as earning
FROM Movie m
LEFT JOIN Ratings r ON m.imdb_link = r.id
WHERE m.revenue-m.budget>0 and m.revenue!=0 and m.budget!=0 and m.release_year = %s
Having Rating >= %s''',(release,rate,))
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
m.revenue-m.budget as earning
FROM Movie m
LEFT JOIN Ratings r ON m.imdb_link = r.id
WHERE m.revenue-m.budget<0 and m.revenue!=0 and m.budget!=0 and m.release_year = %s
Having Rating >= %s''',(release,rate,))
        data = c.fetchall()
        return data
    
def filterbyrelease_length_earning(release,length,earn):
    if(earn == "Profit"):
        if(length == "Short Film"):
            c.execute('''Select title, release_year, runtime, revenue-budget as earning From movie Where revenue-budget>0 and revenue!=0 and budget!=0 and runtime <= 100 and release_year = %s''',(release,))
            data = c.fetchall()
            return data
        else:
            c.execute('''Select title, release_year, runtime, revenue-budget as earning From movie Where revenue-budget>0 and revenue!=0 and budget!=0 and runtime > 100 and release_year = %s''',(release,))
            data = c.fetchall()
            return data
    else:
        if(length == "Short Film"):
            c.execute('''Select title, release_year, runtime, revenue-budget as earning From movie Where revenue-budget<0 and revenue!=0 and budget!=0 and runtime <= 100 and release_year = %s''',(release,))
            data = c.fetchall()
            return data
        else:
            c.execute('''Select title, release_year, runtime, revenue-budget as earning From movie Where revenue-budget<0 and revenue!=0 and budget!=0 and runtime > 100 and release_year = %s''',(release,))
            data = c.fetchall()
            return data
        
def filterbyrating_length_earning(rate,length,earn):
    if(earn == "Profit"):
        if(length == "Short Film"):
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
m.runtime as Runtime,
m.revenue-m.budget as earning
FROM Movie m
LEFT JOIN Ratings r ON m.imdb_link = r.id
WHERE m.revenue-m.budget>0 and m.revenue!=0 and m.budget!=0 and m.Runtime<=100
Having Rating >= %s''',(rate,))
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
m.runtime as Runtime,
m.revenue-m.budget as earning
FROM Movie m
LEFT JOIN Ratings r ON m.imdb_link = r.id
WHERE m.revenue-m.budget>0 and m.revenue!=0 and m.budget!=0 and m.runtime > 100
Having Rating >= %s''',(rate,))
            data = c.fetchall()
            return data

    else:
        if(length == "Short Film"):
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
m.runtime as Runtime,
m.revenue-m.budget as earning
FROM Movie m
LEFT JOIN Ratings r ON m.imdb_link = r.id
WHERE m.revenue-m.budget<0 and m.revenue!=0 and m.budget!=0 and m.Runtime<=100
Having Rating >= %s''',(rate,))
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
m.runtime as Runtime,
m.revenue-m.budget as earning
FROM Movie m
LEFT JOIN Ratings r ON m.imdb_link = r.id
WHERE m.revenue-m.budget<0 and m.revenue!=0 and m.budget!=0 and m.runtime > 100
Having Rating >= %s''',(rate,))
            data = c.fetchall()
            return data

def filterbyrelease_rating_length_earning(release,rate,length,earn):
    if(earn == "Profit"):
        if(length == "Short Film"):
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
m.runtime as Runtime,
m.revenue-m.budget as earning
FROM Movie m
LEFT JOIN Ratings r ON m.imdb_link = r.id
WHERE m.revenue-m.budget>0 and m.revenue!=0 and m.budget!=0 and m.Runtime<=100 and m.release_year=%s
Having Rating >= %s''',(release,rate,))
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
m.runtime as Runtime,
m.revenue-m.budget as earning
FROM Movie m
LEFT JOIN Ratings r ON m.imdb_link = r.id
WHERE m.revenue-m.budget>0 and m.revenue!=0 and m.budget!=0 and m.runtime > 100 and m.release_year=%s
Having Rating >= %s''',(release,rate,))
            data = c.fetchall()
            return data

    else:
        if(length == "Short Film"):
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
m.runtime as Runtime,
m.revenue-m.budget as earning
FROM Movie m
LEFT JOIN Ratings r ON m.imdb_link = r.id
WHERE m.revenue-m.budget<0 and m.revenue!=0 and m.budget!=0 and m.Runtime<=100 and m.release_year=%s
Having Rating >= %s''',(release,rate,))
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
m.runtime as Runtime,
m.revenue-m.budget as earning
FROM Movie m
LEFT JOIN Ratings r ON m.imdb_link = r.id
WHERE m.revenue-m.budget<0 and m.revenue!=0 and m.budget!=0 and m.runtime > 100 and m.release_year=%s
Having Rating >= %s''',(release,rate,))
            data = c.fetchall()
            return data

# ###############################################################################################################################################################
def view_people():
    c.execute('SELECT name, profession, gender, birthyear FROM person')
    data = c.fetchall()
    return data

def filterbygender(gen):
    c.execute('SELECT name, profession, gender, birthyear FROM person WHERE gender = %s', (gen,))
    data = c.fetchall()
    return data

def filterbyprofession(profession):
    c.execute("SELECT name, profession, gender, birthyear FROM person WHERE profession LIKE '%{}%'".format(profession))
    data = c.fetchall()
    return data

def filterbyage(age):
    c.execute('''
    SELECT name,
    CASE
        WHEN deathyear IS NOT NULL THEN deathyear - birthyear
        ELSE YEAR(NOW()) - birthyear
    END AS age,
    birthyear,
    CASE
        WHEN deathyear IS NOT NULL THEN deathyear
        ELSE NULL
    END AS deathyear
FROM person
WHERE(
    (deathyear IS NOT NULL AND deathyear - birthyear >= %s)
    OR
    (deathyear IS NULL AND (YEAR(NOW()) - birthyear) >= %s))''',(age,age,))
    data = c.fetchall()
    return data
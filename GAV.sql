-- --------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------

DROP VIEW IF EXISTS movie;
CREATE VIEW Movie AS
SELECT
    imdb_link,
    MAX(title) AS title,
    MAX(original_title) AS original_title,
    MAX(Release_Year) AS release_year,
    MAX(runtime) AS runtime,
    MAX(is_Adult) AS isAdult,
    MAX(overview) AS overview,
    MAX(revenue) AS revenue,
    MAX(budget) AS budget
FROM (
    SELECT
        imdb_link,
        primary_title AS title,
        original_title,
        year(release_date) AS Release_Year,
        runtime,
        is_Adult,
        NULL AS overview, 
        NULL AS revenue,
        NULL AS budget
    FROM imdbmovie
    UNION
    SELECT
        imdb_link,
        title,
        original_title,
        year(release_date) AS Release_Year,
        NULL AS runtime, 
        NULL AS isAdult,
        overview,
        revenue,
        budget
    FROM tmdbmovie
    UNION
    SELECT
        imdb_link,
        title,
        NULL AS original_title,
        release_date,
        NULL AS runtime,
        NULL AS isAdult,
        NULL AS overview,
        NULL AS revenue,
        NULL AS budget
    FROM mldbmovie
    UNION
    SELECT
        imdb_link,
        title,
        NULL AS original_title,
        release_date,
        NULL AS runtime,
        NULL AS isAdult,
        NULL AS overview,
        NULL AS revenue,
        NULL AS budget
    FROM timdbmovie
) AS combined_data
GROUP BY imdb_link;

-- --------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------

CREATE VIEW Person AS
SELECT 
    Name,
    MAX(Birthyear) AS Birthyear,
    MAX(Deathyear) AS Deathyear,
    MAX(Profession) AS Profession,
    MAX(Gender) AS Gender,
    MAX(Nationality) AS Nationality,
    MAX(IMDB_Link) AS IMDB_Link
FROM (
    SELECT 
        COALESCE(t.name, i.name, c.name) AS Name,
        COALESCE(i.birthday, c.birthday) AS Birthyear,
        COALESCE(i.deathday, NULL) AS Deathyear,
        i.primary_profession AS Profession,
        c.gender AS Gender,
        CASE 
            WHEN c.nationality = 'in' THEN 'India'
            ELSE NULL 
        END AS Nationality,
        COALESCE(t.imdb_link, i.imdb_link) AS IMDB_Link
    FROM capiperson c
    LEFT JOIN tmdbperson t ON c.name = t.name
    LEFT JOIN imdbperson i ON c.name = i.name
) AS subquery
GROUP BY Name;

-- --------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------

CREATE VIEW Ratings AS
SELECT
    i.id,
    m.primary_title,
    t.rating AS tmdb_rating,
    i.rating AS imdb_rating,
    ml.rating AS mldb_rating
FROM
    IMDBMovie m
LEFT JOIN
    TIMDBRatings t ON m.imdb_link = t.imdb_link
LEFT JOIN
    IMDBRatings i ON m.imdb_link = i.id
LEFT JOIN
    MLDBRatings ml ON m.imdb_link = ml.imdb_link;
-- --------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------

CREATE VIEW Movie AS
SELECT
    primary_title AS title,
    original_title,
    year(release_date) AS Release_Year,
    runtime,
    is_Adult AS isAdult,
    NULL AS overview, -- NULL for columns from tables that do not have these fields
    NULL AS revenue,
    NULL AS budget,
    imdb_link
FROM imdbmovie
UNION
SELECT
    title,
    original_title,
    year(release_date) AS Release_Year,
    NULL AS runtime, -- NULL for columns from tables that do not have these fields
    NULL AS isAdult,
    overview,
    revenue,
    budget,
    imdb_link
FROM tmdbmovie
UNION
SELECT
    title,
    NULL AS original_title, -- NULL for columns from tables that do not have these fields
    release_date,
    NULL AS runtime,
    NULL AS isAdult,
    NULL AS overview,
    NULL AS revenue,
    NULL AS budget,
    imdb_link
FROM mldbmovie
UNION
SELECT
    title,
    NULL AS original_title,
    release_date,
    NULL AS runtime,
    NULL AS isAdult,
    NULL AS overview,
    NULL AS revenue,
    NULL AS budget,
    imdb_link
FROM timdbmovie;

-- --------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------

CREATE VIEW Person AS
SELECT
    name AS Name,
    birthday AS Birthyear,
    deathday AS Deathyear,
    primary_profession AS Profession,
    NULL AS Gender,
    NULL AS Nationality,
    imdb_link AS IMDB_Link
FROM imdbperson
UNION
SELECT
    name AS Name,
    YEAR(birthday) AS Birthyear,
    YEAR(deathday) AS Deathyear,
    NULL AS Profession,
    NULL AS Gender,
    home_country AS Nationality,
    imdb_link AS IMDB_Link
FROM tmdbperson
UNION
SELECT
    name AS Name,
    birthday AS Birthyear,
    NULL AS Deathyear,
    occupation AS Profession,
    gender AS Gender,
    NULL AS Nationality,
    NULL AS IMDB_Link
FROM capiperson;

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
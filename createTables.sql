DROP TABLE IF EXISTS IMDBMovie;
CREATE TABLE IMDBMovie (
    mid INT NOT NULL AUTO_INCREMENT,
    primary_title VARCHAR(255),
    original_title VARCHAR(255),
    release_date DATE,
    runtime INT,
    is_adult BOOLEAN,
    imdb_link TEXT,
    genres TEXT,
    PRIMARY KEY (mid)
);

DROP TABLE IF EXISTS IMDBPerson;
CREATE TABLE IMDBPerson(
    mid INT NOT NULL,
    name VARCHAR(255),
    birthday INT,
    deathday INT,
    primary_profession TEXT,
    known_for TEXT,
    imdb_link TEXT,
    PRIMARY KEY (mid)
);

DROP TABLE IF EXISTS IMDBRatings;
CREATE TABLE IMDBRatings(
    id TEXT,
    rating FLOAT,
    votes INTEGER
);

DROP TABLE IF EXISTS TMDBMovie;
CREATE TABLE TMDBMovie (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(255),
    original_title VARCHAR(255),
    release_date DATE,
    runtime FLOAT,
    is_adult BOOLEAN,
    imdb_link TEXT,
    overview TEXT,
    popularity FLOAT,
    poster_path TEXT,
    collection_belongs_to TEXT,
    revenue FLOAT,
    budget FLOAT,
    tagline TEXT,
    homepage_link TEXT,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS TMDBPerson;
CREATE TABLE TMDBPerson(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    birthday DATE,
    deathday DATE,
    alias_name VARCHAR(255),
    gender TEXT,
    biography TEXT,
    profile_path TEXT,
    popularity FLOAT,
    place_of_birth VARCHAR(255),
    homepage TEXT,
    home_country VARCHAR(255),
    imdb_link TEXT,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS RTMovie;
CREATE TABLE RTMovie(
    title TEXT,
    cast1 TEXT,
    cast2 TEXT,
    description TEXT,
    director TEXT,
    genre TEXT,
    rating TEXT
);

DROP TABLE IF EXISTS TIMDBMovie;
CREATE TABLE TIMDBMovie(
    movieid TEXT,
    title TEXT,
    release_date TEXT,
    imdb_link TEXT
);

DROP TABLE IF EXISTS TIMDBRatings;
CREATE TABLE TIMDBRatings(
    movieid TEXT,
    imdb_link TEXT,
    rating FLOAT
);

DROP TABLE IF EXISTS mldbmovie;
CREATE TABLE mldbmovie(
	movieid TEXT,
    title TEXT,
    release_date TEXT,
    imdb_link TEXT
);

DROP TABLE IF EXISTS mldbratings;
CREATE TABLE mldbratings(
    movieid TEXT,
    imdb_link TEXT,
    rating FLOAT
);

DROP TABLE IF EXISTS CAPIPerson;
CREATE TABLE CAPIPerson(
    name TEXT,
    birthday INT,
    occupation TEXT,
    gender TEXT,
    nationality TEXT
);

DROP TABLE IF EXISTS Mapping;
CREATE TABLE Mapping(
    movieId TEXT,
    imdbId TEXT,
    tmdbId TEXT,
    timdbId TEXT
);
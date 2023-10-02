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
    mid INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    birthday YEAR,
    deathday YEAR,
    primary_profession TEXT,
    known_for TEXT,
    imdb_link TEXT,
    PRIMARY KEY (mid)
);

DROP TABLE IF EXISTS IMDBRatings;
CREATE TABLE IMDBRatings(
    id TEXT,
    rating FLOAT,
    votes INTEGER,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS TMDBMovie;
CREATE TABLE TMDBMovie (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(255),
    original_title VARCHAR(255),
    release_date DATE,
    runtime INT,
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

DROP TABLE IF EXISTS Mapping;
CREATE TABLE Mapping(
    movieId TEXT,
    imDBId TEXT,
    tmdbId TEXT
);

DROP TABLE IF EXISTS MovieRatings;
CREATE TABLE MovieRatings(
    uid TEXT,
    mid TEXT,
    rating INTEGER
);
SHOW DATABASES;

CREATE DATABASE IF NOT EXISTS instagram;
    
USE instagram;

CREATE TABLE IF NOT EXISTS profiles (
    sid BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    profile_id VARCHAR(255) NOT NULL,
    profile_name VARCHAR(255),
    firstname_lastname VARCHAR(255),
    description VARCHAR(255),
    following INT NOT NULL,
    followers INT NOT NULL,
    n_posts INT NOT NULL,
    url VARCHAR(255),
    cts TIMESTAMP,
    is_business_account BOOLEAN
);

CREATE TABLE IF NOT EXISTS posts (
    sid BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    sid_profile BIGINT,
    post_id VARCHAR(255),
    profile_id BIGINT NOT NULL,
    location_id BIGINT NOT NULL,
    cts VARCHAR(255),
    post_type INT NOT NULL,
    description VARCHAR(255),
    number_likes INT NOT NULL,
    number_comments INT NOT NULL
);

CREATE TABLE IF NOT EXISTS locations (
    sid BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    street VARCHAR(255),
    zip VARCHAR(255),
    city VARCHAR(255),
    region VARCHAR(255),
    cd VARCHAR(8),
    phone VARCHAR(255),
    blurb VARCHAR(255),
    dir_city_id VARCHAR(255),
    dir_city_name VARCHAR(255),
    dir_city_slug VARCHAR(255),
    dir_country_id VARCHAR(255),
    dir_country_name VARCHAR(255),
    lat FLOAT NOT NULL,
    lng FLOAT NOT NULL,
    primary_alias_on_fb VARCHAR(255),
    slug VARCHAR(255),
    website VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS locations1 (
    sid BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    street VARCHAR(255),
    zip VARCHAR(255),
    city VARCHAR(255),
    region VARCHAR(255),
    cd VARCHAR(8),
    phone VARCHAR(255),
    blurb VARCHAR(255),
    dir_city_id VARCHAR(255),
    dir_city_name VARCHAR(255),
    dir_city_slug VARCHAR(255),
    dir_country_id VARCHAR(255),
    dir_country_name VARCHAR(255),
    lat FLOAT NOT NULL,
    lng FLOAT NOT NULL,
    primary_alias_on_fb VARCHAR(255),
    slug VARCHAR(255),
    website VARCHAR(255)
);


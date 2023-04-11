SHOW DATABASES;

CREATE DATABASE IF NOT EXISTS instagram;
    
USE instagram;

CREATE TABLE IF NOT EXISTS profiles (
    sid BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    profile_id VARCHAR(255),
    profile_name VARCHAR(255),
    firstname_lastname VARCHAR(255),
    description VARCHAR(255),
    following ,
    followers,
    n_posts,
    url,
    cts ,
    is_business_account BOOLEAN
);

CREATE TABLE IF NOT EXISTS posts (
    sid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    post_id VARCHAR(255) NOT NULL,
    location_id VARCHAR(255) NOT NULL,
    profile_id VARCHAR(255) NOT NULL,
    cts VARCHAR(255) NOT NULL,,
    post_type INT,
    description VARCHAR(255),
    number_likes INT,
    number_comments INT,
    photo_url VARCHAR(255),
    location_id FOREIGN KEY REFERENCES locations(id),
    profile_id FOREIGN KEY REFERENCES profiles(profiles_id)
);

CREATE TABLE IF NOT EXISTS locations (
    sid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    street VARCHAR(255),
    zip VARCHAR(255),
    city VARCHAR(255),
    region VARCHAR(255),
    cd VARCHAR(8),
    phone VARCHAR(255)
);


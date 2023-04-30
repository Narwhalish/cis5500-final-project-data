SHOW DATABASES;

CREATE DATABASE IF NOT EXISTS instagram;
    
USE instagram;

CREATE TABLE IF NOT EXISTS profiles (
    sid BIGINT NOT NULL AUTO_INCREMENT,
    profile_id BIGINT NOT NULL,
    profile_name VARCHAR(255),
    firstname_lastname VARCHAR(255),
    description VARCHAR(255),
    following INT NOT NULL,
    followers INT NOT NULL,
    n_posts INT NOT NULL,
    url VARCHAR(255),
    is_business_account BOOLEAN,
    PRIMARY KEY (sid)
);

DELETE FROM profiles
WHERE (sid, profile_id) NOT IN (
    SELECT * FROM (SELECT MIN(sid), profile_id
    FROM profiles
    GROUP BY profile_id) TEMP
);

ALTER TABLE profiles
DROP COLUMN sid;

ALTER TABLE profiles
ADD PRIMARY KEY (profile_id);

CREATE TABLE IF NOT EXISTS posts (
    sid BIGINT NOT NULL AUTO_INCREMENT,
    post_id VARCHAR(255) NOT NULL,
    profile_id BIGINT NOT NULL,
    location_id BIGINT NOT NULL,
    cts VARCHAR(255),
    post_type INT NOT NULL,
    description VARCHAR(255),
    number_likes INT NOT NULL,
    number_comments INT NOT NULL,
    PRIMARY KEY (sid)
#     FOREIGN KEY (profile_id) REFERENCES profiles(profile_id),
#     FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

DELETE FROM posts
WHERE (sid, post_id) NOT IN (
    SELECT * FROM (SELECT MIN(sid), post_id
    FROM posts
    GROUP BY post_id) TEMP
);

ALTER TABLE posts
DROP COLUMN sid;

ALTER TABLE posts
ADD PRIMARY KEY (post_id);

DELETE FROM posts
WHERE profile_id NOT IN (
    SELECT profile_id FROM profiles
);

DELETE FROM posts
WHERE location_id NOT IN (
    SELECT location_id FROM locations
);

ALTER TABLE posts
ADD FOREIGN KEY (profile_id) REFERENCES profiles(profile_id);

ALTER TABLE posts
ADD FOREIGN KEY (location_id) REFERENCES locations(location_id);

CREATE TABLE IF NOT EXISTS locations (
    sid BIGINT NOT NULL AUTO_INCREMENT,
    location_id BIGINT NOT NULL,
    name VARCHAR(255) NOT NULL,
    street VARCHAR(255),
    zip VARCHAR(255),
    city VARCHAR(255),
    region VARCHAR(255),
    cd VARCHAR(8),
    phone VARCHAR(255),
    blurb VARCHAR(255),
    lat FLOAT NOT NULL,
    lng FLOAT NOT NULL,
    primary_alias_on_fb VARCHAR(255),
    slug VARCHAR(255),
    website VARCHAR(255),
    PRIMARY KEY (sid)
);

DELETE FROM locations
WHERE (sid, location_id) NOT IN (
    SELECT * FROM (SELECT MIN(sid), location_id
    FROM locations
    GROUP BY location_id) TEMP
);

ALTER TABLE locations
DROP COLUMN sid;

ALTER TABLE locations
ADD PRIMARY KEY (location_id);

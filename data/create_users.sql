-- DROP is a command that wipes the whole table and it's content
DROP TABLE IF EXISTS users;

-- SQLite has a build in thing that is called 'data affinity', so we dont have to care about datatypes.
CREATE TABLE users(
    user_id                   TEXT,
    username                  TEXT UNIQUE,
    user_email                TEXT,
    user_password             TEXT,
    user_created_at           TEXT,
    user_firstname            TEXT,
    user_lastname             TEXT,
    user_verified             TEXT,
    user_total_followers      TEXT,
    user_total_following      TEXT,
    user_total_tweets         TEXT,
    user_profile_picture      TEXT,
    user_cover_picture        TEXT,
    PRIMARY KEY(user_id)
) WITHOUT ROWID;

INSERT INTO users VALUES(
"64c3b11f947248719fc0f7e97fb5cdb0",
"elonmusk",
"elonmusk@gmail.com",
"password",
"June 2009",
"Elon", 
"Musk", 
"1", 
"128900000", 
"177", 
"22700", 
"438b092d-344d-4628-a2de-afabcf5b0689.jpeg", 
"64786a33-47ed-463e-a198-157991fec3f8.jpeg"
  );

INSERT INTO users VALUES(
"24198c66ba294807a26e235e4bc96c2e", 
"shakira", 
"shakira@gmail.com", 
"password",
"April 2010",
"Shakira", 
"", 
"1", 
"53700000", 
"235", 
"7999", 
"a7b0c6fc-cd3b-4300-9fe4-3fef8171c62a.jpeg", 
"8581bbd0-f245-4816-9c7f-2f8c6cc4ac01.jpeg"
);

INSERT INTO users VALUES(
"dd41b0e3eeb94f3c9d4304ba44ff198c", 
"rihanna",
"rihanna@gmail.com", 
"password",
"August 2009", 
"Rihanna", 
"", 
"1", 
"107000000", 
"980", 
"10600", 
"49b99d9e-2e60-478d-8eb4-ba7358017319.jpeg", 
"84b6d13c-1a7a-4316-9401-3621ff0739fa.jpeg");

-- CREATE UNIQUE INDEX idx_users_username ON users(name);
-- CREATE INDEX idx_users_firstname ON users(firstname);
-- CREATE INDEX idx_users_lastname ON users(lastname);
-- CREATE INDEX idx_users_profile_picture ON users(profile_picture);

-- SELECT name FROM sqlite_master WHERE type = 'index';
-- SELECT name FROM sqlite_master WHERE type = 'trigger';
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
    user_is_verified          TEXT DEFAULT 0,
    user_total_followers      INTEGER DEFAULT 0,
    user_total_following      INTEGER DEFAULT 0,
    user_total_tweets         INTEGER DEFAULT 0,
    user_profile_picture      TEXT,
    user_cover_picture        TEXT,
    user_is_activated         TEXT DEFAULT 0,
    user_activation_key       TEXT,

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
"438b092d344d4628a2deafabcf5b0689.jpeg", 
"64786a3347ed463ea198157991fec3f8.jpeg",
"1",
"a0e189bdd20b437d920c1b60ec78ce22"
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
"a7b0c6fccd3b43009fe43fef8171c62a.jpeg", 
"8581bbd0f24548169c7f2f8c6cc4ac01.jpeg",
"1",
"4779ed2e36a54d8491e207999ab8a606"
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
"49b99d9e2e60478d8eb4ba7358017319.jpeg", 
"84b6d13c1a7a431694013621ff0739fa.jpeg",
"1",
"4fbc6eb58a4940d7a15418e01b2f04bd"
);


INSERT INTO users VALUES(
"ae0069977acc4a35ae2921e287951068", 
"barackobama",
"barack@gmail.com", 
"password",
"August 2009", 
"Barack", 
"Obama", 
"1", 
"132897676", 
"561038", 
"16800", 
"b3aed51663ad43079f44e05d8963d776.jpeg", 
"c514dea6b96b4a359ca1040184467d4e.jpeg",
"1",
"fedd8d68227a4b09be28582432a3e5a2"
);

INSERT INTO users VALUES(
"2f9214d6266e4a96a95bb6a5fb7d1a47", 
"tomineodegard",
"tomine@gmail.com", 
"password",
"Februrary 2023", 
"Tomine", 
"Ødegård", 
"0", 
"107000000", 
"980", 
"10600", 
"50f4de12dcd04b6db49a8831c520662a.jpg", 
"72712dce089e487f9c877ff0b39fd03e.jpg",
"1",
"988c0e1ce84e43ca97d4a60978c2628f"
);

-- CREATE UNIQUE INDEX idx_users_username ON users(username);
-- CREATE INDEX idx_users_firstname ON users(user_firstname);
-- CREATE INDEX idx_users_lastname ON users(user_lastname);
-- CREATE INDEX idx_users_profile_picture ON users(user_profile_picture);

-- SELECT username FROM sqlite_master WHERE type = 'index';
-- SELECT username FROM sqlite_master WHERE type = 'trigger';

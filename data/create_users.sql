-- DROP is a command that wipes the whole table and it's content
DROP TABLE IF EXISTS users;

-- SQLite has a build in thing that is called 'data affinity', so we dont have to care about datatypes.
CREATE TABLE users(
    user_id                   TEXT,
    username                  TEXT UNIQUE,
    user_email                TEXT,
    user_password             TEXT,
    user_created_at           INTEGER NOT NULL,
    user_firstname            TEXT,
    user_lastname             TEXT,
    user_bio                  TEXT,
    user_is_verified          TEXT DEFAULT 0,
    user_total_followers      INTEGER DEFAULT 0,
    user_total_following      INTEGER DEFAULT 0,
    user_total_tweets         INTEGER DEFAULT 0,
    user_profile_picture      TEXT,
    user_cover_picture        TEXT,
    user_is_activated         TEXT DEFAULT 0,
    user_activation_key       TEXT,
    user_reset_password_key   TEXT,

    PRIMARY KEY(user_id)
) WITHOUT ROWID;

INSERT INTO users VALUES(
"64c3b11f947248719fc0f7e97fb5cdb0",
"elonmusk",
"elonmusk@gmail.com",
"password",
"1244725452",
"Elon", 
"Musk", 
"Bio coming here",
"1", 
"128900000", 
"177", 
"22700", 
"438b092d344d4628a2deafabcf5b0689.jpeg", 
"64786a3347ed463ea198157991fec3f8.jpeg",
"1",
"a0e189bdd20b437d920c1b60ec78ce22",
"5f98d56a-164a-4a11-bb49-04ce0ece52bb"
);

INSERT INTO users VALUES(
"24198c66ba294807a26e235e4bc96c2e", 
"shakira", 
"shakira@gmail.com", 
"password",
"1270991052",
"Shakira", 
"",
"Bio coming here", 
"1", 
"53700000", 
"235", 
"7999", 
"a7b0c6fccd3b43009fe43fef8171c62a.jpeg", 
"8581bbd0f24548169c7f2f8c6cc4ac01.jpeg",
"1",
"4779ed2e36a54d8491e207999ab8a606",
"7328a36db66a425bacfaf7242807a927"
);

INSERT INTO users VALUES(
"dd41b0e3eeb94f3c9d4304ba44ff198c", 
"rihanna",
"rihanna@gmail.com", 
"password",
"1281531852", 
"Rihanna", 
"", 
"Rihanan bio coming here",
"1", 
"107000000", 
"980", 
"10600", 
"49b99d9e2e60478d8eb4ba7358017319.jpeg", 
"84b6d13c1a7a431694013621ff0739fa.jpeg",
"1",
"4fbc6eb58a4940d7a15418e01b2f04bd",
"01faad78d31541d385c7cedfc931d752"
);


INSERT INTO users VALUES(
"ae0069977acc4a35ae2921e287951068", 
"barackobama",
"barack@gmail.com", 
"password",
"1281531849", 
"Barack", 
"Obama", 
"Bio coming here",
"1", 
"132897676", 
"561038", 
"16800", 
"b3aed51663ad43079f44e05d8963d776.jpeg", 
"f60e3019f269420a8d5589222ffd4eff.jpeg",
"1",
"fedd8d68227a4b09be28582432a3e5a2",
"5199fa92067b4819bada61836512aac9"
);

INSERT INTO users VALUES(
"2f9214d6266e4a96a95bb6a5fb7d1a47", 
"tomineodegard",
"tomine@gmail.com", 
"password",
"1676120649", 
"Tomine", 
"Ødegård", 
"Bio coming here",
"0", 
"0", 
"0", 
"0", 
"50f4de12dcd04b6db49a8831c520662a.jpg", 
"72712dce089e487f9c877ff0b39fd03e.jpg",
"1",
"988c0e1ce84e43ca97d4a60978c2628f",
"4ada7bf8dcfa4aa0a481aee77854114e"
);

INSERT INTO users VALUES(
"5293c15d99904c6bbb512f8828216486", 
"beyonce",
"beyonce@gmail.com", 
"password",
"1239455049", 
"Beyoncé", 
"", 
"Bio coming here",
"0", 
"0", 
"0", 
"0", 
"95eb1075b6ec4804964e14094f8dae46.jpeg", 
"cef45e69e9f64069a6cec9f995fa5c88.jpeg",
"1",
"28255b871ac34bf5be087e62b800c0e9",
"d232dd14c2b64cb78d59c85177b4c9e7"
);


INSERT INTO users VALUES(
"999ac9342c79411c9a4800f2af792847", 
"billgates",
"beyonce@gmail.com", 
"password",
"1244725449", 
"Bill", 
"Gates", 
"Bio coming here",
"0", 
"500048", 
"536", 
"0", 
"720e20d964e844b39068767d25e79623.jpeg", 
"9832d0b2a1e94238b4e2993e46a7b069.jpeg",
"1",
"696a9430f4044501aab1d231267e5b9f",
"5cdd2418a523499db9d0bb4bbbde8c77"
);


INSERT INTO users VALUES(
"38ccc0414dcc4aecb72dfa207b947fa1", 
"kyliejenner",
"kylie@gmail.com", 
"password",
"1294751049", 
"Kylie", 
"Jenner", 
"Bio coming here",
"0", 
"4000048", 
"959", 
"14200", 
"a0fbf16e7daa41daa95e95d6f9b54cfb.jpeg", 
"724cee819e554d6999768e199bf9fd83.jpeg",
"1",
"696a9430f4044501aab1d231267e5b9f",
"6de1bc14404b42ee9462bb38c95d86e5"
);

INSERT INTO users VALUES(
"f415ccbd409f4547bf7e263f92e550af", 
"justinbieber",
"justin@gmail.com", 
"password",
"1294750929", 
"Justin", 
"Bieber", 
"Bio coming here",
"0", 
"14000048", 
"279000", 
"31200", 
"6b04b05663294572ab43c5982bdfc1f4.jpeg", 
"3a860033043d48da9bb76d68b5023886.jpeg",
"1",
"32201dd332d54e7ea6380e3da442a6e2",
"57a3248050e5457fb0d67c8affc46ef5"
);


INSERT INTO users VALUES(
"73efc6d9a14f42d4ba7e7f55393efa5c", 
"jeffbezoz",
"jeff@gmail.com", 
"password",
"1215781329", 
"Jeff", 
"Bezoz", 
"Bio coming here",
"0", 
"61000000", 
"220", 
"391", 
"06d072b8dc624d93bbc39802cd013ab8.jpeg", 
"fecbbd05a777412f8a5e13fd8846825d.jpeg",
"1",
"1c39de32d86e4f15b965d75748386e74",
"b613d25967214954ad043055d8033687"
);



-- CREATE UNIQUE INDEX idx_users_username ON users(username);
-- CREATE INDEX idx_users_firstname ON users(user_firstname);
-- CREATE INDEX idx_users_lastname ON users(user_lastname);
-- CREATE INDEX idx_users_profile_picture ON users(user_profile_picture);

-- SELECT username FROM sqlite_master WHERE type = 'index';
-- SELECT username FROM sqlite_master WHERE type = 'trigger';

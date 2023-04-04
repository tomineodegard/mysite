DROP TABLE IF EXISTS suggested_users;

CREATE TABLE suggested_users(
    suggested_users_id            TEXT,
    suggested_user_username       TEXT,
    suggested_user_firstname      TEXT,
    suggested_user_lastname       TEXT,
    suggested_user_picture        TEXT,
    PRIMARY KEY(suggested_users_id)
) WITHOUT ROWID;


INSERT INTO suggested_users VALUES("64c3b11f947248719fc0f7e97fb5cdb0", "elonmusk", "Elon", "Musk", "438b092d344d4628a2deafabcf5b0689.jpeg");
INSERT INTO suggested_users VALUES("24198c66ba294807a26e235e4bc96c2e", "shakira", "Shakira", "", "a7b0c6fccd3b43009fe43fef8171c62a.jpeg");
INSERT INTO suggested_users VALUES("dd41b0e3eeb94f3c9d4304ba44ff198c", "rihanna", "Rihanna", "", "49b99d9e2e60478d8eb4ba7358017319.jpeg");

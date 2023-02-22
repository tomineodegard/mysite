-- DROP is a command that wipes the whole table and it's content
DROP TABLE IF EXISTS users;

-- SQLite has a build in thing that is called 'data affinity', so we dont have to care about datatypes.
CREATE TABLE users(
    id               TEXT,
    joined_at        TEXT,
    username         TEXT,
    firstname        TEXT,
    lastname         TEXT,
    verified         TEXT,
    total_followers  TEXT,
    total_following  TEXT,
    total_tweets     TEXT,
    profile_picture  TEXT,
    cover_picture    TEXT,
    PRIMARY KEY(id)
) WITHOUT ROWID;

INSERT INTO users VALUES("64c3b11f947248719fc0f7e97fb5cdb0", "June 2009", "elonmusk", "Elon", "Musk", "1", "128900000", "177", "22700", "438b092d-344d-4628-a2de-afabcf5b0689.jpeg", "64786a33-47ed-463e-a198-157991fec3f8.jpeg");
INSERT INTO users VALUES("24198c66ba294807a26e235e4bc96c2e", "", "shakira", "Shakira", "", "0", "53700000", "235", "7999", "a7b0c6fc-cd3b-4300-9fe4-3fef8171c62a.jpeg", "8581bbd0-f245-4816-9c7f-2f8c6cc4ac01.jpeg");
INSERT INTO users VALUES("dd41b0e3eeb94f3c9d4304ba44ff198c", "", "rihanna", "Rihanna", "", "0", "107000000", "980", "10600", "49b99d9e-2e60-478d-8eb4-ba7358017319.jpeg", "84b6d13c-1a7a-4316-9401-3621ff0739fa.jpeg");
INSERT INTO users VALUES("23fb0cf9-7a4d-469d-ab96-e76ece452b70", "", "tomineodegard", "Tomine", "Ødegård","1", "199000000", "1980", "10000", "50f4de12-dcd0-4b6d-b49a-8831c520662a.jpg", "");
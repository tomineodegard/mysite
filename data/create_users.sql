-- DROP is a command that wipes the whole table and it's content
DROP TABLE IF EXISTS users;

-- SQLite has a build in thing that is called 'data affinity', so we dont have to care about datatypes.
CREATE TABLE users(
    id                TEXT,
    username          TEXT,
    first_name        TEXT,
    last_name         TEXT,
    total_followers   TEXT,
    total_following   TEXT,
    total_tweets      TEXT,
    avatar            TEXT,
    PRIMARY KEY(id)
) WITHOUT ROWID;

INSERT INTO users VALUES("64c3b11f947248719fc0f7e97fb5cdb0", "elonmusk", "Elon", "Musk", "128900000", "177", "22700", "438b092d-344d-4628-a2de-afabcf5b0689.jpeg");
INSERT INTO users VALUES("24198c66ba294807a26e235e4bc96c2e", "shakira", "Shakira", "Musk", "53700000", "235", "7999", "49b99d9e-2e60-478d-8eb4-ba7358017319.jpeg");
INSERT INTO users VALUES("dd41b0e3eeb94f3c9d4304ba44ff198c", "rihanna", "Rihanna", "", "107000000", "980", "10600", "a7b0c6fc-cd3b-4300-9fe4-3fef8171c62a.jpeg");
INSERT INTO users VALUES("dd41b0e3eeb94f3c9d4304ba44ff198c", "ladygaga", "Lady", "Gaga", "107000000", "980", "10600", "a7b0c6fc-cd3b-4300-9fe4-3fef8171c62a.jpeg");
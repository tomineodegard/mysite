DROP TABLE IF EXISTS tweets;

CREATE TABLE tweets(
    id               TEXT,
    user_fk          TEXT,
    created_at       TEXT,
    message          TEXT,
    image            TEXT,
    updated_at       TEXT,
    total_retweets   TEXT,
    total_likes      TEXT,
    total_views      TEXT,
    total_replies    TEXT,
    PRIMARY KEY(id)
) WITHOUT ROWID;
                           
INSERT INTO tweets VALUES(
    "fa27d61658e14f6f9f2a40a8e11b5bf0", 
    "64c3b11f947248719fc0f7e97fb5cdb0", 
    "1676283255", 
    "Hello world", 
    "438b092d-344d-4628-a2de-afabcf5b0689.jpeg", 
    "",
    "0",
    "0",
    "0", 
    "0"
);
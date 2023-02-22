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
    total_dislikes   TEXT,
    total_views      TEXT,
    total_replies    TEXT,
    PRIMARY KEY(id)
) WITHOUT ROWID;
                           
INSERT INTO tweets VALUES(
    "49c29377eda74912b854ffd818bf34cf", 
    "64c3b11f947248719fc0f7e97fb5cdb0", 
    "1676283255", 
    "ChatGPT to the mainstream media", 
    "tweet1.jpeg", 
    "",
    "",
    "0",
    "0",
    "0", 
    "0"
);
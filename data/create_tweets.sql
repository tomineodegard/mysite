DROP TABLE IF EXISTS tweets;

CREATE TABLE tweets(
    tweet_id         TEXT,
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
    PRIMARY KEY(tweet_id)
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

INSERT INTO tweets VALUES(
    "1506aeba-962b-45dd-ba0a-6719bf6accb1", 
    "24198c66ba294807a26e235e4bc96c2e", 
    "1676283255", 
    "Hello I am Shakira", 
    "tweet1.jpeg", 
    "",
    "",
    "0",
    "0",
    "0", 
    "0"
);
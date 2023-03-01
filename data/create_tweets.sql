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

-- rihanna tweet
INSERT INTO tweets VALUES(
    "add4498db796415484cc22890b707d91", 
    "dd41b0e3eeb94f3c9d4304ba44ff198c", 
    "1676283255", 
    "my son so fine! Idc idc idc! How crazy both of my babies were in these photos and mommy had no clue ❤️❤️ thank you so much @edward_enninful and @inezandvinoodh for celebrating us as a family!", 
    "8432451bc484471fac3788f2ac70ad26.jpeg", 
    "",
    "",
    "0",
    "0",
    "0", 
    "0"
);


-- elon tweet                    
INSERT INTO tweets VALUES(
    "49c29377eda74912b854ffd818bf34cf", 
    "64c3b11f947248719fc0f7e97fb5cdb0", 
    "1677679887", 
    "ChatGPT to the mainstream media", 
    "tweet1.jpeg", 
    "",
    "",
    "0",
    "0",
    "0", 
    "0"
);

-- shakira tweet
INSERT INTO tweets VALUES(
    "1506aeba962b45ddba0a6719bf6accb1", 
    "24198c66ba294807a26e235e4bc96c2e", 
    "1677679912", 
    "Hello I am Shakira", 
    "890b7ecfd33a48a38cfbba7e61137e43.jpeg", 
    "",
    "",
    "0",
    "0",
    "0", 
    "0"
);

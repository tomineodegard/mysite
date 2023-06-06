DROP TABLE IF EXISTS likes;
CREATE TABLE likes (
    user_fk        TEXT,
    tweet_fk       TEXT,
    created_at     TEXT,
    PRIMARY KEY(user_fk, tweet_fk)
) WITHOUT ROWID;
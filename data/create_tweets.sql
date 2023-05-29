-- PRAGMA foreign_keys;
-- PRAGMA foreign_keys = true;
-- PRAGMA foreign_keys;


DROP TABLE IF EXISTS tweets;

CREATE TABLE tweets(
    tweet_id               TEXT,
    tweet_user_fk          TEXT,
    tweet_created_at       TEXT,
    tweet_message          TEXT,
    tweet_image            TEXT,
    tweet_updated_at       TEXT,
    tweet_total_retweets   TEXT,
    tweet_total_likes      TEXT,
    tweet_total_views      TEXT,
    tweet_total_replies    TEXT,
    PRIMARY KEY(tweet_id),
    FOREIGN KEY(tweet_user_fk) REFERENCES users(user_id)
) WITHOUT ROWID;



-- Tweets Plus 
DROP TRIGGER IF EXISTS increment_user_total_tweets;
CREATE TRIGGER increment_user_total_tweets 
    AFTER INSERT ON tweets
BEGIN
    UPDATE users
    SET user_total_tweets = user_total_tweets + 1
    WHERE user_id = NEW.tweet_user_fk;
END;

-- Tweets Minus
DROP TRIGGER IF EXISTS decrement_user_total_tweets;
CREATE TRIGGER decrement_user_total_tweets 
    AFTER DELETE ON tweets
BEGIN
    UPDATE users
    SET user_total_tweets = user_total_tweets - 1
    WHERE user_id = NEW.tweet_user_fk;
END;
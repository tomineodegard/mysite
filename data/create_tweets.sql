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
    tweet_total_retweets   INTEGER DEFAULT 0,
    tweet_total_likes      INTEGER DEFAULT 0,
    tweet_total_views      INTEGER DEFAULT 0,
    tweet_total_replies    INTEGER DEFAULT 0,
    PRIMARY KEY(tweet_id),
    FOREIGN KEY(tweet_user_fk) REFERENCES users(user_id) ON DELETE CASCADE
) WITHOUT ROWID;



DROP TRIGGER IF EXISTS increment_user_total_tweets;
CREATE TRIGGER increment_user_total_tweets AFTER INSERT ON tweets
BEGIN 
UPDATE users
SET user_total_tweets = user_total_tweets + 1
WHERE user_id = NEW.tweet_user_fk;
END;

DROP TRIGGER IF EXISTS decrement_user_total_tweets;
CREATE TRIGGER decrement_user_total_tweets AFTER DELETE ON tweets
BEGIN UPDATE users
SET user_total_tweets = user_total_tweets - 1
WHERE user_id = OLD.tweet_user_fk;
END;


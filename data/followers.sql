DROP TABLE IF EXISTS followers;
CREATE TABLE followers (
    follower_fk      TEXT,
    followee_fk      TEXT,
    followed_at      TEXT,
    PRIMARY KEY(follower_fk, followee_fk)
) WITHOUT ROWID;


-- Followers Plus 
DROP TRIGGER IF EXISTS increment_user_total_followers;
CREATE TRIGGER increment_user_total_followers 
    AFTER INSERT ON followers
BEGIN
    UPDATE users
    SET user_total_followers = user_total_followers + "1"
    WHERE user_id = NEW.followee_fk;
END;

-- Followers Minus
DROP TRIGGER IF EXISTS decrement_user_total_followers;
CREATE TRIGGER decrement_user_total_followers 
    AFTER DELETE ON followers
BEGIN
    UPDATE users
    SET user_total_followers = user_total_followers - "1"
    WHERE user_id = OLD.followee_fk;
END;






-- Following Plus 
DROP TRIGGER IF EXISTS increment_user_total_following;
CREATE TRIGGER increment_user_total_following 
    AFTER INSERT ON followers
BEGIN
    UPDATE users
    SET user_total_following = user_total_following + 1
    WHERE user_id = NEW.follower_fk;
END;


-- Following Minus
DROP TRIGGER IF EXISTS decrement_user_total_following;
CREATE TRIGGER decrement_user_total_following 
    AFTER DELETE ON followers
BEGIN
    UPDATE users
    SET user_total_following = user_total_following - 1
    WHERE user_id = OLD.follower_fk;
END;



SELECT name FROM sqlite_master WHERE type = "trigger";


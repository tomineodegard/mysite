DROP TABLE IF EXISTS followers;


CREATE TABLE followers (
    follower_fk      TEXT,
    followee_fk      TEXT,
    followed_at      TEXT,
    PRIMARY KEY(follower_fk, followee_fk)
) WITHOUT ROWID;


-- DROP is a command that wipes the whole table and it's content
DROP TABLE IF EXISTS users;

-- SQLite has a build in thing that is called 'data affinity', so we dont have to care about datatypes.
CREATE TABLE users(
    user_id                   TEXT,
    username                  TEXT UNIQUE,
    user_email                TEXT,
    user_password             TEXT,
    user_created_at           INTEGER NOT NULL,
    user_firstname            TEXT NOT NULL,
    user_lastname             TEXT,
    user_bio                  TEXT,
    user_is_verified          INTEGER DEFAULT 0,
    user_total_followers      INTEGER DEFAULT 0,
    user_total_following      INTEGER DEFAULT 0,
    user_total_tweets         INTEGER DEFAULT 0,
    user_profile_picture      TEXT,
    user_cover_picture        TEXT,
    user_is_activated         INTEGER DEFAULT 0,
    user_is_active            INTEGER DEFAULT 1,
    user_activation_key       TEXT,
    user_reset_password_key   TEXT,
    user_deactivate_key       TEXT,

    PRIMARY KEY(user_id)
) WITHOUT ROWID;



CREATE UNIQUE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_firstname ON users(user_firstname);
CREATE INDEX idx_users_lastname ON users(user_lastname);

-- SELECT username FROM sqlite_master WHERE type = 'index';
-- SELECT username FROM sqlite_master WHERE type = 'trigger';

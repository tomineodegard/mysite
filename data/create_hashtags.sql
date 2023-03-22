DROP TABLE IF EXISTS hashtags;

CREATE TABLE hashtags(
    hashtag_id                       TEXT,
    hashtag_title                    TEXT,
    PRIMARY KEY(hashtag_id)
) WITHOUT ROWID;
                         
INSERT INTO hashtags VALUES(
    "e7a2b43c0d2042bfae69cbb7c4dd6410",
    "Hashtag-title"
);     

INSERT INTO hashtags VALUES(
    "b4090d09a39f4b8994e960f25e168845",
    "haaland"
);   
DROP TABLE IF EXISTS trends;

CREATE TABLE trends(
    trend_id                       TEXT,
    tweet_fk                       TEXT,
    location_fk                    TEXT,
    -- hashtag_fk                     TEXT,
    trend_title                    TEXT UNIQUE,
    trend_total_hashtags           TEXT,
    PRIMARY KEY(trend_id)
) WITHOUT ROWID;
                         
-- INSERT INTO trends VALUES(
--     "88292d096d3140dc9438bd24596e5010",
--     "add4498db796415484cc22890b707d91",
--     "43143be9e2584fc89b0ae71625de3da4",
--     "e7a2b43c0d2042bfae69cbb7c4dd6410",
--     "Unique trend title",
--     "26700"
-- );

INSERT INTO trends VALUES(
    "88292d096d3140dc9438bd24596e5010",
    "add4498db796415484cc22890b707d91",
    "43143be9e2584fc89b0ae71625de3da4",
    "Rød grød med fløde",
    "26"
);

-- INSERT INTO trends VALUES(
--     "8e4c35d038154d52ae4a88c9f4bf5de8",
--     "64c3b11f947248719fc0f7e97fb5cdb0",
--     "df1dac31878a4348b7e7e00f5a5a8278",
--     "b4090d09a39f4b8994e960f25e168845",
--     "Haaland",
--     "3"
-- );

INSERT INTO trends VALUES(
    "8e4c35d038154d52ae4a88c9f4bf5de8",
    "64c3b11f947248719fc0f7e97fb5cdb0",
    "df1dac31878a4348b7e7e00f5a5a8278",
    "Haaland",
    "12234"
);


DROP TABLE IF EXISTS trends;

CREATE TABLE trends(
    trend_id                       TEXT,
    tweet_fk                       TEXT,
    location_fk                    TEXT,
    trend_title                    TEXT UNIQUE,
    trend_total_hashtags           INTEGER,
    PRIMARY KEY(trend_id)
) WITHOUT ROWID;
                         

INSERT INTO trends VALUES(
    "f3bdbe58f22b4781b596a2bf0d89fc43",
    "89ffc88c611744518eab6a6dc7cf1bd8",
    "43143be9e2584fc89b0ae71625de3da4",
    "Store Bededag",
    2190
);


INSERT INTO trends VALUES(
    "88292d096d3140dc9438bd24596e5010",
    "add4498db796415484cc22890b707d91",
    "43143be9e2584fc89b0ae71625de3da4",
    "ChatGPT",
    89000
);

INSERT INTO trends VALUES(
    "8e4c35d038154d52ae4a88c9f4bf5de8",
    "64c3b11f947248719fc0f7e97fb5cdb0",
    "df1dac31878a4348b7e7e00f5a5a8278",
    "Haaland",
    12234
);

INSERT INTO trends VALUES(
    "6e4c35d038154d52ae4a88c9f4bf5de7",
    "64c3b11f947248719fc0f7e97fb5cdb0",
    "5b2ddf87748e466a99dcff4f77f67c2a",
    "Twitter algorithm",
    199999
);



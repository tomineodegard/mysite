DROP TABLE IF EXISTS trends;

CREATE TABLE trends(
    trend_id             TEXT,
    trending_location    TEXT,
    trending_content     TEXT,
    amount_of_tweets     TEXT,
    PRIMARY KEY(trend_id)
) WITHOUT ROWID;
                         
INSERT INTO trends VALUES(
    "6973522c-c93c-4192-92ee-5c0d1c4b1517",
    "Denmark", 
    "#China",
    "26700"
);                        
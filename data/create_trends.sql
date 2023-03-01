DROP TABLE IF EXISTS trends;

CREATE TABLE trends(
    trend_id             TEXT,
    trend_location       TEXT,
    title                TEXT,
    total_hash           TEXT,
    PRIMARY KEY(trend_id)
) WITHOUT ROWID;
                         
INSERT INTO trends VALUES(
    "88292d096d3140dc9438bd24596e5010",
    "Denmark", 
    "trend#1",
    "26700"
);

INSERT INTO trends VALUES(
    "ad52501650ed4c2d88827fac2084f678",
    "Denmark", 
    "trend#2",
    "26700"
);

INSERT INTO trends VALUES(
    "612f85e3ad424957a9a8d4c8fc40adf7",
    "Denmark", 
    "trend#3",
    "26700"
);                        
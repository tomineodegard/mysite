DROP TABLE IF EXISTS locations;

CREATE TABLE locations(
    location_id                       TEXT,
    location_title                    TEXT,
    PRIMARY KEY(location_id)
) WITHOUT ROWID;
                         
INSERT INTO locations VALUES(
    "43143be9e2584fc89b0ae71625de3da4",
    "Denmark"
);        

INSERT INTO locations VALUES(
    "df1dac31878a4348b7e7e00f5a5a8278",
    "Norway"
);

INSERT INTO locations VALUES(
    "0b2ddf87748e466a99dcff4f77f67c2a",
    "Spain"
);

INSERT INTO locations VALUES(
    "5b2ddf87748e466a99dcff4f77f67c2a",
    "the entire world"
);
  
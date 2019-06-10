CREATE TABLE potentialCrime (
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    title TEXT,
    keyword TEXT,
    crime_risk TEXT,
    cnt TEXT NOT NULL,
    news_title TEXT,
    news_link TEXT,
    other_suspect TEXT,
    suspect_probability TEXT
);

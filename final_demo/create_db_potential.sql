CREATE TABLE potentialCrime (
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    profile_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    age INTEGER,
    title TEXT,
    cnt TEXT NOT NULL,
    keyword TEXT
);

-- SQLite Database Schema

CREATE TABLE hdfc_top100_nav_clean (
    date TEXT,
    nav REAL
);

CREATE TABLE nifty50_clean (
    Date TEXT,
    Open REAL,
    High REAL,
    Low REAL,
    Close REAL,
    Volume INTEGER
);

CREATE TABLE sensex_clean (
    Date TEXT,
    Open REAL,
    High REAL,
    Low REAL,
    Close REAL,
    Volume INTEGER
);
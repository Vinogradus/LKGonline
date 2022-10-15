DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    user_name varchar (50) PRIMARY KEY NOT NULL,
    password TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    curCookie TEXT,
    curAuthMail TEXT
);

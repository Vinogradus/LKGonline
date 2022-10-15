DROP TABLE IF EXISTS history;

CREATE TABLE history (
    user_name varchar (50) NOT NULL,
    posledovatelnost TEXT NOT NULL,
    a INTEGER,
    c INTEGER,
    m INTEGER
    
    -- CONSTRAINT FK1_history FOREIGN KEY(user_name)
);
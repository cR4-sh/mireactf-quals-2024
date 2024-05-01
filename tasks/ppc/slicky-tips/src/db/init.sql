ALTER USER root with password 'root';

CREATE DATABASE slickytips;

\c slickytips;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    tips TEXT,
    main_tip TEXT
);

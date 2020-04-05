CREATE DATABASE rand_gen;
CREATE table rand_gen.rand_obj(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first VARCHAR(80) NOT NULL,
    last VARCHAR(80) NOT NULL,
    gender VARCHAR(80) NOT NULL,
    age VARCHAR(80) NOT NULL,
    img VARCHAR(100) NOT NULL,
    agility VARCHAR(80) NOT NULL,
    charisma VARCHAR(80) NOT NULL,
    rand_item VARCHAR(80) NOT NULL,
    endurance VARCHAR(80) NOT NULL,
    intelligence VARCHAR(80) NOT NULL,
    strength VARCHAR(80) NOT NULL,
    weapon VARCHAR(80) NOT NULL,
    start_point VARCHAR(80) NOT NULL,
    end_point VARCHAR(80) NOT NULL
);


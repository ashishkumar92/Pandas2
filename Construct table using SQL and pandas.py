import pandas as pd
import sqlite3
# create and connect to database
connector = sqlite3.connect('test_result.db')
# create cursor
my_cursor = connector.cursor()
# create tables
my_cursor.executescript("""
CREATE TABLE sweets_types
(
    id integer NOT NULL,
    name character varying NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE sweets
(
    id integer NOT NULL,
    sweets_types_id integer,
    name character varying NOT NULL,
    cost character varying NOT NULL,
    weight character varying NOT NULL,
    manufacturer_id integer NOT NULL,
    with_sugar boolean,
    requires_freezing boolean,
    production_date date NOT NULL,
    expiration_date date NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE manufacturers_storehouses
(
    id integer NOT NULL,
    storehouses_id integer NOT NULL,
    manufacturers_id integer NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE manufacturers
(
    id integer NOT NULL,
    name character varying NOT NULL,
    phone character varying,
    address character varying,
    city character varying NOT NULL,
    country character varying NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE storehouses
(
    id integer NOT NULL,
    name character varying NOT NULL,
    address character varying,
    city character varying NOT NULL,
    country character varying NOT NULL,
    PRIMARY KEY (id)
);
""")
# insert data
my_cursor.executescript("""
INSERT INTO sweets_types(name) VALUES
    ('waffles'),
    ('candy'),
    ('marmalade'),
    ('cookies'),
    ('chocolate');
INSERT INTO storehouses(name, address, city, country) VALUES
    ('MSK-1', '109235, Moscow, 4386 Projected proezd, 8', 'Moscow', 'Russia'),
    ('SPB-1 ', '197375, St. Petersburg, Suzdal highway, 26', 'Saint-petersburg', 'Russia'),
    ('EKB-1', '620137, Yekaterinburg, Shefskaya street, 1A ', 'Yekaterinburg', 'Russia'),
    ('EKB-2', '620137, Yekaterinburg, Shefskaya street, 2A', 'Yekaterinburg', 'Russia');
INSERT INTO manufacturers(name, phone, address, city, country) VALUES
    ('Mishan', '', '109235, Moscow, Proektiruemoy proezd, 15', 'Moscow', 'Russia'),
    ('Sobaken', '78125748899', '197375, St. Petersburg, Suzdal highway, 75', 'Saint-petersburg', 'Russia'),
    ('Martykha', '74657896525', '620137, Yekaterinburg, Shefskaya street, 5A', 'Yekaterinburg', 'Russia'),
    ('Mishan', '', '109235, Kazan, Projected street, 15', 'Kazan', 'Russia');
INSERT INTO manufacturers_storehouses(storehouses_id, manufacturers_id) VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (1, 2),
    (2, 1);
INSERT INTO sweets(
    sweets_types_id,
    name,
    cost,
    weight,
    manufacturer_id,
    with_sugar,
    requires_freezing,
    production_date,
    expiration_date
) VALUES
    (1, 'Milty', '100', '200',1, false, false, '2022-05-03 ', '2022-05-15'),
    (2, 'Mikus', '150', '300', 1 , true, true, '2022-04-03', '2022-05-03'),
    ( 3, 'Mivi', '110', '100', 1 , true, false, '2022-03-03', '2022-04-14'),
    (4, 'Mi', '120', '200 ', 1, false, true, '2022-03-04', '2022-04-04'),
    (5, 'Misa', '145', '570', 1, true, false, '2021-03 -03', '2022-12-03'),
    (1, 'Soltic', '115', '200', 2 , false, false, '2022-05-03', '2022-05-15'),
    (2, 'Soucus', '155', '300', 2 , true, true, '2022-03-03', '2022-05-03'),
    (3, 'Soviet', '117', '500', 2 , true, false, '2022-03-03', '2022-04-14'),
    (4, 'Co', '129', '250', 2, false, true, '2022 -03-04', '2022-04-04'),
    (5, 'Sor', '148', '500', 2, true, false, '2021-02-03', '2022-12-03 '),
    (1, 'Maltik', '210', '200', 3 , false, false, '2022-05-03', '2022-05-15'),
    (2, 'Macus', '350 ', '300', 3 , true, true, '2022-01-03', '2022-05-03');
""")
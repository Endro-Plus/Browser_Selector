DROP TABLE IF EXISTS browsers;
DROP TABLE IF EXISTS browser; --yeah, I'm pretty dumb sometimes
CREATE TABLE browsers (
    browser_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    browser_name varchar(25) UNIQUE,
    browser_icon varchar(500) UNIQUE,
    browser_exe varchar(500) UNIQUE,
    relative INTEGER NOT NULL

);

DROP TABLE IF EXISTS bpos;--browser positions (on the main GUI)
CREATE TABLE bpos(

    xpos INTEGER NOT NULL,
    ypos INTEGER NOT NULL,
    browser_ID INTEGER,
    FOREIGN KEY (browser_ID) REFERENCES browser(browser_ID)

);
--You are filled with BRAVERY
INSERT INTO browsers 
    VALUES (1, "Brave", "..\IMG\Brave.jpg", null, 1);

--Look, It's Da Dawg Guys!
INSERT INTO browsers 
    VALUES (2, "DuckDuckGo", "..\IMG\DDG.jpg", null, 1);

--Epic ga- I meant Epic privacy!
INSERT INTO browsers 
    VALUES (3, "Epic Privacy", "..\IMG\EPIC.jpg", null, 1);

--CAPTAIN FALKON!
INSERT INTO browsers 
    VALUES (4, "Falkon", "..\IMG\Falko.jpg", null, 1);

-- Fox's up-B
INSERT INTO browsers 
    VALUES (5, "Firefox", "..\IMG\Firefox.jpg", null, 1);

--Literal crap
INSERT INTO browsers 
    VALUES (6, "Edge", "..\IMG\Garbage.jpg", null, 1);

--Goggles
INSERT INTO browsers 
    VALUES (7, "Chome", "..\IMG\Gogle.jpg", null, 1);

--Chrome...ium
INSERT INTO browsers 
    VALUES (8, "Chromium", "..\IMG\Chromium.jpg", null, 1);

--Librefo- I meant Librewolf!
INSERT INTO browsers 
    VALUES (9, "Librewolf", "..\IMG\Librefox.jpg", null, 1);

--"Where she walks, seedlings awaken and reach out to the sun's warmth." -Hadori, the Promise of Spring
INSERT INTO browsers 
    VALUES (10, "Midori", "..\IMG\Midori.jpg", null, 1);

--The Opera
INSERT INTO browsers 
    VALUES (11, "Opera", "..\IMG\Opera.jpg", null, 1);

--The Opera, GTX on
INSERT INTO browsers 
    VALUES (12, "OperaGX", "..\IMG\OperaGX.jpg", null, 1);

--Torarria
INSERT INTO browsers 
    VALUES (13, "Tor Browser", "..\IMG\Tor_logo.jpg", null, 1);

--Vivivivivivivivivivalaldi
INSERT INTO browsers 
    VALUES (14, "Vivaldi", "..\IMG\Vivsomething.jpg", null, 1);

--H2OFox
INSERT INTO browsers 
    VALUES (15, "Waterfox", "..\IMG\Waterfox.jpg", null, 1);








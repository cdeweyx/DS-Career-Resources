
-- Link: https://en.wikibooks.org/wiki/SQL_Exercises/Pieces_and_providers

-- 5.1 Select the name of all the pieces. 
SELECT name
FROM pieces;


-- 5.2  Select all the providers' data. 
SELECT *
FROM providers;


-- 5.3 Obtain the average price of each piece (show only the piece code and the average price).
SELECT piece, AVG(price)
FROM provides
GROUP BY piece;


-- 5.4  Obtain the names of all providers who supply piece 1.
SELECT b.name
FROM provides a JOIN providers b
ON a.provider = b.code
WHERE a.piece = 1;


-- 5.5 Select the name of pieces provided by provider with code "HAL".
SELECT b.name
FROM provides a JOIN pieces b
ON a.piece = b.code
WHERE a.provider = 'HAL';


-- 5.6 For each piece, find the most expensive offering of that piece and include the piece name, provider name, and price 
-- (note that there could be two providers who supply the same piece at the most expensive price).
SELECT b.name, c.name, a.price
FROM provides a JOIN pieces b
ON a.piece = b.code JOIN providers c
ON a.provider = c.code
WHERE a.price = (SELECT MAX(price)
				 FROM provides
				 WHERE piece = b.code);


-- 5.7 Add an entry to the database to indicate that "Skellington Supplies" (code "TNBC") will provide sprockets (code "1") for 7 cents each.


-- 5.8 Increase all prices by one cent.


-- 5.9 Update the database to reflect that "Susan Calvin Corp." (code "RBT") will not supply bolts (code 4).


-- 5.10 Update the database to reflect that "Susan Calvin Corp." (code "RBT") will not supply any pieces 
-- (the provider should still remain in the database).
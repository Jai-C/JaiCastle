SELECT AVG(City.Population) AS AVG_POPULATION
FROM City INNER JOIN Country ON City.CountryCode = Country.Code
WHERE Country.Name = "Germany"
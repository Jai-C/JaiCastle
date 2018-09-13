SELECT Count(*) AS Number_Of_Cities
FROM City INNER JOIN Country ON City.CountryCode = Country.Code
WHERE Country.Name = "China" AND City.Population > 1000000
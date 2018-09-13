SELECT Sum(City.Population) AS Sum_Of_City_Populations
FROM City INNER JOIN Country ON City.CountryCode = Country.Code
WHERE Country.Name = "China" AND City.Population > 1000000
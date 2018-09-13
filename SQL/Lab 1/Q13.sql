SELECT stddev(City.Population) AS STD_DEV
FROM City INNER JOIN Country ON City.CountryCode = Country.Code
WHERE Country.Name = "Germany"
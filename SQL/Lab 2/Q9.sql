SELECT COUNT(City.ID) AS Number_Of_French_Speaking_Cities
FROM (City INNER JOIN Country ON City.CountryCode = Country.Code) INNER JOIN CountryLanguage ON Country.Code = CountryLanguage.CountryCode
WHERE CountryLanguage.Language = "French" AND CountryLanguage.IsOfficial = TRUE AND NOT(Country.Region = "Western Europe")
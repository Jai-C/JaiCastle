SELECT Country.Name, CountryLanguage.Language
FROM Country INNER JOIN CountryLanguage ON Country.Code = CountryLanguage.CountryCode
WHERE IsOfficial = TRUE
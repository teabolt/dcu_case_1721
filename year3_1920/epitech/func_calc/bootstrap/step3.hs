myBaro :: String -> Int -> String
myBaro "Spring" hPa 
    | 1060 <= hPa = "Sunny or fair weather."
    | (1006 <= hPa) && (hPa <= 1020) = "Showers or hail showers."
    | hPa < 1006 = "Rain and wind."
myBaro "Summer" hPa
    | 1020 <= hPa = "Sunny or fair weather."
    | (1013 <= hPa) && (hPa <= 1020) = "Fair or possible showers."
    | (1006 <= hPa) && (hPa <= 1013) = "Showers or hail showers."
    | hPa < 1006 = "Rain and wind."
-- myBaro "Autumn" hPa
--     | 1020 hPa or more = "Sunny or fair weather."
--     | from 1013 to 1020 hPa = "Local showers."
--     | from 1006 to 1013 hPa = "Showers, fresh weather."
--     | less than 1006 hPa = "Showers, chilly weather.""
-- myBaro "Winter" hPa
--     | 1020 hPa or more = "Fair and foggy."
--     | from 1013 to 1020 hPa = "Fair weather."
--     | from 1006 to 1013 hPa = "Snow or hail showers."
--     | less than 1006 hPa = Snow, cold weather."
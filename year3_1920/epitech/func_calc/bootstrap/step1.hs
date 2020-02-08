-- number less 3
prev3 :: Int -> Int
prev3 x = x - 3


-- min of 3 numbers
min3 :: Int -> Int -> Int -> Int
min3 a b c = min a (min b c)


-- check if number is negative
isneg :: Int -> Bool
isneg x = x < 0
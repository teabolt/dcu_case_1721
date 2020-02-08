import Text.Printf

-- recursive factorial
myFact :: Int -> Int
myFact 0 = 1
myFact n | n < 0 = 0
         | 0 < n = n * myFact (n-1)


-- square root of a number
mySqrt :: Float -> Float
mySqrt n = mySqrtFormat (mySqrtCalc n)

mySqrtCalc :: Float -> Float
mySqrtCalc 1 = 1
mySqrtCalc n | n < 0 = 0
             | True = n * n
            --  TODO

mySqrtFormat :: Float -> Float
mySqrtFormat x = read (printf "%.3f" x :: String) :: Float
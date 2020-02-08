import Data.List

-- sum of even numbers in a list
-- implementation filters odd numbers with a list comprehension
-- and uses a built-in sum function
-- can also use Data.List.filter
mySumEven :: [Int] -> Int
mySumEven lst = sum [x | x <- lst, x `mod` 2 == 0]


-- check if a list is palindrome
myPal :: [Int] -> Bool
-- base case even
myPal [] = True
-- base case odd
myPal [x] = True
-- recursive case
myPal lst =
    -- check endpoints
    if head lst == last lst
        then
            -- chop off endpoints and continue checking
            myPal (init (tail lst))
        else
            -- endpoints do not match
            False


-- average of a list
-- implement with a sum and division by length (integer division)
myAverage :: [Int] -> Int
-- exceptional case
myAverage [] = 0
-- regular case
-- note that the order of function definitions matters
myAverage lst = sum lst `div` length lst


-- sort a list
-- myDicho :: [Int] -> [Int]


-- all tuples (m, n) such that m+n == k
-- implemented by sorting the list
-- then reducing the endpoints step by step
my2Sum :: [Int] -> Int -> (Int, Int)
-- base cases - not enough elements
my2Sum [] k = (-1, -1)
-- we assume that elements can not be repeated in the calculation
my2Sum [a] k = (-1, -1)
-- recursive case
my2Sum lst k
    | head lstS + last lstS == k = (head lstS, last lstS)
    | head lstS + last lstS < k = my2Sum (tail lstS) k
    | head lstS + last lstS > k = my2Sum (init lstS) k
    where
        lstS = sort lst
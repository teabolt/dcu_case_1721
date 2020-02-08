module Lib
    ( evalExpr
    ) where


import Data.List
import Data.Maybe


evalExpr :: String -> Maybe Float
evalExpr input = simpleParser input



-- See docs/arithmetic.peg for a description of the PEG being used

-- TODO:
-- pegParser :: String -> Float
-- pegParser input = 0.0



-- A simple parser not as powerful as a PEG parser
-- supports the following expressions:
-- a+b, a-b, a*b, a/b, a^b
-- where a and b are floats in the form x.y
-- and there may be arbitrary whitespace between an operator and its literals


-- we place - last because it may be used as a unary operator
operators = "*/^+-"


simpleParser :: String -> Maybe Float
simpleParser str =
    -- FIXME: might have multiple unary - operators, in which case the parsing fails
    let opIdx = firstMatching operators str in
    if isJust (opIdx)
        then 
            let idx = fromJust (opIdx)
                op = str !! idx
                a = extractLiteral 0 (idx-1) str 
                b = extractLiteral (idx+1) (length str) str in
            Just (applyOp op a b)
    else
        Nothing


-- a function that is like findIndex with equality, but accepts multiple characters for the predicate
firstMatching :: String -> String -> Maybe Int
firstMatching "" str = Nothing
firstMatching ops str = 
    let curr = head ops
        idx = findIndex (==curr) str in
    if isJust (idx)
        then idx
    else
        let rest = tail ops in
        firstMatching rest str


-- https://stackoverflow.com/questions/4597820/does-haskell-have-list-slices-i-e-python
slice :: Int -> Int -> [a] -> [a]
slice from to xs = take (to - from + 1) (drop from xs)


-- extract the float number in a string between two ranges
extractLiteral :: Int -> Int -> String -> Float
extractLiteral start stop str =
    let chars = slice start stop str in
    read chars :: Float


-- apply given operator from a character, to the two given floats
applyOp :: Char -> Float -> Float -> Float
applyOp '+' a b = a + b
applyOp '-' a b = a - b
applyOp '*' a b = a * b
applyOp '/' a b = a / b
applyOp '^' a b = a**b

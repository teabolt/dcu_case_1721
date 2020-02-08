-- search an element in a list
-- implement without Data.List elem
-- a is constrained to implement equality
-- we have two arguments here ** (separated by ->)
myFind :: Eq a => a -> [a] -> Maybe a
-- base case - empty
myFind a [] = Nothing
-- recursive case
-- implement by stepping through the list one by one by chopping off head
myFind a lst 
    | x == a = Just x
    | x /= a = myFind a (tail lst)
    where
        x = head lst
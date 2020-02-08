module Main where

import System.Environment
import System.Exit
import Text.Printf
import Data.Maybe
import Lib


errorExit :: String -> IO ()
errorExit msg = do
    putStrLn msg
    exitWith $ ExitFailure 84


main :: IO ()
main = do
    args <- getArgs
    let argc = length args
    if argc == 0
        then errorExit "Arguments missing."
    else if argc /= 1
        then errorExit "Too many arguments (Must have one argument only)."
    else
        let str = head args
            res = evalExpr str in
        if isJust res
            then printf "%.2f\n" $ fromJust (res)
        else
            errorExit "Could not parse expression."

        -- FIXME: catch read exceptions and raise own exceptions 
        -- let str = head args
        -- res <- try (evalExpr str) :: IO (Either SomeException ())
        --     case res of
        --         Left e -> do
        --             errorExit "Error parsing expression."
        --         Right n -> do
        --             if isJust res
        --                 then printf "%.2f\n" $ fromJust (res)
        --             else
        --                 errorExit "Could not parse expression."

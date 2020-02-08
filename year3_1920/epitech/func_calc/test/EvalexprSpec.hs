module EvalexprSpec where


import Test.Hspec
import Lib


spec :: IO ()
spec = hspec $ do
    describe "evalExpr" $ do
        it "adds two positive integers" $
            evalExpr "2+3" `shouldBe` Just 5

        it "subtracts two positive integers" $
            evalExpr "3-1" `shouldBe` Just 2

        it "multiplies two positive integers" $
            evalExpr "2*2" `shouldBe` Just 4

        it "divides two positive integers" $
            evalExpr "4/2" `shouldBe` Just 2

        it "raises a positive integer to another positive integer" $
            evalExpr "2^2" `shouldBe` Just 4

        it "handles floats" $
            evalExpr "2.5+2.6" `shouldBe` Just 5.1

        it "handles negative numbers" $
            evalExpr "-2.5*-1" `shouldBe` Just 2.5

        it "handles extra whitespace" $
            evalExpr "-2    + 4" `shouldBe` Just 2
            
        it "handles unary - operator" $
            evalExpr "-2-2" `shouldBe` Just 4

        it "handles unary + operator" $
            evalExpr "+2-3" `shouldBe` Just (-1)

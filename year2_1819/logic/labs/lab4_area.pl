/* Infix (a+b) binary operator tA
true if triangle represented by the left operand
has the area that is the number in the right operand.
The triangle is A/B, with base A and height B.
The area formula is (A*B)/2 */

tA(A/B, X) :- X is (A*B)/2.
:- op(1200, yfx, tA).

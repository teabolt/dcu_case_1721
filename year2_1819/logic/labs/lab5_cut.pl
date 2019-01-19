/* Find the class of a number (zero, positive, or negative) */

class(X, positive) :- X > 0, !.
class(X, negative) :- X < 0, !.
class(X, zero) :- X =:= 0, !.

/* Split the list Numbers into two lists, Positive (positive/zero numbers) and Negative (negative numbers)*/
split([], [], []) :- !. /* base case */
/* check if head of positive is head of numbers */
split([X|NumsTail], [X|PosTail], Neg) :- X >= 0, split(NumsTail, PosTail, Neg).
/* check if head of negative is head of numbers */
split([X|NumsTail], Pos, [X|NegTail]) :- X < 0, split(NumsTail, Pos, NegTail).

/* Calculate the fibonacci number Y of term X */
fib(0, 1) :- !.
fib(1, 1) :- !.
fib(X, Y) :- X1 is X-1, X2 is X-2, fib(X1, Y1), fib(X2, Y2), Y is Y1+Y2, !.
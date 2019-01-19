/* Predicate fib(X, Y) returns true if Y is the fibonacci number of X
The base cases are assumed to be 1 and 1 for 0 and 1 respectively.
The relation defines that a fibonacci number is the sum of the previous two fibonacii numbers*/


/* base cases */
fib(0, 1).
fib(1, 1).
/* recursive case, F is fibonacci argument, N is the integer */
fib(F, N) :- F1 is F-1, F2 is F-2,
    fib(F1, N1), fib(F2, N2),
    N is N1+N2.

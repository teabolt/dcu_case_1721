% Check if a number is prime

% Evaluate to true if number is prime, false otherwise
% Start the recursion
prime(N) :- Upperbound is N - 1, check_divs(N, Upperbound).

% Recurse on number and the current divisor being tested (go downwards)
% reached 1, the number is prime
check_divs(_, 1).
% check and descend
check_divs(N, D) :- nondiv(N, D), NextD is D - 1, check_divs(N, NextD).

% Evaluate to true if D does *not* evenly divide N
nondiv(N, D) :- N mod D =\= 0.

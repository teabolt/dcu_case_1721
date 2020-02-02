% Return true if X is a term

book(logic, davids).

term(X) :- var(X) ; nonvar(X).

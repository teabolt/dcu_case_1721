/* FACTS */

parents(david, george, noreen).
parents(jennifer, george, noreen).
parents(georgejr, george, noreen).
parents(scott, george, noreen).
parents(joanne, george, noreen).
parents(jessica, david, edel).
parents(clara, david, edel).
parents(michael, david, edel).
parents(laura, georgejr, susan).
parents(anna, scott, siobhan).

/* more facts for generality test */
parents(edel, mick, peggy).
parents(maria, mick, peggy).
parents(assumpta, mick, peggy).
parents(patrick, kevin, maria).
parents(hugh, kevin, maria).
parents(helena, kevin, maria).
parents(roisin, wim, assumpta).

/* RELATIONSHIPS */

father(X, Y) :- parents(Y, X, _).
male(X) :- father(X, _).

mother(X, Y) :- parents(Y, _, X).
female(X) :- mother(X, _).
/* fix: add gender as a fact (just for the sisters now) */
female(jennifer).
female(joanne).

grandfather(X, Y) :- father(X, Z), father(Z, Y).
grandfather(X, Y) :- father(X, Z), mother(Z, Y).

grandmother(X, Y) :- mother(X, Z), mother(Z, Y).
grandmother(X, Y) :- mother(X, Z), father(Z, Y).

/* brother(X, Y) :- male(X), father(Z, X), father(Z, Y). */
/* fix: relation non-reflexive */
brother(X, Y) :- X \== Y, male(X), father(Z, X), father(Z, Y).
sister(X, Y) :- X \== Y, female(X), father(Z, X), father(Z, Y).


/* Extra relationships */

uncle(X, Y) :- father(Z, Y), brother(X, Z).
aunt(X, Y) :- father(Z, Y), sister(X, Z).
siblings(X, Y) :- parents(X, M, F), parents(Y, M, F).
cousin(X, Y) :- father(Z, X), father(W, Y), Z \== W, siblings(Z, W).

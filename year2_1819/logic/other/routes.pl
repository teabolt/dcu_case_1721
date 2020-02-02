bus('17a').

% in(X, A)
in(X, [X|_]) :- !.
in(X, [_|Tail]) :- in(X, Tail).

notin(_,[]).
notin(X, [Y|Tail]) :- X =\= Y, notin(X, Tail).

% union(A, B, C). C = A|B (no repeats)
union([], [], []).
union([AH|ATail], B, [AH|CTail]) :- notin(AH, CTail), union(ATail, B, CTail).
union([], [BH|BTail], [BH|CTail]) :- notin(BH, CTail), union([], BTail, CTail).

intersection([], [], []).

route(charlestown, mystreet, time(10, 30), time(11, 00)).
route(mystreet, oconnell, time(11, 00), (11, 30)).
route(mystreet, finglas, time(12, 00), time(12, 10)).
route(finglas, dcu, time(12, 10), time(12, 19)).

timediff(time(H1, M1), time(H2, M2), D) :- HD is H2 - H1, MD is M2 - M1, D is 60*HD + MD.

journey(Start, End) :- route(Start, End, _, _). /* direct route */
journey(Start, End) :-
    route(Start, Mediate, _, _),
    route(Mediate, End, ArrivalTime, DepartureTime), timediff(ArrivalTime, DepartureTime, Diff), 10 =< Diff.

valid(X) :- number(X), Rem is X mod 2, Rem =\= 0.
oddsquaresum([X], XSquare) :- valid(X), XSquare is X**2.
oddsquaresum([H|XTail], NewS) :-
    valid(H),
    HSquare is H**2,
    oddsquaresum(XTail, OldS), NewS is HSquare + OldS.

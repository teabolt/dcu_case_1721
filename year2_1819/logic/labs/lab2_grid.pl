/* Represent a grid of points */

/* North-South-East-West grid*/

/* list comprehension attempt? */
/* North = [[p, k], [q, l], [r, m], [s, n], [t, o], 
        [k, f], [l, g], [m, h], [n, i], [o, j], 
        [f, a], [g, b], [h, c], [i, d], [j, e]].

East = [[p, q], [q, r], [r, s], [s, t], 
       [k, l], [l, m], [m, n], [n, o], 
       [f, g], [g, h], [h, i], [i, j], 
       [a, b], [b, c], [c, d], [d, e]].
*/

% Represent the grid as a matrix (lists within a list)
grid(L) :-
    L = [
        [a, b, c, d, e], % first row
        [f, g, h, i, j], % second row
        [k, l, m, n, o], % third row
        [p, q, r, s, t]  % fourth row
    ].

% Alternative representation
% first row
point(a, 0, 0).
point(b, 1, 0).
point(c, 2, 0).
point(d, 3, 0).
point(e, 4, 0).

% second row
point(f, 0, 1).
point(g, 1, 1).
point(h, 2, 1).
point(i, 3, 1).
point(j, 4, 1).

% third row
point(k, 0, 2).
point(l, 1, 2).
point(m, 2, 2).
point(n, 3, 2).
point(o, 4, 2).

% fourth row
point(p, 0, 3).
point(q, 1, 3).
point(r, 2, 3).
point(s, 3, 3).
point(t, 4, 3).

% Rules: dueDir(P, Q).
% Use the point representation
%
cmp(point(P, X1, Y1), point(Q, X2, Y2)).

% 'Atomic' rules

dueNorth(P, Q) :- point(P, X1, Y1), point(Q, X2, Y2), X1 =:= X2, Diff is Y1-Y2,
    Diff =:= 1.

% steps:
% instantiate coordinates
% check x axis
% check y axis (get point difference, verify difference)

dueEast(P, Q) :- point(P, X1, Y1), point(Q, X2, Y2), Y1 =:= Y2, Diff is X1-X2,
    Diff =:= -1.

% 'Derived' rules

dueSouth(P, Q) :- dueNorth(Q, P).
dueWest(P, Q) :- dueEast(Q, P).
dueNorthEast(P, Q) :- dueNorth(P, Z), dueEast(P, W), dueEast(Z, Q), dueNorth(W, Q).
dueSouthEast(P, Q) :- .

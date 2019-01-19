/* An element (term) X is a member of a list structure A */
myElem(X, [X|_]).
myElem(X, [_|Tail]) :-  myElem(X, Tail).

/* An element X is at the head (first) of a list A */
myHead(X, [X|_]).

/* An element X is the tail (last) element of a list A*/
/* myLast(X, [X]). */ /* base case v1 - singleton*/
myLast(X, [X|[]]). /* base case v2 tail is empty */
/* myLast(X, [_, X]). */ /* base case v3, 2nd elem of 2 */
myLast(X, [_|Tail]) :- myLast(X, Tail). /* reduce the list */

/* A list A is the tail of list B (sublist at the end). */
myTail(A, A). /* same lists */
/* myTail(A, [_|A]). */ /* A matches the tail of A - doesn't work - one less the simplest case*/
myTail(A, [_|Tail]) :- myTail(A, Tail). /* reduce to tail */

/* A list A is appended with a list B at its end, resulting in list C : A+B=C*/
myAppend([], B, B).
myAppend([Head|Tail1], B, [Head|Tail2]) :- myAppend(Tail1, B, Tail2).
/* other attempts:
myAppend([], [], []).
myAppend([Head|[]], Tail, [Head|Tail]).
myAppend([_|Tail], X, Y) :- myAppend([Tail], X, Y).
myAppend([], [], []).
myAppend([X], [Y], [X, Y]).
myAppend([X1, X2], [Y1], [X1, X2, Y1]). */

myDelete(X, [X|Tail], Tail).
myDelete(X, [Head|Tail1], [Head|Tail2]) :- myDelete(X, Tail1, Tail2).
/* other attempt
myDelete(X,[X|Tail],Tail).
myDelete(X,[Head|Tail],B) :- myDelete(X,Tail,B).
*/

/* myReverse([Head|Tail], .(Tail, Head)). */
/* broken attempts
myReverse([], []).
myReverse([X], [X]).
myReverse([X, Y], [Y, X]).
myReverse([Head1|Tail1], [Head2|Tail2]) :- myReverse([Tail1], [Head1]), myReverse([Tail2], [Head2]).
myReverse([X|Y], [[Y|_]|[X]]).
*/

/* Hint: Use previously defined predicates */
myReverse([], []). /* base case */
myReverse([S|ATail], B) :- myLast(S, B), myAppend(BHead, [S], B), myReverse(ATail, BHead).
/* take two lists, check if the front and the end of both match (Same), 'reverse' the rest of the lists appropriately */
/* this fails to terminate when looking for more things (press ;)when one of the lists is not supplied */

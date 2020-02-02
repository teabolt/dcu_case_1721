% Playing around with own defined operators

% Notation: prefix *(a, b), infix (a*b), postfix a b *
% Internally prefix is used (operator as functor), but infix and postfix
% be external representations


% Binary operator modulo, returns remainder after division
% blueprint: /%(dividend, divisor, remainder)

/*
modulo(A/B, Remainder) :- Multiple is A // B,
    Quotient is Multiple * B,
    Remainder is A - Quotient.
:- op(450, xf, modulo).
*/

/*
% Unary operator 'transform'
t(X) :- X + 2 * 3.
*/

% Previous:
tA(Base/Height, Area) :- Area is (Base*Height) / 2.
:- op(500, yfx, tA).
% yfx - left to right

neg(X, N) :- N is -X.
:- op(500, xfy, neg).

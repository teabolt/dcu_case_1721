% Binary Search Trees implementation in SWI Prolog.
% CA208, Assignment 2, 2018
% Student ID: 17350793. Name: Tomas Baltrunas. Programme: CASE2.



% BST Definition

% Express binary trees as follows:
% emptyBT. - an empty binary tree
% bTree(N, T1, T2). - a binary tree with item N (number),
% left subtree T1, right subtree T2.



% insert(I, T1, T2).
% base case: insert into an empty tree
insert(I, emptyBT, bTree(I, emptyBT, emptyBT)) :- !.

% recursive case: pick a branch, insert into it, restore other branch
% pick left branch
insert(I, bTree(Root, LeftOld, RightOld), bTree(Root, LeftNew, RightOld)) :-
    I =< Root, insert(I, LeftOld, LeftNew).

% pick right branch
insert(I, bTree(Root, LeftOld, RightOld), bTree(Root, LeftOld, RightNew)) :-
    Root < I, insert(I, RightOld, RightNew).



% my_concat(A, B, C): A+B = C, concatinates two lists together
my_concat([], [], []).
my_concat([], [BHead|BTail], [BHead|CTail]) :- my_concat([], BTail, CTail).
my_concat([AHead|ATail], B, [AHead|CTail]) :- my_concat(ATail, B, CTail).
% Don't use the name 'concat',
% else get a 'No permission to redefine imported_procedure' error.
% Could use some builtin predicate instead of this:
% 'append' does the same thing.


% preorder(T, L).
% empty tree produces no nodes
preorder(emptyBT, []) :- !.
% NLR traversal is [N] + L + R
preorder(bTree(Root, Left, Right), [Root|TLeftRight]) :-
    preorder(Left, TLeft),
    preorder(Right, TRight),
    my_concat(TLeft, TRight, TLeftRight), !.

% inorder(T, L).
inorder(emptyBT, []) :- !.
% LNR traversal is L + [N] + R
inorder(bTree(Root, Left, Right), L) :-
    inorder(Left, TLeft), inorder(Right, TRight),
    my_concat(TLeft, [Root], TLeftRoot), my_concat(TLeftRoot, TRight, L), !.

% postorder(T, L).
postorder(emptyBT, []) :- !.
% LRN traversal is L + R + [N]
postorder(bTree(Root, Left, Right), L) :-
    postorder(Left, TLeft), postorder(Right, TRight),
    my_concat(TLeft, TRight, TLeftRight), my_concat(TLeftRight, [Root], L), !.



% search(T, I).
% Empty tree has no nodes. Sentinel for the recursion
search(emptyBT, _) :- fail.
% Item is at root
search(bTree(Root, _, _), Root) :- !.
% Search an appropriate branch
search(bTree(Root, Left, _), I) :- I =< Root, search(Left, I), !.
search(bTree(Root, _, Right), I) :- Root < I, search(Right, I), !.



% height(T, H).
% Empty tree has no height
height(emptyBT, 0) :- !.
% The subtree on the left is taller
height(bTree(_, Left, Right), H) :- height(Left, HLeft),
    height(Right, HRight), HRight =< HLeft, H is HLeft + 1, !.
% The subtree on the right is taller
height(bTree(_, Left, Right), H) :- height(Left, HLeft),
    height(Right, HRight), HLeft < HRight, H is HRight + 1, !.
% To avoid repetition in the two recursive rules, could also use a
% max/min predicate to pick the taller subtree.



% Required predicates done



%
% Helper Predicates
%



% bt(T) - T is a binary tree.
% Empty Binary Tree
bt(emptyBT) :- !.
% Integer/float at the root, and binary trees at branches
bt(bTree(N, T1, T2)) :- number(N), bt(T1), bt(T2), !.

% bst(T) - T is a binary search tree.
% Empty BT is a BST vacuously.
bst(emptyBT) :- !.
% Recurse on subtrees. Get their nodes. Check if match against root
bst(bTree(N, Left, Right)) :-
    bst(Left), bst(Right),
    preorder(Left, NodesLeft), preorder(Right, NodesRight),
    all_left(N, NodesLeft), all_right(N, NodesRight), !.
% Not the most optimal solution:
% recursive bst call and preorder in a way repeat each other.
% Could somehow 'cache' the nodes already visited.

% Support predicates.
% all_left(N, L) - all items in L are less/equal to N.
all_left(_, []).
all_left(Root, [Current|Remaining]) :-
    Current =< Root,
    all_left(Root, Remaining).

% all_right(N, L) - all items in L are greater than N.
all_right(_, []).
all_right(Root, [Current|Remaining]) :-
    Root < Current,
    all_right(Root, Remaining).



% insert_list(L, T1, T2) - insert a list L of items into a tree T1,
% resulting in T2
insert_list([], OldTree, OldTree) :- !.
insert_list([Current|Rest], OldTree, FinalTree) :-
    insert(Current, OldTree, OldWithCurrent),
    insert_list(Rest, OldWithCurrent, FinalTree), !.


























































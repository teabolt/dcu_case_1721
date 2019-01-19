/* Book recommender */

/*
Structures
*/

book(Title, Author, Genre, Size). /* structure representing a book instance */
Library = []. /* a variable pointing to a library, a list of book structure instances */


/*
Example facts
*/

book(illiad, homer, drama, 1000).
book(crime_and_punishment, dostoyevsky, crime).
book(it, king, fiction, 300).
book(datastructures_algorithms, knuth, study, 800).
book(medical_diseases, gp, reference, 2000).
book(infinitejest, wallace, comedy, 1000).

/*
Helper rules
*/
buildLibrary(Lib) :- findall(book(Title, Author, Genre, Size), book(Title, Author, Genre, Size), Lib).

/*
Rules
*/

literary(B, L) :- B(X, Y, drama, Z).
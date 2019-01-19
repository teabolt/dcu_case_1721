; Determine if a number in AL is prime.
; If it is prime, AL is unchanged.
; If it is not prime, AL is set to 00.

; A prime is a number that has only two divisors: 1 and itself.
; A number is a divisor of number p if when p is divided by the divisor \
; the remainder after division is zero.
; In other words, the divisor "goes in evenly" into p.

; The classic (though admitedly not the most efficient) primality algorith is to go through each number d between 2 and p-1.
; At each iteration, the remainder after dividing p by d is checked.
; If at any point the remainder is zero (the number goes in fully, it is a divisor) \
; the number is declared not prime.
; If the iteration finishes without finding any divisors, then the number is prime.
; There are base cases for primes 2, non-prime 1 and 0, and so on. (negative numbers - excluded here)

; This is based on the fundamental theorem of arithmetic.
; A number is either prime, or made out of primes multiplied together (it has prime divisors).
; something ... something ... I haven't a clue

CLO		; close previous/opened windows

; <TO-DO> (done) Interface for reading the number from the keyboard
MOV DL, 0
PUSH DL 			; null value for stack end (sentinel)

; Read two characters
IN 0				; read the first character
PUSH AL				; store MSB in stack
IN 0				; read the second character
PUSH AL				; store LSB in stack



; Translate each ASCII character code to actual hex values

; Digits 0 to 9: maths equation with range check (simpler maths)
; Digits A to F: contiguous array map		 (like 1 more instruction, but anyways...)

MOV DL, 2			; get two iterations
MOV CL, B0 			; store values in RAM (B0 and B1 - need to change - LSB then MSB)
loop:
POP AL				; get a digit
; check "ranges" that the digit falls into
digit_range:				; "decimal" range 0-9, ASCII ranges 29 to 40 exclusive
	MOV BL, 29			; lower bound
	CMP BL, AL			; BL is less than AL
	JNS mid				; number is not too small, mismatch - no point in checking the next range (has a higher upper range anyways - short circuit)
	MOV BL, 40			; upper bound
	CMP AL, BL			; AL is less than BL
	JNS letter_range		; number is not too big. go to next range to be checked
	JMP digit_process 		; number is in range


letter_range:				; "letter" range A-F, ASCII ranges 40 to 47 exclusive
	MOV BL, 40			; lower bound
	CMP BL, AL
	JNS mid
	MOV BL, 47			; upper bound
	CMP AL, BL
	JNS mid
	JMP letter_process		; the number is in this range	
	
	
; check if lowercase	
; SUB AL, 20			; normalise ASCII 60 to 40
; JMP letter_range		; need a loop
; out of memory if add this...
	

digit_process: 				; processing digits 0-9
	SUB AL, 30				; constant offset formula
	JMP condition				; next

letter_process:				; processing "letters" A-F
	SUB AL, 41			; map (complicating things with DB, RAM, etc) vs constant offset formula (harmonious)
	ADD AL, 0A
	JMP condition


condition:				; loop condition
	MOV [CL], AL
	INC CL
	DEC DL
	CMP DL, 0
	JNZ loop
	JMP calculate

	
; calculate the actual number
; in byte case (2 hex characters): MSB*10+LSB
calculate:
	MOV CL,	[B1]	; MSB 
	MOV DL,	[B0]	; LSB
	PUSH CL		; result=MSB*10+LSB
	POP AL
	MUL AL, 10
	ADD AL, DL
	JMP start

mid:
	JMP error

start:
; AL is the number whose primality is to be checked
; IN HEX AND LESS THAN 127 (7F IN HEX)

; base cases
CMP AL, 2
JZ prime
CMP AL, 1
JZ notprime
CMP AL, 0
JZ notprime
JS error	; negative numbers are not dealt with in this program


; primality algorithm for numbers greater than 2
MOV DL, 02	; initialise the starting divisor being tested
divisors:	; a 'do-while' construct loop
	PUSH AL
	POP BL			; temporary variable to store result of modulo in
	MOD BL, DL	 	; check for divisors
	JZ notprime		; found a divisor, exit the loop pre-emptively
	; did not find a divisor, next iteration
	INC DL
	CMP DL, AL	; check if not at the end
	JNZ divisors	; another iteration
	JMP prime	; done, number must be prime

; <TO-DO (done)> Print out if the number is prime on the VDU. Flash a LED if the number is/not prime
; program termination conditions
prime:
	PUSH AL
	POP DL			; temporary save for AL
	MOV AL, 04		; set a light to green
	OUT 1			
	PUSH DL
	POP AL			; move back to AL
	JMP terminate
notprime:
	MOV AL, 10		; set a light to red
	OUT 1
	MOV AL, 0		; reset AL
	JMP terminate
error:
	MOV AL, 8
	OUT 1
	; <TO-DO>: Add error codes for different types of error (char out of ascii range, neg num, etc). Write them to the VDU
terminate:
	END	; only one END is allowed per program


; <TO-DO> generally:
; -comments
; -optimised code
; -memory organisation
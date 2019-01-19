; Check if a hexadecimal number at AL is prime.
; If it is prime, leave it. If it is not prime, set AL to 0xFF.
; Test results for numbers 0x02 to 0x20 are in memory locations 0x72 to 0x90

; A number p is prime if its only divisors are 1 and p
; So the numbers 2 to p-1 never divide into p evenly

; Test by initially storing the numbers to be tested in the required memory locations (at run-time) \
; Then traversing the memory locations, leaving the numbers or setting them to FF as required

; Memory locations: 0x72 to 0x90
; Numbers: 0x02 to 0x20
MOV BL, 2		; initialise first number to be tested
MOV CL,	72		; initialise first memory location where the number and the result should be stored
test_writer:
	MOV [CL], BL	; move number to location
	INC BL		; next number
	INC CL		; next location
	CMP CL, 91	; check if not over the memory bound
	JNZ test_writer ; keep going
	; next phase

MOV CL, 72		; location of number to be tested first
test:
	MOV AL, [CL]

; check if a number in AL is prime. Registers BL and DL will be used
; base cases
; p = 2, prime
CMP AL, 2			; the number at AL is equal to 1
JZ prime			; therefore, the number is prime

; p = 1, not prime, only one divisor
CMP AL, 1		
JZ notprime

; p = 0, not prime, infinite divisors
CMP AL, 0
JZ notprime

; p < 0, not considered
CMP AL, 0
JS terminate

; 'algorithm' case - check each divisor from 2 to p-1 (not the most efficient solution)
MOV DL, 2		; starting divisor
divisors:
	PUSH AL
	POP BL		; work with BL, leave AL untouched
	MOD BL, DL	; check remainder after division
	JZ notprime	; remainder is zero, therefore number at DL is a divisor, so AL number is not prime
	INC DL		; move on to the next divisor
	CMP DL, AL	; check if at the end
	JNZ divisors	; next iteration
	JMP prime	; reached the end. No unwanted divisors found. Number is prime

prime:
	JMP next_test
notprime:
	MOV AL, FF
	MOV BL, FF
	MOV [CL], BL
	JMP next_test

next_test:
	INC CL
	CMP CL, 91	; not at the end
	JNZ test
terminate:
	END
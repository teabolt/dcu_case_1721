; Sum of odd numbers in a memory range
; Numbers are assumed to be unsigned hex (the absolute value of negative numbers is taken)
; Odd number endings: 1, 3, 5, 7, 9, B, D, F



JMP main



ORG 10	; test data here
DB 0
DB 1
DB 1
DB 2
DB 3
DB 5
DB 8
DB 13
DB 45
DB 46	; 10 numbers
DB FF
DB 7F
DB 81
DB 81
DB B1
DB C0



ORG 30	; procedure 'SUM_ODD', calculates the sum of odd numbers between two memory locations
	; Parameters: AL, BL, the two memory locations, AL <= BL
	; Returns: CL, the sum of the odd numbers
	PUSH AL	; back up used registers
	PUSH BL

	MOV CL, 0		; initialise counter
	sum_loop:		; a 'do-while' loop
		MOV DL, [AL]	; get the number
		; check if the number is odd
		PUSH BL		; free up a register
		PUSH DL		; copy DL to BL
		POP BL
		MOD BL, 2 	; number is even (0) or odd(1 or -1)
		MUL DL, BL 	; keep the number if it's odd (set to unsigned value), discard if it's even (set to 0)
		POP BL		; restore BL value
		ADD CL, DL 	; add to the sum
		INC AL		; onto the next number (move up the 'low' pointer)
		CMP BL, AL 	; BL < AL
		JS sum_end	; break out of the loop
		JMP sum_loop	; otherwise keep going

	sum_end:
	POP BL  ; restore backed up registers
	POP AL
	RET
; Note that the counter may overflow if the numbers added are too large to hold in an 8 bit register


ORG 70
main:
	MOV AL, 10	; inclusive range
	MOV BL, 1F
	CALL 30
	HALT	

END
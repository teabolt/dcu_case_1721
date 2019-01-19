; Fibonacci Sequence methods

; In the Fibonacci sequence, F_N, the value of term N (N > 0), 
; is the sum of the fibonacci values of the previous two terms,
; F_N = F_N-1+F_N-2
; The base cases are assumed to be F_0 = 0 and F_1 = 1


; main program
MOV AL, 0	; initialise term counter (start counting from 0)
loop:
	CALL 40		; get fibonacci value
	ADD AL, 20	; add cache offset
	MOV [AL], BL 	; save value
	SUB AL, 20	; restore term counter
	INC AL		; next term
	CMP AL, 20	; iterate for first 20 terms only
	JNZ loop
HALT



ORG 20  ; table 'CACHE' contains the cached fibonacci sequence terms, addresses [20] to [3F]
DB 0	; base case 1
DB 1	; base case 2



ORG 40	; procedure 'REC_FIB', recursive fibonacci sequence implementation
	; for a given term, returns its value
; Parameters: AL (term required to be calculated, positive integer)
; Returns: BL (value of term)
	PUSH AL	; back up used registers
	PUSH CL

	; base cases
	CMP AL, 0	; N = 0
	JZ recfib_base1
	CMP AL, 1	; N = 1
	JZ recfib_base2

	; recursive case
	DEC AL	; N-1 term
	; use the cache to get the terms
	; ADD AL, 20	
	; MOV CL, [AL]
	; SUB AL, 20	
	; calculate the value recursively
	CALL 40	; get the value, result in BL
	PUSH BL	; back up N-1 value
	POP CL	

	DEC AL	; N-2 term
	;ADD AL, 20
	;MOV BL, [AL]
	;SUB AL, 20
	CALL 40 ; result in BL

	ADD BL, CL	; F_N-2 + F_N-1 = F_N
	JMP recfib_end
	

	recfib_base1:
		MOV BL, [20]	; base cases are stored in the cache table
		JMP recfib_end
	
	recfib_base2:
		MOV BL, [21]

	recfib_end:
		POP CL	; restore used registers
		POP AL	
		RET



ORG 80  ; procedure 'ITER_FIB', iterative fibonacci sequence implementation
NOP



END
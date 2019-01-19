; Program for calculating square roots


main:
	MOV CL, C0
	MOV AL, 0
	loop:
		CALL 30
		MOV [CL], BL
		INC CL
		INC AL
		CMP AL, 40
		JNZ loop
	HALT
	


ORG 30	; procedure LOWER_ROOT, returns the square root of a number (rounded down if the root is not an integer)
; Input: AL (number)
; Output: BL (root)
; This is not a very efficient solution.
	; do something...

	RET


END
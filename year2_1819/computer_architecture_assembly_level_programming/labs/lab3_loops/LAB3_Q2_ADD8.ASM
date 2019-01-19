CLO
MOV CL, 8		; initialise counter
MOV AL, 0		; initialise total
adder:
	ADD AL, CL	; sum and carry
	DEC CL		; go to next count
	JNZ adder	; check if last operation - 'DEC CL' - is non-zero
END
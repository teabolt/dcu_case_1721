;	PROGRAM TO ITERATE THROUGH THE NUMBERS 1 TO N, inclusive

CLO
MOV AL, 1		; Starting number and index of the loop
MOV BL, 10	; Ending number

Loop:
	INC AL
	CMP AL, BL
	JMP Loop

END
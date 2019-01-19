; Procedure to print a character on a spot on the VDU, parametrised with AL and BL registers

CLO	; windows out the way
; test
MOV AL, C0	; [ to top left
MOV BL, 5B
CALL 70

MOV AL, CF	; ] to top right
MOV BL, 5D
CALL 70

MOV AL, D0	; loop example
MOV BL, 20
loop:
	CALL 70
	INC BL	
	INC AL
	CMP AL, 00	; check if not at end (FF overflows back to 0)
	JNZ loop

HALT


ORG 70
print:
; 'print' procedure puts ASCII character in BL onto the VDU location pointed to by AL
MOV [AL], BL	; put the character to the VDU location
RET

END
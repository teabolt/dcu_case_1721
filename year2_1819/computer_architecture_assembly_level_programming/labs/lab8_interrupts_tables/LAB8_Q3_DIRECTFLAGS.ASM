; Store a number directly to the flags register
; Copy the contents of a register into the flags register
; An implementation using the stack


JMP main


ORG 20	; procedure 'SET FLAG', sets the SR flags register to the value in a general purpose register
; Parameters: AL
; Returns: Modified SR
PUSH AL	; save AL onto the stack
POPF	; restore AL into the flags register
RET


ORG 70
main: 
	CLO	; close extra windows
	MOV AL, 2
	CALL 20
	JZ main
	HALT	


END
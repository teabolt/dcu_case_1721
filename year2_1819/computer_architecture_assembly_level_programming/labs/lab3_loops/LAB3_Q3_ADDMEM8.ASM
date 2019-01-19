; Store sum [08]+[07]+...+[00] (of values at memory addresses) in register AL

CLO
MOV AL, 0		; initialise sum register
MOV CL, 08 		; initialise register pointing to memory locations
memsum:
	MOV BL, [CL]	; store result of indirect read temporarily
	ADD AL, BL	; add to sum
	DEC CL		; move pointer to next location
	JNS memsum	; continue if have not reached address 00
END
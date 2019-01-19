; Write to memory locations [40], [41], ..., [49] the corresponding values of 40, 41, ..., 49
; A downwards loop implementation

CLO
MOV AL, 0A		; loop variable. Going 10 times until 0
MOV BL, 40		; memory location and value variable.
memwrite:
	MOV [BL], BL
	INC BL
	DEC AL
	JNZ memwrite
END
ORG 90
DB FB	; 0
DB 0B	; 1
DB B7	; 2
DB 9F	; 3
DB 4F	; 4
DB DD	; 5
DB FD	; 6
DB 8B	; 7
DB FF	; 8
DB CF	; 9

ORG 0
CLO

MOV BL, 90
bigger_loop:
	MOV AL, [BL]
	DEC AL	; show on left
	OUT 02
	MOV CL, 90
	smaller_loop:
		CALL 50	; show on right
		INC CL
		CMP CL, 9A
		JNZ smaller_loop
	INC BL
	CMP BL, 9A
	JNZ bigger_loop
HALT

; display number procedure
ORG 50
	PUSH AL
	MOV AL, [CL]
	OUT 02
	POP AL
	RET

; flip side of digit
ORG 60


END
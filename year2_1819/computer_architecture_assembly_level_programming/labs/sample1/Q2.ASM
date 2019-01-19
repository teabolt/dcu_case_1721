; 0 to 9 are codes 30 to 39



MOV DL, 0

; check if character read is between 29 and 3A


get_nums:
read:
	IN 0

check:
	MOV BL, 29
	CMP BL, AL	; BL < AL
	JNS read
	MOV BL, 3A
	CMP AL, BL 	; AL < BL
	JNS read
	PUSH AL
	INC DL
	CMP DL, 2
	JNZ get_nums

POP AL
SUB AL, 30
POP CL
SUB CL, 30
MUL AL, CL


END
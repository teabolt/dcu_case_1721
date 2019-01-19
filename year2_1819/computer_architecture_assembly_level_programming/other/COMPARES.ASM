; Comparisons based on equality, range, etc
; CMP AL, BL:		AL = BL: Z flag is set, AL < BL: S flag is set
; JNS label:		jump if S flag is set

CLO
MOV AL, 49
; check if AL falls into the range 29 and 40 (*exclusive bounds)
; lower bound
MOV BL, 29
CMP BL, AL		; BL is less than AL
JNS letters		; number is not too small
; upper bound
MOV BL, 40
CMP AL, BL		; AL is less than BL
JNS letters		; number is not too big
JMP terminate		; match this range

; if mismatch, go to next range comparison: 40 to 47 exclusive
letters:
	MOV BL, 40
	CMP BL, AL
	JNS terminate
	MOV BL, 47
	CMP AL, BL
	JNS terminate
	JMP terminate

terminate:
	END
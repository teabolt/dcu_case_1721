; Write ABC to the VDU at execution/run time

; ASCII codes: character - hex value
; A - 41
; B - 42
; C - 43

CLO
MOV CL, C0		; starting point of memory mapped VDU
MOV AL, 41		; starting ascii code of characters to write
MOV BL, 3		; use a loop variable to loop for 3 times, descending
print:
	MOV [CL], AL
	INC AL		; next character
	INC CL		; next screen position
	DEC BL		; another loop repetition
	JNZ print
END
   ; Split a read character to two digits and display each digit as a character on the VDU
; eg: read 6F -> register B holds 6, register C holds F -> display 6C *characters* on the VDU
; A-F is uppercase

; Relevant ASCII codes: (char: hex)
; 0-9: 30-39
; A-F: 41-46

CLO
MOV DL, 00
PUSH DL		; stack terminator

; from Q1
; THIS ONLY WORKS IF THE NUMBER IS NON-NEGATIVE, MOV AL, CC GIVES A WRONG DISPLAY
IN 00
PUSH AL
PUSH AL
POP BL
POP CL
AND BL, F0
DIV BL, 10
AND CL, 0F
; BL and CL are the most significant digit and the least significant digit respectively

; set up
PUSH CL		; store second digit
PUSH BL		; store first digit
POP DL 		; use DL to hold a single digit
MOV CL, C0	; use CL as the VDU pointer
; BL is a temporary value register

loop:		; use a loop for the two digits (a 'do-while' construct)
; translate values to ASCII codes

; two cases: value from 0 to 9 (a 'digit'), and value from A to F (a 'letter')
; check which case is it
; 0-9: less than A	
MOV BL, A
CMP DL, BL	; DL < A
JS to_digit	; it's a digit
; A-F: more than 9
MOV BL, 9
CMP BL, DL	; 9 < DL
JS to_letter	; it's a 'letter'

; do the translation
to_digit:	; 0 to 9
	; add 30 to make into a character code for 0-9
	ADD DL, 30
	JMP print

to_letter:	; A to F
	; add 37 to make into a character code for A-F
	ADD DL, 37

; print out the codes on the VDU
print:
	MOV [CL], DL
	INC CL

condition:	; loop condition
	POP DL
	CMP DL, 00	; check if stack terminator
	JNZ loop	; if not at the end
	PUSH DL		; push the stack terminator back


terminate:
	END
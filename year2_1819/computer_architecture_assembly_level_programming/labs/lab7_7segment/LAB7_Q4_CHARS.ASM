; Display various characters on the 7 segment display (letters)


JMP main


ORG 10	; table of characters for the 7 segment display (left side based)
	; start at position 0
DB FA	; 0
DB EE	; A
DB 7C	; B
DB F0	; C
DB 3E	; D
DB F4	; E
DB E4	; F
DB 52	; :|
DB 0	; table terminator

ORG 50	; procedure '7SEG_CLEAR', clears both sides of the 7 segment display
	PUSH AL ; back up used register
	; clear the left
	MOV AL, 00
	OUT 02
	; clear the right
	MOV AL, 01
	OUT 02
	POP AL	; restore used register
	RET

ORG 70 ; main program
main:
	MOV CL, 10	; initialise table pointer
	loop:           ; go through each character
		MOV AL, [CL] ; get the value
		CMP AL, 0
		JZ terminate ; if the value is the terminator (00), exit
		CALL 50	     ; clear the display
		OUT 02       ; display the new value
		INC AL	     ; display on the right side as well
		OUT 02
		INC CL	     ; move up to the next character
		JMP loop     ; onto the next
	terminate:
		HALT	


END
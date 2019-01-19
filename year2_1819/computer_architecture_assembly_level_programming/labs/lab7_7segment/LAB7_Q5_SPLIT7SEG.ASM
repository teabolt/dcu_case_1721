; Split the character code read from the keyboard into two digits, 
; displaying them on the 7 segment display
; Will have hex digits

JMP main



ORG 10	; table of hex digits (0-9 and A-F) (right side based)
DB FB ; 0	; address 10
DB 0B ; 1
DB B7 ; 2
DB 9F ; 3
DB 4F ; 4
DB DD ; 5
DB FD ; 6
DB 8B ; 7
DB FF ; 8
DB CF ; 9	; address 19
DB EF ; A	; address 1A
DB 7D ; B
DB F1 ; C
DB 3F ; D
DB F5 ; E
DB E5 ; F	; address 1F



ORG 20	; procedure 'SPLIT' splits a hex number into its two digit parts
; Parameters: AL - the input number
; Returns: AL, BL - the MSD and LSD of the number respectively
PUSH AL		; copy AL into BL
POP BL
; MSD
AND AL, F0	; keep the first four bits only
DIV AL, 10	; shift the first four bits to the left four times (to the next byte)
; LSD
AND BL, 0F	; keep the last four bits only
RET



ORG 30	; procedure '7SEG_VALUE' gets the value for displaying a hex digit
; Parameters: AL - the digit required
; Returns: AL - the value for the 7 segment display corresponding to the digit
ADD AL, 10	; offset + starting value = desired index
MOV AL, [AL]	; get the value
RET



ORG 70
main:
	CLO	; close unused windows
	; clear the 7 segment display
	MOV AL, 00	; left
	OUT 02
	MOV AL, 01	; right
	OUT 02
	IN 0	; read a character from the simple keyboard, value stored in AL
	CALL 20	; split the character code into its two digit values
	; MSD
	CALL 30 ; get the 7seg value
	DEC AL	; display on the left
	OUT 02
	; LSD
	PUSH BL ; copy BL to AL
	POP AL
	CALL 30
	OUT 02
	HALT

END
; Read a character and display its code on the 7 segment display
; Character must be between 0 and 9
; The program is terminated by 'q'
; Relevant devices:
; 7seg - Port 02 write-only
; Simple keyboard - Port 00, read-only



JMP main



ORG 10	; 7 segment table, digits 0 to 9 (no A-F letters) (left based)
DB FA	; 0
DB 0A	; 1
DB B6	; 2
DB 9E	; 3
DB 4E	; 4
DB DC	; 5
DB FC	; 6
DB 8A	; 7
DB FE	; 8
DB CE	; 9

ORG 30 ; procedure 'GET 7SEG VALUE', calculates the 7 segment value for a digit using the table
; Parameters: AL, the number whose value is required
; Returns: AL with its value modified to the required 7seg value
	ADD AL, 10
	MOV AL, [AL]	
	RET

ORG 50	; procedure 'SPLIT DIGIT', splits a two-digit hex number into its MSB and LSB
; Parameters: AL
; Returns: MSB in AL, LSB in BL
	PUSH AL	; copy AL into BL
	POP BL
	AND AL, F0	; keep the first four binary digits
	DIV AL, 10	; shift the digits to the right four times
	AND BL, 0F
	RET

ORG 70
main:
	loop:		; a 'do while loop'
		IN 00		; read a character (assuming it's from 0 to 9)
		CMP AL, 71	; check if the character is 'q'
		JZ exit	; end if it is

		CALL 50 ; split the character code into two digits (in AL and BL)
		CALL 30 ; get value for MSB
		OUT 02	
		PUSH BL	; copy BL into AL
		POP AL
		CALL 30	; get value for LSB
		INC AL	; modify the right side	
		OUT 02
		JMP loop

	exit:
		HALT

END
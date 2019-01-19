; Count on the 7 segment display in decimal from 00 to 99
; Implementation details:
; A 'DIGIT TUPLE'(DTUPLE) data structure (own made) is used
; It is of the form (a, b), where a and b are between 0 and 9 inclusive
; Essentially this represents counting in decimal, eg: 0,0; 0,1 ... 0,9; 1,0 ...
; It is hoped that this 'separation' (decoupling) of logic and the 7 segment presentation will help the program structure

JMP main



ORG 10 ; 7 segment display table for digits 0-9 (right panel version)
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



ORG 20	; procedure 'DTUPLE_INCREMENT', increases the decimal count by 1, or keeps it at the upper limit (9,9)
; Parameters: BL (MSD), CL (LSD)
; Returns: Modified BL and CL
	INC CL	; increment LSD
	; check if overflow
	CMP CL, 0A
	JNS inc_msd	; CL >= 0A (overflow
	JMP inc_end     ; CL < 0A (no overflow)

	inc_msd:	; increment MSD
		INC BL
		; check if no overflow
		CMP BL, 0A
		JNS inc_roof	; overflow (reached maximum value, and keep at it)	
		; no overflow
		MOV CL, 0	; reset LSD
	inc_end:
		RET
	
	inc_roof:
		MOV BL, 9	; set both MSD and LSD to the maximum value
		MOV CL, 9
		JMP inc_end



ORG 40	; procedure '7SEG_VALUE', gets the value required to display a digit on the 7 segment display
	; uses the table defined
; Parameters: AL (the digit)
; Returns: AL with the value
	PUSH BL	; back up used register
	
	MOV BL, 10	; initial starting point
	ADD BL, AL	; add offset
	MOV AL, [BL]	; get the actual value

	POP BL	; restore registers
	RET



ORG 50 ; procedure 'DTUPLE_DISPLAY', displays the values of the DTUPLE on the 7-seg display
	; uses the '7SEG_VALUE' procedure to get values
; Parameters: BL (MSD), CL (LSD)
	PUSH BL ; back up used registers
	PUSH CL

	; LSD
	PUSH CL ; copy CL to AL
	POP AL
	CALL 40 ; get the value
	OUT 02  ; show it

	; MSD
	PUSH BL
	POP AL
	CALL 40
	DEC AL	; use the left side of the 7seg
	OUT 02

	POP CL ; restore registers
	POP BL
	RET



ORG 70 ; main program
main:
	CLO  ; close some windows
	; clear the 7 segment display
	MOV AL, 00
	OUT 02
	MOV AL, 01
	OUT 02
	; initialise the DTUPLE data structure with appropriate starting values
	MOV BL, 0	; represents the MSD
	MOV CL, 0	; represents the LSD
	loop:		; runtime loop
		CALL 50		; display the DTUPLE
		CALL 20		; increment the DTUPLE by one
		JMP loop
	HALT ; stop the CPU



END	; end of source code
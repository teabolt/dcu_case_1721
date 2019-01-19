; Using the 7-segment display, count down from 9 to 0
; Be able to use both the right side and left side
; Use procedures

; The seven segment display is on port 2
; It is a write-only device
; It takes input from AL
; The first (MSB) seven bits are the pattern. 
; The last (LSB) is 1 for controlling 									right side, 0 for the left side
; Lights stay on until turned off - they must be turned off by sending 0's

; Use a table. Hex values for 7 segment display, for right side
ORG 90	; starting point of table
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
DB 10	; table terminator (00010000), should not be used as a value in the table

ORG 0
CLO
MOV AL, 90	; initialise pointer to table
loop:
	CALL 50
	INC AL
	MOV BL, [AL]
	CMP BL, 10
	JNZ loop
	HALT

ORG 50 		; 'display' procedure
; reads value at AL and displays it to the 7 segment display
PUSH AL
MOV AL, [AL]
OUT 02
POP AL
RET

ORG 70


END
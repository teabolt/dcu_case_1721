; Count down using the seven segment display from 99 to 00 (use both digits)
; every second (timer interrupt)
; configuration -> set hardware timer interval to 1 second

; Relevant device info:
; Hardware timer is at 0x02 of IVT
; 7-segment display is write-only at port 02


JMP main	; jump over the IVT
DB 20		; address of ISR for the hardware timer
DB 0
DB 0
DB 1F		; software interrupt 0x05, terminate program (jumps to 00/empty value)

ORG 10		; 7 segment display numbers table ('left side' form) ; better to have right side? Change LSB most of the time - have it in the normal form
DB FA ; 0	; at position 10
DB 0A ; 1
DB B6 ; 2
DB 9E ; 3
DB 4E ; 4
DB DC ; 5
DB FC ; 6
DB 8A ; 7
DB FE ; 8
DB CE ; 9	; at position 19


ORG 20	; 'hardware timer' ISR
; print the number and get the next one
CLI
PUSH AL 	; back up used register
MOV AL, 10	; start of table
ADD AL, BL	; required number's index = start+offset
MOV AL, [AL]	; get the 7-segment display value
OUT 02		; display
MOV AL, 10
ADD AL, CL	; get LSB
MOV AL, [AL]
INC AL		; switch to right side
OUT 02
CALL 50		; get the next numbers in tuple
POP AL		; restore used register
IRET


ORG 40; procedure 'CLEAR_7SEG'
PUSH AL	; backup used register
MOV AL, 00	; turn off the left side
OUT 02
INC AL		; turn off the right side
OUT 02
POP AL	; restore register
RET



ORG 50	; procedure 'DECREMENT TUPLE'
; Paremeters:
; BL - MSD, CL - LSD
; Returns decremented BL and CL, with appropriate overflow handling
DEC CL			; modify LSB
JS msb	; CL < 0 	; check if overflown
JMP end_dec		; no overflow, finished
msb:			; overflown, change MSB (reset LSB)
DEC BL			; modify MSB
JS base	; BL < 0	; check if overflown (reached the 'lowest' value)
; no overflow
MOV CL, 9		; reset LSB
JMP end_dec		; exit the procedure
base:
	MOV BL, 0	; reached (0, 0)
	MOV CL, 0
end_dec:
	RET



ORG 70                                                                       
main:	; start the actual program
	CLO	; close undesirable windows
	; CALL 60	; clear the 7-segment display
	; data structure - a tuple of two digits 0 to 9, represents the 7-segment decimal digit
	; has a method 'DECEREMENT_TUPLE', over BL and CL	
	MOV BL, 9	; initialise the tuples
	MOV CL, 9
	loop:
		STI
		JMP loop
	HALT	; a useless HALT?

END